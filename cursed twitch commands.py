
import win32gui
import win32con
import socket
import os
import keyboard
from pynput.mouse import Controller
import random
import scipy.interpolate
import pyautogui
import time


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'NICKNAME'
token = 'oauth'
channel = '#CHANNEL'

def lerp(a, b,  c):
    return (c * a) + ((1-c) * b)

def screenOff():
    win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def pcOFF():
    print("bye")
    os.system("shutdown /s /t 1")

def closeGame():
    try:
        #os.system('TASKKILL /F /IM overwatch.exe')
        keyboard.press("alt")
        keyboard.press_and_release("F4")
        keyboard.release("alt")
    

    except Exception:
        print("Overwacth not open")

def randomMouse():
    mouse = Controller()
    xStart, yStart = mouse.position
    xGoal = random.randrange(-1280, 1280)
    yGoal = random.randrange(-800, 800)

    x = xStart
    y = yStart

    #while x != xGoal:
        #x = lerp(x, xGoal, 0.5)
        #y = lerp(y, yGoal, 0.5)
        #print(str(x)+ " " + str(y))
        #mouse.move(xGoal,yGoal)

    #mouse.moveTo()
    pyautogui.moveRel(xGoal, yGoal, 6)
    #mouse.move(xGoal,yGoal, False, 5.0)
    scroll = random.randrange(-200, 200)
    mouse.scroll(0, scroll)

def flipMonitor():
    keyboard.press("ctrl")
    keyboard.press("alt")
    keyboard.press_and_release("down arrow")
    keyboard.release("ctrl")
    keyboard.release("alt")

sock = socket.socket()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        print(resp)
        if ("!off" in resp):
            screenOff()
            resp = ""
        
        if ("!altF4" in resp):
            closeGame()

        if ("!powerOffLOL" in resp):
            pcOFF()
        
        if ("!butter" in resp):
            randomMouse()

        if ("!flip" in resp):
            print("lol")
            flipMonitor()

#sock.close()



   