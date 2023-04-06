from fileinput import filename
from glob import glob
import random
import os
from sqlite3 import Time
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from threading import Timer
#from time import sleep
from mutagen.mp3 import MP3


bot = commands.Bot(command_prefix='!')
client = discord.Client()

#channel_id = 982140107664523288
#voice_channel = client.get_channel(channel_id)
#await voice_channel.connect()

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    #channel = client.get_channel('982140107664523288')
    #channel_id = "982140107664523288"
    #voice_channel = client.get_channel(channel_id)
    #await voice_channel.connect()

def loadRadio(vc):
    print("Radio starting")

    playSong(vc)



FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
   
songsTillAdd = 3


def playSong(vc):

    global songsTillAdd
    songsTillAdd -= 1
    print(songsTillAdd)

    if (songsTillAdd > 0):
        songFile = random.choice(os.listdir("./songs"))
        source =  "./songs/"+ songFile
        time = MP3("songs/" + songFile).info.length
    else:
        print("Playing Ad")
        songFile = random.choice(os.listdir("./ads"))
        source =  "./ads/"+ songFile
        time = MP3("ads/" + songFile).info.length
        songsTillAdd = 6



    player = vc.play(FFmpegPCMAudio(source), after=lambda e: print('done', e))

    print(songFile)

    nextSong = Timer(time +0.1, playSong, args=[vc])
    nextSong.start()
 

    
    


def selectSong():
    file = "./songs/"+ random.choice(os.listdir("./songs"))
    return file

@bot.command(name ="start")
async def start(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    vc = await channel.connect()
    loadRadio(vc)

    


bot.run("OAUTH TOKEN")