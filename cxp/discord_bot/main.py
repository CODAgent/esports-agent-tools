import discord
import os
import re

from general_helper_functions import get_bot_token

# SERVER = "LonelyDock3's server"
SERVER = "College XP CoD"

list_of_admins = ['lonelydock3']

# list of commands and the number of arguments they require
command_map = {'delete_category_matches': 1}
list_of_commands = list(command_map.keys())

bot_token = get_bot_token('bot_token.txt')

async def execute_command(Client, guild, command, args_list):
    success = 0
    if command == list_of_commands[0]:      # delete_category_matches
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

