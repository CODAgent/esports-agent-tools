import discord
import os
import re

from general_helper_functions import get_bot_token
from general_helper_functions import read_create_matches_csv

# SERVER = "LonelyDock3's server"   # TESTING
SERVER = "College XP CoD"   # DEPLOYMENT

list_of_admins = ['lonelydock3', 'shanethor']

# list of commands and the number of arguments they require
command_map = {'delete_category_matches': 1, 'create_category_matches': 1}
list_of_commands = list(command_map.keys())

bot_token = get_bot_token('bot_token.txt')

async def execute_command(Client, guild, command, args_list):
    success = 0

    # delete_category_matches 
    if command == list_of_commands[0]:
        # for this command, we can only input one category
        category_given = ' '.join(args_list)
        
        # get category
        guild_categories = guild.categories
        channel_list = []
        for categoryIdx, category in enumerate(guild_categories):
            if category.name == category_given:
                # get channels under the category that are matches 
                channels = category.text_channels
                for channelIdx, channel in enumerate(channels):
                    if '-vs-' in channel.name:
                        channel_list.append(channel)

        for chIdx, ch in enumerate(channel_list):
            print('Deleting text channel: ' + ch.name + ' ....')
            await ch.delete()
            print('Deleted')
                

        success = 1

    # create_category_matches 
    elif command == list_of_commands[1]:
        # get category name
        category_given = ' '.join(args_list)

        # create the category 
        await guild.create_category(category_given)

        for categoryIdx, category in enumerate(guild.categories):
            if category.name == category_given:
                category_obj = category

        # read in the csv file 
        # matches_dict = read_create_matches_csv('create_matches_input/test_input.csv')     # TESTING 
        matches_dict = read_create_matches_csv('create_matches_input/input_file.csv')     # DEPLOYMENT

        # create names for the text channels, get each member from the team captain lists, get the role(s) needed to add to the channels 
        dict_keys = list(matches_dict.keys())

        # if the member is not found, None will be returned 
        cxp_manager_role = guild.self_role

        guild_roles = guild.roles
        admin_role = None
        # get the admin role (if there is one)
        for roleIdx, role in enumerate(guild_roles):
            if role.name == 'Admin':
                admin_role = role

        created_channels = {'away_members': [], 'home_members': [], 'text_channels': []}

        # create the channels and get the info we need
        for rowIdx, row in enumerate(matches_dict[dict_keys[0]]):
            away_team = matches_dict['away_team'][rowIdx]
            home_team = matches_dict['home_team'][rowIdx]
            away_team_captain = matches_dict['away_team_discord_captain'][rowIdx]
            home_team_captain = matches_dict['home_team_discord_captain'][rowIdx]

            # format the match name properly 
            match_name_preprocess = away_team + ' vs ' + home_team
            match_name = match_name_preprocess.replace(' ', '-').lower()

            # fetch the discord users of away team and home team 
            away_team_member = guild.get_member_named(away_team_captain)
            home_team_member = guild.get_member_named(home_team_captain)

            created_channels['away_members'].append(away_team_member)
            created_channels['home_members'].append(home_team_member)

            admin_permissions = discord.PermissionOverwrite()
            admin_permissions.read_messages = True
            admin_permissions.manage_channels = True

            cxp_manager_permissions = discord.PermissionOverwrite()
            cxp_manager_permissions.read_messages = True
            cxp_manager_permissions.manage_channels = True

            overwriter = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                admin_role: admin_permissions,
                cxp_manager_role: cxp_manager_permissions
            }

            created_channels['text_channels'].append(await guild.create_text_channel(match_name, category=category_obj, overwrites=overwriter))
            print('Created channel named: ' + match_name)
        
        # add the permissions onto the channels just created 
        for channelIdx, channel in enumerate(created_channels['text_channels']):
            created_channel = channel
            away_team_member = created_channels['away_members'][channelIdx]
            home_team_member = created_channels['home_members'][channelIdx]

            away_overwrite = discord.PermissionOverwrite()
            away_overwrite.read_messages = True
            away_overwrite.send_messages = True

            home_overwrite = discord.PermissionOverwrite()
            home_overwrite.read_messages = True
            home_overwrite.send_messages = True

            admin_overwrite = discord.PermissionOverwrite()
            admin_overwrite.read_messages = True
            admin_overwrite.send_messages = True
            admin_overwrite.manage_channels = True
            admin_overwrite.manage_messages = True

            if away_team_member:
                await created_channel.set_permissions(away_team_member, overwrite=away_overwrite)
            if home_team_member:
                await created_channel.set_permissions(home_team_member, overwrite=home_overwrite)
            if cxp_manager_role:
                await created_channel.set_permissions(cxp_manager_role, overwrite=admin_overwrite)
            if admin_role:
                await created_channel.set_permissions(admin_role, overwrite=admin_overwrite)

            print('Added permissions to recently created channel.')

        success = 1


    return success

def get_guild_on(Client, guild_on):
    list_of_guilds = []
    for guildIdx, guildObj in enumerate(Client.guilds):
        list_of_guilds.append(guildObj)
    for guildIdx, guild in enumerate(list_of_guilds):
        if guild.name == guild_on:
            return guild


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        guild = get_guild_on(self, SERVER)

        message_author = str(message.author)
        message_content = str(message.content)

        # commands 
        if message_author in list_of_admins:
            if len(message_content) > 0:
                searching_command = re.search('^cxp\/[^\s]*', message_content)
                if searching_command != None:
                    command_said = searching_command.group(0)[4:len(searching_command.group(0))]
                    if command_said in list_of_commands:
                        args_info = command_map[command_said]

                        # command requires arugments 
                        if args_info != None:
                            min_num_args = args_info
                        # command does not take arguments 
                        else:
                            min_num_args = 0
                        
                        getting_args = re.search('(?<=cxp\/' + command_said + '\s).*', message_content)
                        args_str = getting_args.group(0)
                        list_of_args = args_str.split()

                        if not(len(list_of_args) >= min_num_args):
                            raise Exception('Invalid number of arguments.')

                        command_execute_res = await execute_command(self, guild, command_said, list_of_args)

                        if command_execute_res != 1:
                            raise Exception('Error executing command.')



                        
                

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(bot_token)

