
from time import sleep, time
from pynput.keyboard import Key, Controller
import threading 
import win32api, win32con


keyboard = Controller()

#KEYBOARD MOVEMENTS
#WASD JUMP AND CROUCH
def pressLeft():
    keyboard.press('a')
    release= threading.Timer(0.232, releseLeft)
    release.start()

def releseLeft():
    keyboard.release('a')

def pressRight():
    keyboard.press('d')
    release= threading.Timer(0.232, releseRight)
    release.start()

def releseRight():
    keyboard.release('d')

def pressForward():
    keyboard.press('w')
    release= threading.Timer(0.232, releaseForward)
    release.start()

def releaseForward():
    keyboard.release('w')

def pressBack():
    keyboard.press('s')
    release= threading.Timer(0.232, releaseBack)
    release.start()

def releaseBack():
    keyboard.release('s')

def pressJump():
    keyboard.press(Key.space)
    release= threading.Timer(0.2, releaseJump)
    release.start()

originalTurnAmount = 600
turnAmount = originalTurnAmount

def turnRight():
    global turnAmount
    if turnAmount > 0:
        #print(turnAmount)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,  1 * 1, 0, 0, 0)
        turnAmount -= 1
        callAgain = threading.Timer(0.0000001, turnRight)
        callAgain.start()
    

    else:
        turnAmount = originalTurnAmount

def addTurn(direction):
    global turnAmount
    if turnAmount > 0:
        #print(turnAmount)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, direction * 12, 0, 0, 0)
        turnAmount -= 12
        #callAgain = threading.Timer(0.1, addTurn(direction))
        #callAgain.start()
        sleep(0.0000000000000000000000000000000000000000000000000001)
        addTurn(1)

    else:
        turnAmount = originalTurnAmount


def releaseJump():
    keyboard.release(Key.space)

def pressCrouch():
    keyboard.press(Key.shift)

def releaseCrouch():
    keyboard.release(Key.shift)

#MOUSE MOVEMENT
def turn():
    addTurn(1)
   
def reverseTurn():
    addTurn(-1)

import speech_recognition as sr
def listenToMic():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('say something')
        


        try:
        
            audio = r.listen(source, phrase_time_limit=1)
            voiceData = r.recognize_google(audio)
            respond(voiceData)
     

        except sr.UnknownValueError:
            print('error i did not get that')
        except sr.RequestError:
            print('sorry speech service down')
        except sr.WaitTimeoutError:
            print('error')


def respond(data):
    split = data.split(' ')
    print(data)

    for word in split:
    
        match word[0]:
            case 'l':
                pressLeft()
            
            case 'r':
                pressRight()

            case 'f':
                pressForward()

            case 'b':
                pressBack()

            case 'j':
                pressJump()

            case 'd':
                pressCrouch()

            case 's':
                releaseCrouch()

            case 't':
                addTurn(1)
            
            case 's':
                print("swivel")
                addTurn(-1)
        
        print(word)



import socket
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'NICKNAME'
token = 'oauth'
channel = '#CHANNEL'

def twitch():
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
            response = resp.split(' :')[1]
            respond(response)
            #print(response[1])
            
twitch()
