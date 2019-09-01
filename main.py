#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from random import randint

# Write your program here

points = 0

screenWidth = 178
screenHeight = 128

playerWidth = 50
playerHeight = 50
playerPositionX = int((screenWidth / 2) - (playerWidth / 2))
playerPositionY = screenHeight - playerHeight

enemyWidth = 30
enemyHeight = 30

enemy1PositionX = randint(0, screenWidth - enemyWidth)
enemy1PositionY = -30

enemy2PositionX = randint(0, screenWidth - enemyWidth)
enemy2PositionY = -120


brick.sound.beep()

gyro = GyroSensor(Port.S1)
touchR = TouchSensor(Port.S4)
time1 = StopWatch()
#motorL = Motor(Port.B)
#motorR = Motor(Port.C)


gyro.reset_angle(0)



def loadImage():
    brick.display.image("Player.png", (200, 200), clear = False)
    brick.display.image("Enemy.png", (200, 200), clear = False)
    brick.display.image('SpaceWars.png')
    brick.sound.file(SoundFile.T_REX_ROAR)
    wait(2000)



loadImage()

while True:
    brick.display.image("Player.png", (playerPositionX, playerPositionY), clear = False)
    brick.display.image("Enemy.png", (enemy1PositionX, enemy1PositionY), clear = False)
    brick.display.image("Enemy.png", (enemy2PositionX, enemy2PositionY), clear = False)
    brick.display.text(int(time1.time() / 1000), (150, 20))
    
    if (playerPositionX + playerWidth) >= screenWidth:
        playerPositionX = screenWidth - playerWidth
    
    elif playerPositionX <= 0: 
        playerPositionX = 0


    if enemy1PositionY > screenHeight:
        enemy1PositionY = -enemyHeight
        enemy1PositionX = randint(0, screenWidth - 60)

    if enemy2PositionY > screenHeight:
        enemy2PositionY = -enemyHeight
        enemy2PositionX = randint(0, screenWidth - 90)

    enemy1PositionY += 12
    enemy2PositionY += 12

    #if playerPositionX >= enemy1PositionX and playerPositionX <= (enemy1PositionX + enemyWidth) and playerPositionY >= enemy1PositionY and playerPositionY <= (enemy1PositionY + enemyHeight):
     #   break
    
   # if (playerPositionX + playerWidth) >= enemy1PositionX and (playerPositionX + playerWidth) <= (enemy1PositionX + enemyWidth) and playerPositionY >= enemy1PositionY and playerPositionY <= (enemy1PositionY + enemyHeight):
    #    break

    if touchR.pressed():
        break

   # motorL.run_angle(100, gyro.angle() * 100, Stop.COAST, False)
    #motorR.run_angle(100, -(gyro.angle() * 100), Stop.COAST, False)
    playerPositionX -= gyro.angle()
    wait(60)
    brick.display.clear()

brick.sound.file(SoundFile.GAME_OVER)
brick.display.image('GameOver.png')
wait(3000)