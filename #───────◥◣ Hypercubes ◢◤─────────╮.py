#───────◥◣ Hypercubes ◢◤─────────╮

# My First Python Bot
# Disruptor - February 2023

import calendar
import discord
import asyncio
import sqlite3
import random
import typing
import time
import pytz
import os
import re
#import logging; logging.basicConfig(level=logging.DEBUG)


from datetime import datetime, timedelta
from discord.ext import commands, tasks
from collections import defaultdict
from time import sleep
from os import system
from discord import TextChannel
from typing import Dict, Union

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
#⊱──────────────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ List off all commands ☆ ⋅.}───────────────⊰

# Define !h & !help
@bot.command(name='h', category='Help')
async def help(ctx):
    #docstring 
    """List all available commands."""
    embed = discord.Embed(title="", description="""
╭⋆✼⋅⋆**Commands** 
✼
`!h`
`cl`Command details
✼
`remindme nm r`
`stopremind`
`rar`remove reminder
✼
`timestamp`
`convert`
✼
`partner`
`inv` / `invite`
`ip` / `server`
`le`list emojis
`roles`
✼
`startaddroles`
`stopaddroles`
✼
`updateroles`
`removeroles`
✼
`add_channel id`
`list_channels`
`set_clear_frequency nh|nm`
`start`Start clear
`stop` Stop clear
`remove_channel id`
✼
You need Administrator permission
✼
╰────── ⋆⋅ ✼ ⋅⋆
""", color=discord.Color.green())
    embed.set_author(name="Time To do Some Cleaning", icon_url="https://cdn-icons-png.flaticon.com/512/2954/2954888.png")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2954/2954888.png") 

    message=await ctx.send(embed=embed)
    await message.add_reaction("🏃‍♀️")
    await message.add_reaction("💨")
    await message.add_reaction("🌬️")
    await message.add_reaction("🔫")
#⊱──────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Commands Descriptions ☆ ⋅.}───────────────⊰

#list items in pages and switch pages with emojis
@bot.command(name='commands_list', category='Help', aliases=['cl'])
async def commands_list(ctx):
    items = [
        #Page 1
"╭⋆ ✼ ⋅⋆ **Commands in details**",
"┃",
"┃ ⁠ ⁠ ⁠ ✼ ⁠     Here's a list of all available commands:",
"┃",
"┃      ▷ ⁠ `!h` ",
"┃Embed List of commands",
"┃      ▷ ⁠ `!cl`",
"┃Commands In Details",
"┃",
"┃      ▷ ⁠ `!remindme nm r`",
"┃use m,h,d as time interval", 
"┃add or remove `r` for repeat",
"┃`!remindme 1h`|`!remindme 2m r`|`!remindme 3d`",
"┃      ▷ ⁠ `!stopremind`",
"┃Stop all reminders",
"┃      ▷ ⁠ `!rar`",
"┃remove reminders",
"┃",
"┃",
"╰────── ⋆⋅ ✼ ⋅⋆ ",
        #Page 2
"╭⋆ ✼ ⋅⋆ **Page 2**",
"┃",
"┃      ▷ ⁠ `!timestamp`",
"┃Display current time in <t::f> format",
"┃      ▷ ⁠ `!convert`",
"┃Generate a timestamp using format",
"┃`!convert 2023 3 18 1 30`" ,
"┃where 1 30 = 7.30am  , 2 30 = 8.30am",
"┃missing arguments will be set to current",
"┃",
"┃      ▷ ⁠ `!partner`",
"┃partner/ affiliate inv message",
"┃      ▷ ⁠ `!inv` / `!invite`",
"┃ invite link",
"┃      ▷ ⁠ `!ip` / `!server`",
"┃list server ip",
"┃      ▷ ⁠ `!le`list emojis",
"┃      ▷ ⁠ `!roles` list roles",
"┃",
"╰────── ⋆⋅ ✼ ⋅⋆ ",
        #Page 3
"╭⋆ ✼ ⋅⋆ Page 3",
"┃",
"┃",
"┃",
"┃      ▷ ⁠ `!startaddroles`",
"┃add predefined role to joining members",
"┃send a welcome message to new members",
"┃edit role in code",
"┃      ▷ ⁠ `!stopaddroles`",
"┃stop adding roles for new members",
"┃",
"┃      ▷ ⁠ `!updateroles`",
"┃add a role to all members",
"┃edit role in code",
"┃      ▷ ⁠ `!removeroles`",
"┃remove a role to all members",
"┃",
"┃",
"┃",
"╰────── ⋆⋅ ✼ ⋅⋆ ",
        #page 4
"╭⋆ ✼ ⋅⋆ Page 4",
"┃",
"┃      ▷ ⁠ !`add_channel id`\`ac`",
"┃add channel to clear list",
"┃      ▷ ⁠ !`list_channels`",
"┃list current channels set to clear",
"┃      ▷ ⁠ !`set_clear_frequency nh|nm`\`scf`",
"┃set the time to clear channels",
"┃set time with minutes m or hours h",
"┃`!scf 3m` |`!sch 24h`",
"┃      ▷ ⁠ !`start`Start clear",
"┃      ▷ ⁠ !`stop` Stop clear",
"┃      ▷ ⁠ !`remove_channel id`\`rc`",
"┃remove a channel from clear list",
"┃",
"┃You need Administrator permission",
"┃for most of the commands",
"┃",
"┃",
"╰────── ⋆⋅ ✼ ⋅⋆ ",
        #page 5
#"Item..."
# "Item 8",
# "Item 9",
# "Item 10",
# "Item 11",
# "Item 12",
# "Item 13",
# "Item 14",
# "Item 15",
# "Item 16",
# "Item 17",
# "Item 18",
# "Item 19",
# "Item 20",

]
    
    page_size = 20  # number of items to display per page \changing this will change also the layout u want to appear in discord so careful
    num_pages = (len(items) // page_size) + 1  # calculate the number of pages needed
    pages = []
    for i in range(num_pages):
        start_index = i * page_size
        end_index = min((i+1) * page_size, len(items))
        page_items = items[start_index:end_index]
        page_content = "\n".join(page_items)
        pages.append(page_content)

    current_page = 0
    message = await ctx.send(pages[current_page])
    await message.add_reaction('◀️')
    await message.add_reaction('▶️')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['◀️', '▶️']

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == '▶️' and current_page < len(pages)-1:
                current_page += 1
                await message.edit(content=pages[current_page])
            elif str(reaction.emoji) == '◀️' and current_page >= 0:
                current_page -= 1
                await message.edit(content=pages[current_page])
            await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.clear_reactions()
            break
#⊱─────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Reminder ☆ ⋅.}───────────────⊰

#remind at a specific Time with repeat option
REMINDERS = {}

async def send_reminder(ctx, reminder):
    await ctx.author.send(f"Hey {ctx.author.name}, here's your reminder to {reminder}!")
    await ctx.send(f"Hey {ctx.author.mention}, I sent you a reminder to {reminder} in your DMs!")

async def schedule_reminder(ctx, time, reminder, repeat):
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    time_val = int(time[:-1]) * time_convert[time[-1]]
    
    await ctx.send(f"Okay, I will remind you to {reminder} in {time}.")
    await ctx.author.send(f"Okay, I will remind you to {reminder} in {time}.")
    
    while repeat:
        await asyncio.sleep(time_val)
        await send_reminder(ctx, reminder)

@bot.command(name='remindme', category='Reminder')
async def remindme(ctx, time: str, repeat: str = "", *, reminder: str):
    
    """
    #docstring
    Sets a reminder for a specified amount of time.
    Time format m=minutes, h=hours, d=days. 
    r for repeat.
    Usage: !remindme 3h Take a break
    Usage: !remindme 30m r Take a break (repeat every 30 minutes)
    """
    repeat = repeat == "r"
    task = asyncio.create_task(schedule_reminder(ctx, time, reminder, repeat))
    REMINDERS[ctx.author.id] = task
    
@bot.command(name='stopremind', category='Reminder')
async def stopremind(ctx):
    """
    Stops all reminders for the user who sent the command.
    Usage: !stopremind
    """
    if ctx.author.id in REMINDERS:
        REMINDERS[ctx.author.id].cancel()
        del REMINDERS[ctx.author.id]
        await ctx.send("All reminders stopped.")
    else:
        await ctx.send("You don't have any reminders.")

@bot.command(name='removeallreminders', category='Reminder', aliases=['rar'])
async def removeallreminders(ctx):
    """
    Removes all reminders for all users.
    Usage: !removeallreminders \  !rar
    """
    for reminder in REMINDERS.values():
        reminder.cancel()
    REMINDERS.clear()
    await ctx.send("All reminders removed.")
#⊱─────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Timestamp ☆ ⋅.}───────────────⊰

#Current Timestamp
@bot.command(name='timestamp', category='Timestamp')
async def timestamp(ctx, day: int = None, month: int = None, year: int = None, hour: str = None, minute: int = None):
    """
    Usage: !timestamp
    """
    try:
        # Check if any arguments are None, and set them to current date/time if they are
        now = datetime.now()
        year = year or now.year
        month = month or now.month
        day = day or now.day
        hour = hour or now.strftime('%I%p').lower()
        minute = minute or now.minute

        # Adjust hour for AM/PM
        if hour[-2:] == "pm":
            hour = str(int(hour[:-2]) + 12)
        else:
            hour = hour[:-2].zfill(2)

        # Parse the input values into a datetime object
        dt = datetime(year=year, month=month, day=day, hour=int(hour), minute=minute)

        # Convert the datetime object to a UNIX timestamp and format it for Discord
        unix_time = int(dt.timestamp())
        timestamp = f"<t:{unix_time}:f>"

        # Send the timestamp to the user
        await ctx.send(f"The timestamp For: {timestamp} is `{timestamp}`")

    except ValueError as e:
        # Send an error message to the user if there was an issue with the input values
        await ctx.send(f"An error occurred: {str(e)}")

#get a specific timestamp !convert 2023 3 18 1 30  where 1 30 = 7.30am  , 2 30 = 8.30am
@bot.command(name='convert2timestamp', category='Timestamp', aliases=['convert'])
async def convert2timestamp(ctx, *args):
    """
    Get <\
    Usage: !convert 2023 3 18 1 30  where 1 30 = 7.30am  , 2 30 = 8.30am (in my local time zone)
    """
    try:
        # Get the current date/time
        now = datetime.now()

        # Set the default values for any missing arguments
        year = now.year
        month = now.month
        day = now.day
        hour = None
        minute = None

        # Parse the input arguments
        for i, arg in enumerate(args):
            if i == 0:
                year = int(arg)
            elif i == 1:
                month = int(arg)
            elif i == 2:
                day = int(arg)
            elif i == 3:
                hour = int(arg)
            elif i == 4:
                minute = int(arg)
            elif i == 5:
                if arg.lower() == 'am' or arg.lower() == 'pm':
                    if hour is not None:
                        hour = hour % 12 + 12 if arg.lower() == 'pm' else hour % 12
                else:
                    raise ValueError("Invalid time format")

        # Fill in missing time arguments with current time
        hour = hour or now.hour
        minute = minute or now.minute

        # Convert the input values into a datetime object
        dt = datetime(year=year, month=month, day=day, hour=hour, minute=minute)

        # Convert the datetime object to a Unix timestamp and format it for Discord
        unix_time = int(dt.timestamp())
        timestamp = f"<t:{unix_time}:f>"

        # Send the timestamp to the user
        await ctx.send(f"The timestamp For: {timestamp} is `{timestamp}`")

    except ValueError as e:
        # Send an error message to the user if there was an issue with the input values
        await ctx.send(f"An error occurred: {str(e)}")
#⊱─────────────────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Post Commands ☆ ⋅.}───────────────⊰

# ▩━━━━━◈ Partnership / Affiliate ◈━━━━━▩
@bot.command(name='partner', category='Post Commands', aliases=['affiliate'])
async def partner_command(ctx):
    #post as code in discord
    code = '''
╭╭⋆✼ 🅹🅾🅸🅽 ⋅⋆  ℍ ℽ ℙ ℰ ℛ ℂ Ⴎ ℬ ℰ Տ
┃ 
┃   ʕ•́ᴥ•̀ʔっ  Exclusives :
┃      
┃     ➤ 65 Custom Enchants
┃     ➤ Tnt Canon
┃
●Tags:"HolyKnight,Guardian,eGirl"&More
┃
┃     ➤ new Massive PVP Arena
┃     ➤ Quest Gui System
┃
● Fishing {Random items from Sea}
┃
┃     ➤ Trade Gui System
┃     ➤ Defense Towers
┃     ➤ new OverClaim System
●
┃   ʕ•́ᴥ•̀ʔっ  for limited Time
┃
┃     ➤ Redeem Daily Chest
┃     ➤ Free Keys Drop
●
┃
● Season 2 Release Date:"00-00-2023"
┃
┃
¸☆'.•'
.•'✶'*.
.¸v . ¸•' ¸',•'¨¸
¸✶.•'¸.•'✶
☆'¸.•★' ¸.✶* ☆★
╱◥◣
│∩ │◥███◣ ╱◥███◣
╱◥◣ ◥████◣▓∩▓│∩
│╱◥█◣║∩∩∩ ║◥█▓ ▓█
╰──────────────────────────── ⋆⋅ ✼ ⋅⋆
'''

    messages = [
        "\n",
        "⬛⬛⬛⬛🟩🟩⬛🟩🟩⬛⬛",
        "⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛",
        "⬛⬛🟩🟩⬜⬛⬜⬜⬛🟩⬛    𝓙𝓸𝓲𝓷",
        "⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛          ᑎOᗯ",
        "⬛🟩🟩🟩🟩🟫🟫🟫🟫⬛⬛",
        "⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛",
        "       𝔻𝕠𝕟'𝕥 𝔻𝕚𝕤𝕒𝕡𝕡𝕠𝕚𝕟𝕥 𝕄𝕖",
        "\nhttps://media.discordapp.net/attachments/664948888058200152/667351517707370506/HyperCubes.gif \nhttps://discord.gg/GbdxtUBqbe",
    ]

    # Concatenate all messages in a single string
    all_messages = "\n".join(messages)
    await ctx.send(f"\n```python\n{code}\n```\n{all_messages}")#post code in python ten messages
#⊱-------------------------------------------------------------------------------------------------⊰

# ▩━━━━━◈ Invite link ◈━━━━━▩
@bot.command(name='invite', aliases=['inv'], category='Post Commands')
async def invite_link(ctx):
    await ctx.send('Here is the invite link: \nhttps://media.discordapp.net/attachments/664948888058200152/667351517707370506/HyperCubes.gif \nhttps://discord.gg/GbdxtUBqbe')
#⊱-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------⊰

# ▩━━━━━◈ IP ◈━━━━━▩
# Define the function that will be executed by the commands
def ServerIp():
    embed = discord.Embed(title="", description="""
╭⋆✼⋅⋆**Hypercube Server Details** 
✼
FACTION:
**IP**➤ Coming Soon
**Port**➤ Default
✼
╰────── ⋆⋅ ✼ ⋅⋆
    """, color=discord.Color.green())
    embed.set_author(name="Minecraft Server Details", icon_url="https://cdn.discordapp.com/attachments/611102853536415769/619243094323232801/hypercubes.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/611102853536415769/1084234202762989660/pngaaa.com-310383.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/611102853536415769/1084234201869602938/pngaaa.com-4540357.png")
    return embed

# Server ip
@bot.command(name='minecraft', aliases=['ip', 'server'], category='Post Commands')
async def minecraft_command(ctx):
    await ctx.send(embed=ServerIp())
#⊱-------------------------------------------------------------------------------------------------⊰

# ▩━━━━━◈ List All Emojis  ◈━━━━━▩
@bot.command(name='listemojis', aliases=['le'], category='Post Commands')
@commands.has_permissions(administrator=True) 
async def listemojis(ctx):
    emojis = ctx.guild.emojis
    emoji_names = [str(emoji) for emoji in emojis]
    await ctx.send("\n""Server Emojis: {}".format(" ".join(emoji_names)))
#⊱───────────────────────────────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Roles ☆ ⋅.}───────────────⊰

# ▩━━━━━◈ List All Roles  ◈━━━━━▩
@bot.command(name='roles', category='Post Commands')
@commands.has_permissions(administrator=True) 
async def roles(ctx):
    try:
        server = ctx.guild
        roles='\n'.join(
                map(lambda role: f"{role.mention}", server.roles))
        em=discord.Embed(title=f"Roles [{len(server.roles)}]",description=roles, color=0xa8165f)
        await ctx.send(embed=em)
    except Exception as error:
        await roles_error(ctx, error)

@roles.error
async def roles_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, you don't have permission to use that command.")
    else:
        await ctx.send(f"An error occurred: {error}")
#⊱----------------------------------------------------------⊰

# ▩━━━━━◈ Auto add Roles for New Members + Welcomer  ◈━━━━━▩

# Define an event that adds roles to members when they join the server
add_roles_enabled = True
async def add_roles_to_new_member(member):
    # Get the roles IDs you want to add
    role_ids = [1080258166308221120]#add roles id u want members to get when they join here [1080431722992238652, 987654321]. Currently >> Release + Pack -Temp Role

    # Loop through the role IDs and add the roles to the roles list
    roles = []
    for role_id in role_ids:
        role = member.guild.get_role(role_id)
        if role:
            roles.append(role)

    # Add the roles to the new member
    await member.add_roles(*roles)

    # Send a welcome message
    welcome_channel = discord.utils.get(member.guild.channels, name="【👣】")
    if welcome_channel:
        await welcome_channel.send(f"Welcome, {member.mention}!")
    print(f"{member.name} joined the server.")

# Listen for the on_member_join event
@bot.event
async def on_member_join(member):
    global add_roles_enabled
    if add_roles_enabled:
        await add_roles_to_new_member(member)

# Define a command to start the event of adding role to new joined members
@bot.command(name='startaddroles', category='@Join Roles', aliases=['startar'])
@commands.has_permissions(administrator=True) 
async def startaddroles(ctx):
    global add_roles_enabled
    add_roles_enabled = True
    await ctx.send("New member role assignment enabled.")
    print("New member role assignment enabled.")

# Define a command to stop the event
@bot.command(name='stopaddroles', category='@Join Roles', aliases=['stopar'])
@commands.has_permissions(administrator=True) 
async def stopaddroles(ctx):
    global add_roles_enabled
    add_roles_enabled = False
    await ctx.send("New member role assignment disabled.")
    print("New member role assignment disabled.")
#⊱----------------------------------------------------------⊰

#  ▩━━━━━◈ Add & Remove Roles To all members  ◈━━━━━▩
# Define a command to update roles for all members
@bot.command(name='updateroles', category='Update Members Roles', aliases=['updater'])
@commands.has_permissions(administrator=True) 
async def updateroles(ctx):
    # Get the roles IDs you want to add
    role_ids = [1080258166308221120]#add channel ids here  [1080258166308221120, 987654321]. Currently >> Release + Pack -Temp Role 

    # Loop through the role IDs and add the roles to the roles list
    roles = []
    for role_id in role_ids:
        role = ctx.guild.get_role(role_id)
        if role:
            roles.append(role)

    # Loop through all members and add the roles
    for member in ctx.guild.members:
        await member.add_roles(*roles)

    # Send a confirmation message
    await ctx.send("Roles updated for all members.")
    print("Roles updated for all members.")

# Remove roles from members
@bot.command(name='removeroles', category='Update Members Roles', aliases=['remover'])
@commands.has_permissions(administrator=True) 
async def removeroles(ctx):
    # Get the roles IDs you want to remove
    role_ids = [1080431801027276800]#remove channel ids here  [1080258166308221120, 987654321]. 

    # Loop through the role IDs and add the roles to the roles list
    roles = []
    for role_id in role_ids:
        role = ctx.guild.get_role(role_id)
        if role:
            roles.append(role)

    # Loop through all members and remove the roles
    for member in ctx.guild.members:
        await member.remove_roles(*roles)

    # Send a confirmation message
    await ctx.send("Roles removed for all members.")
    print("Roles removed for all members.")
#⊱─────────────────────────────────────────────────────⊰


#⊱───────────────{.⋅ ☆ Schedule Clear Messages ☆ ⋅.}───────────────⊰

channels_to_clear = []  # The list of channel IDs to clear
hours_between_clears = 24  # The default number of hours between clearings

# Define the scheduled clear task
@tasks.loop(hours=hours_between_clears)
async def scheduled_clear():
    for channel_id in channels_to_clear:
        channel = bot.get_channel(channel_id)
        messages = []
        async for message in channel.history(limit=None): #(limit=200) means delete 200 msg max
            if not message.pinned:
                messages.append(message)
        await channel.delete_messages(messages)

# Define the add and remove channel commands
@bot.command(name='add_channel', category='Schedule Clear', aliases=['ac'])
@commands.has_permissions(administrator=True) #commands that require administrative privileges
async def add_channel(ctx, channel_id: int):  #add your channels by id
    """add a channel to clear !ac 123456789 """
    channels_to_clear.append(channel_id)
    await ctx.send(f"Added channel <#{channel_id}> to the list of channels to clear.")

@bot.command(name='remove_channel', category='Schedule Clear', aliases=['rc'])
@commands.has_permissions(administrator=True)
async def remove_channel(ctx, channel_id: int): #remove channels by id
    """remove a channel to clear !rc 123456789 """
    if channel_id in channels_to_clear:
        channels_to_clear.remove(channel_id)
        await ctx.send(f"Removed channel <#{channel_id}> from the list of channels to clear.")
    else:
        await ctx.send(f"Channel <#{channel_id}> is not in the list of channels to clear.")

# Define the start and stop commands
@bot.command(category='Schedule Clear')
@commands.has_permissions(administrator=True)
async def start(ctx): #start the clearing command
    scheduled_clear.start()
    await ctx.send("Scheduled clear started.")

@bot.command(category='Schedule Clear')
@commands.has_permissions(administrator=True)
async def stop(ctx): #stop the clearing command
    scheduled_clear.stop()
    await ctx.send("Scheduled clear stopped.")

# Define the set_clear_frequency command
@bot.command(name='set_clear_frequency', category='Schedule Clear', aliases=['scf'])
@commands.has_permissions(administrator=True) 
async def set_clear_frequency(ctx, time_interval: str): #example :for hours `!set_clear_frequency 2h` OR for minutes `!set_clear_frequency 2m`
    """!scf 2m or 2h"""
    global hours_between_clears
    if time_interval.endswith("h"):
        hours = int(time_interval[:-1])
        hours_between_clears = hours
        scheduled_clear.change_interval(hours=hours)
        await ctx.send(f"Clear frequency set to {hours} hours.")
    elif time_interval.endswith("m"):
        minutes = int(time_interval[:-1])
        hours_between_clears = minutes / 60
        scheduled_clear.change_interval(minutes=minutes)
        await ctx.send(f"Clear frequency set to {minutes} minutes.")
    else:
        await ctx.send("Invalid time interval. Please specify a time interval in hours (h) or minutes (m).")

# Define the list_channels command
@bot.command(name='list_channels', category='Schedule Clear', aliases=['lc'])
@commands.has_permissions(administrator=True)
async def list_channels(ctx):
    """channels listed to clear """
    if not channels_to_clear:
        await ctx.send("😴 There are no channels currently listed for clearing.")
    else:
        channel_list = "\n".join(f"<#{str(c)}> " for c in channels_to_clear)
        await ctx.send(f"🧹 The channels currently listed for clearing are:\n\n{channel_list}")
#⊱──────────────────────────────────────────────────────────────────────────────────────────────────────⊰





# ► ► ► ≫ Run And Have Fun !
bot.run('Token Here')
