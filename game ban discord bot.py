from fileinput import filename
from glob import glob
from multiprocessing.connection import Client
import random
import os
from turtle import end_fill
import discord
import time
from discord.ext import commands

import discord
intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='SonOfABITCH')


@client.event
async def on_member_update(before, after):

        game_after = [i for i in after.activities if str(i.type) == "ActivityType.playing" and str(i.name) == "League Of Legends"]
        game_before = [i for i in before.activities if str(i.type) == "ActivityType.playing" and str(i.name) == "League Of Legends"]

        global start
        end = 0
        total = 0
        global max
        max = 1800
        if game_after:
                #print(game_after)
                start = time.perf_counter()
                print("==Start==")
                print (start)
                
        
        elif game_before and not game_after:
                end = time.perf_counter()
                total = end - start
                print("==END==")
                print(end)
                print("==Total==")
                print(total)

                
                
                if total >= max:
                        print (after)
                        await after.send("You made a mistake my friend")
                        await after.kick(reason="That's bannable behaviour")
                        
       
     
       
     

client.run("OAUTH TOKEN")