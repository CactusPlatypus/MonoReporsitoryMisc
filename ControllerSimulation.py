import time
import vgamepad as vg
import pyautogui
import keyboard
import socket

gamepad = vg.VX360Gamepad()

#done
def Jump():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button

   gamepad.update()  # send the updated state to the computer
    # (...) A and left hat are pressed...
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button

   gamepad.update()  # send the updated state to the computer
    # (...) left hat is still pressed...

#done
def RB():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)  

   gamepad.update() 

#done
def LB():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)  

   gamepad.update() 

#done
def X():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  

   gamepad.update() 

#done
def Y():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)  

   gamepad.update() 

def B():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)  

   gamepad.update() 


#done
def LT():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)  

   gamepad.update() 

#done
def RT():
   gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB) 

   gamepad.update()  
   time.sleep(0.5)

   gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)  

   gamepad.update() 

#done
def lookLeft():
    gamepad.right_joystick_float(-0.7,0)
    gamepad.update()
    time.sleep(0.5)
    gamepad.right_joystick_float(0,0)

#done
def lookRight():
    gamepad.right_joystick_float(0.7,0)
    gamepad.update()
    time.sleep(0.5)
    gamepad.right_joystick_float(0,0)

#done
def lookUp():
    gamepad.right_joystick_float(0.0,0.7)
    gamepad.update()
    time.sleep(0.5)
    gamepad.right_joystick_float(0,0)

#done
def lookDown():
    gamepad.right_joystick_float(0.0,-0.7)
    gamepad.update()
    time.sleep(0.5)
    gamepad.right_joystick_float(0,0)

#done
def moveForward():
    gamepad.left_joystick_float(0.0,0.7)
    gamepad.update()
    time.sleep(0.5)

#done
def strafeLeft():
    gamepad.left_joystick_float(-0.7,0.0)
    gamepad.update()
    time.sleep(0.5)

#done
def strafeRight():
    gamepad.left_joystick_float(0.7,0.0)
    gamepad.update()
    time.sleep(0.5)

#done
def moveBack():
    gamepad.left_joystick_float(0.0,-0.7)
    gamepad.update()
    time.sleep(0.5)

#done
def stopMoving():
    gamepad.left_joystick_float(0,0)

#done
def sprint():
    moveForward()
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB) 
    gamepad.update()  

#done
def stopSprint():
    stopMoving()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB) 
    gamepad.update()  

#done
def leftTriggerIn():
    gamepad.left_trigger(255)
    gamepad.update()
    time.sleep(0.5)

#done
def leftTriggerOut():
    gamepad.left_trigger(0)
    gamepad.update()
    time.sleep(0.5)

#done
def rightTriggerIn():
    gamepad.right_trigger(255)
    gamepad.update()
    time.sleep(0.5)

#done
def rightTriggerOut():
    gamepad.right_trigger(0)
    gamepad.update()
    time.sleep(0.5)

#while True:
   # if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        #print('You Pressed A Key!')
     # finishing the loop

sock = socket.socket()

enabled = True

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'NICKNAME'
token = 'OAUTH TOKEN'
channel = '#CHANNEL'

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        exit()
    
    if keyboard.is_pressed('p'): 
        enabled = not enabled
        print(enabled)

    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    

    if len(resp) > 0:
        print(resp )
        if ("walk" in resp):
            moveForward()
        
        if ("stopWalk" in resp):
            stopMoving()

        if ("strafeLeft" in resp):
            strafeLeft()
        
        if ("strafeRight" in resp):
            strafeRight()

        if ("backwards" in resp):
            moveBack()

        if ("sprint" in resp):
            sprint()

        if ("stopSprint" in resp):
            stopSprint()

        if ("jump" in resp):
            Jump()
        
        if ("lookLeft" in resp):
            print("Look Left")
            lookLeft()
        
        if ("lookRight" in resp):
            print("Look Right")
            lookRight()

        if ("lookUp" in resp):
            print("Look Up")
            lookUp()

        if ("lookDown" in resp):
            print("Look Down")
            lookDown()

        if ("fire" in resp):
            print("fire")
            rightTriggerIn()

        if ("stopFire" in resp):
            print("stop fire")
            rightTriggerOut()   
        
        if ("leftTrigger" in resp):
            print("leftTrigger")
            leftTriggerIn()   
        
        if ("leftTriggerOut" in resp):
            print("leftTriggerOut")
            leftTriggerOut()

        if ("LB" in resp):
            print("leftBumper")
            LB()

        if ("RB" in resp):
            print("RB")
            RB()

        if ("X" in resp):
            print("X")
            X()
        
        if ("Y" in resp):
            print("Y")
            Y()

        if ("B" in resp):
           print("B")
           B()

        if ("LeftStick" in resp):
            print("LT")
            LT()

        if ("RightStick" in resp):
            print("RT")
            RT()
        
        if ("resetMate" in resp):
            gamepad.reset()
            gamepad.update()

    #gamepad.left_joystick_float(-0.5, 0.0)

    #gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    gamepad.update()  # send the updated state to the computer