import discord
import os
import re

from general_helper_functions import get_bot_token
from general_helper_functions import read_create_matches_csv

SERVER = "LonelyDock3's server"
# SERVER = "College XP CoD"

list_of_admins = ['lonelydock3']

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

        # going to use ```create_text_channel(name, category=category_obj)``` on the guild 
        # might need to pass it a dictionary to provide the roles/members who have access to the channel 
        # await guild.create_text_channel('test', category=category_obj)

        # read in the csv file 
        # matches_dict = read_create_matches_csv('create_matches_input/input_file.csv')
        matches_dict = read_create_matches_csv('create_matches_input/test_input.csv')

        # create names for the text channels, get each member from the team captain lists, get the role(s) needed to add to the channels 


        # create the text channels with the proper members and role(s) added to them 

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

client = MyClient(intents=intents)
client.run(bot_token)

