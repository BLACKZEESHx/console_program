import discord
import colorama
from colorama import Fore
import os
import re
import json
import time
import asyncio
from time import sleep
from discord.ext.commands.core import command
from discord import Permissions, Intents, File
import random
import datetime
from discord.ext import commands
from discord import Embed
from discord.ext import tasks
from discord.utils import get

intents = Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True


def exception_handler(loop,context):
   print("Caught the following exception")
   print(context['message'])

print(f"{Fore.LIGHTRED_EX}Loading...{Fore.RESET}")
time.sleep(0.1)
os.system("cls")
activity = discord.Game(name="sam.#9999")


class MyBot(commands.Bot):
    async def setup_hook(self):
        detectmultiplier.start()

bot = MyBot(command_prefix=".", intents=intents, help_command=None, activity=activity, status=discord.Status.dnd)

bot.remove_command('help')

@bot.event
async def on_connect():
    os.system(f"title [multiplier Notifier] - Connected: {bot.user}")
    os.system('cls')
    print("connected")

@bot.event 
async def on_command_error(ctx, error): 
    await ctx.message.delete()
    if isinstance(error, commands.CommandNotFound): 
        #em = discord.Embed(title=f"Error", description=f"Crash command not found.", color=ctx.author.color) 
        print(Fore.RED + "[CMD] | " + Fore.WHITE + "Command not found")
        #await channel.send(embed=em, delete_after=int(deleteafter))


detecttime = 1

@tasks.loop(minutes=detecttime)
async def detectmultiplier():
    channel = bot.get_channel(1074474168290115665)
    await asyncio.sleep(1680)
    await channel.send("> Ping: <@&1074482713937068165> ", delete_after=130)
    embed3 = discord.Embed(color=0xE5AD4E, title=f"multiplier Detected", description=f"""
    **MULTIPLIER**
    
    A event is happening in 2 minutes! - This will be the only notification for this multiplier.
    
    *Log on to the game to claim*""")
    embed3.set_footer(text = "sam.#9999")
    await channel.send(embed=embed3, delete_after=130)
    print(Fore.LIGHTRED_EX + "[CMD] | " + Fore.WHITE + "multiplier Detected Sent")
    await asyncio.sleep(120)

@detectmultiplier.before_loop
async def before():
    await bot.wait_until_ready()

bot.run('not sharing')
exit()
import random
from time import sleep as wt
import pyfiglet
from pynput.keyboard import Controller



def write_like_gpt(text,waite=0.1):
    for echar in text:
        print(echar,end="",flush=True)
        wt(waite)
    print()

def write_in_underline(text,waite=0.1):
    for echar in text:
        print(echar,end="_",flush=True)
        wt(waite)
    print()

def write_in_mono(text,waite=0.1):
    for echar in text:
        print(echar,end=" ",flush=True)
        wt(waite)
    print()

def write_in_ascii(text:str)->str:
    # Use pyfiglet to convert the text to ASCII art
    ascii_art = pyfiglet.figlet_format(text)
    # typing the ASCII art to the console
    write_like_gpt(ascii_art)


def write_in_3d_underline(text,waite=0.1):
    for echar in text:
        print(echar,end="__",flush=True)
        wt(waite)
    print()


def overwrite_typing(text):
    for i in range(len(text)):
        print(text[:i+1], end='\r', flush=True)
        wt(0.1) # adjust the delay as needed
    print()

# example usage
overwrite_typing("Hello, world!")
wt(1) # add a pause before modifying the text
overwrite_typing("My Name is Abdullah")
wt(5) # add a pause before modifying the text

def real_time_typeing(text):
    # wt(5)
    key = Controller()
    for tychar in text:
        key.type(tychar)
        wt(0.1)

real_time_typeing("may people here a course very again they present group hold problem well may also most want such when but point well need face if all house down off hold program think own person he between eye without present face back you find through nation")

def write_in_blind_line(text):
    for i in range(len(text)):
        if i % 2 == 0:
            print(text[:i], end='', flush=True)
        else:
            print(text[:i] + '\u2588'*(len(text)-i), end='', flush=True)
        wt(0.05) # adjust the delay as needed
        print('\r', end='') # move the cursor back to the beginning of the line
    print(text) # print the final text after the animation is done


def write_in_random(text):
    for i in range(len(text)):
        # Choose a random animation effect
        animation = random.choice(['normal', 'reverse', 'fill'])
        if animation == 'normal':
            print(text[:i+1], end='', flush=True)
        elif animation == 'reverse':
            print(text[::-1][:i+1][::-1], end='', flush=True)
        elif animation == 'fill':
            print(text[:i] + '\u2588'*(len(text)-i), end='', flush=True)
        wt(0.05) # adjust the delay as needed
        print('\r', end='') # move the cursor back to the beginning of the line
    print(text) # print the final text after the animation is done