import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode ((1280, 720))
pygame.display.set_caption("Pong")
screenwidth = 1280
screenheight = 720

level = 1
a = 200
x = 100
y = 150
x2 = 1180.1
y2 = 150.1
width = 10
height = 150
speed = 5
start = 0
ballxspeed = 12
ballyspeed = 6
run = True
ballx = 1000
bally = randint(50, screenheight-60)
playerscore = 0
cpuscore = 0

import os       #makes game work on any pc by not requiring the whole path to be entered to load image and fonts
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)





font = pygame.font.Font('Pixeled.ttf', 100)
scorefont = pygame.font.Font('Pixeled.ttf', 10)
spacefont =pygame.font.Font('Pixeled.ttf', 40)

s = 2
t = 0

logo = pygame.image.load('logo.png')


logox = 10
logoy = 100
logoxspeed = 5
logoyspeed = 5
brea = 0 
highestlevel = 1
    


while run:
    pygame.time.delay(10) #fps esseintally
    #quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    if keys [pygame.K_F11]:
        DISPLAYSURF = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

    if keys [pygame.K_ESCAPE]:
         DISPLAYSURF = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)


#player controlled paddle
    if keys [pygame.K_DOWN] and y < screenheight - height:
        y += speed
    if keys [pygame.K_UP] and y > 0:
        y -= speed
    
    paddle1 = pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
#start game

    
        #starting animation
    while start == 0:
        pygame.time.delay(10)
        
        for event in pygame.event.get():    #makes quitting possible within this loop
            if event.type == pygame.QUIT:
                run = False
                brea = 1 #breaks it properly to quit
                break
                
        if brea == 1:
            break
        
        eys = pygame.key.get_pressed()

        if eys [pygame.K_SPACE]:        #checks for space press to start game
            start = 1
            s = 0
            t = 1
            a = 0

        if eys [pygame.K_F11]:
            DISPLAYSURF = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        if eys [pygame.K_ESCAPE]:
            DISPLAYSURF = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        
    
        screen.blit(logo, (logox, logoy))
        

        if (logox + 795 >= screenwidth) or (logox <= -50):
            logoxspeed = -logoxspeed
        
        if (logoy + 550 >= screenheight) or (logoy <= -50):
            logoyspeed = -logoyspeed
        
        logox += logoxspeed
        logoy += logoyspeed
        
        
        spacetostart = spacefont.render("Press Space To Start", True, (255, 255, 255))
        screen.blit(spacetostart, (logox + 50, logoy + 450))
        
        pygame.display.update()
        screen.fill((0, 0, 0))
        
        

    if start == 1:
    #ball code
        if s == 1:   #s does stuff that makes the ball slow for the first serve - this is how original pong did it, and makes the game much better
            if ballxspeed == -4:
                ballxspeed = -12
            elif ballyspeed == -2:
                ballyspeed = -6
            elif ballxspeed == 4:
                ballxspeed = 12
            elif ballyspeed == 2:
                ballyspeed = 6
            
        if s == 0:
            if t == 2:
                ballxspeed = 4
                ballyspeed = 2
            if t == 1:
                ballxspeed = -4
                ballyspeed = -2
            t = 3


        if (ballx + 25 >= screenwidth) or (ballx <= 0):
            ballxspeed = -ballxspeed
       
        if (bally + 25 >= screenheight) or (bally <= 0):
            ballyspeed = -ballyspeed


        if ballx in range (x - 5, x + 10) and bally in range (y, y + 150):
            ballxspeed = -ballxspeed
            s += 1
        if ballx in range (int(x2) - 5, int(x2) + 10) and bally in range (int(y2), int(y2) + 150):
            ballxspeed = -ballxspeed
            s += 1
        
        

        if a  > 199:  # a is a little integer to keep the ball stationary for a few seconds at the beginning of a new set (after a point is scored)
            ballx += ballxspeed   #makes ball move
            bally += ballyspeed

        a += 1
            # new serve function for after someone scores a point
        def newset(e):
            
            global ballx
            global bally
            global a
            global s
            ballx = e
            bally = randint(50, screenheight-60)
            a = 0
            s = 0

        if ballx <= 25:
            cpuscore += 1
            newset(1000)
            t = 1
        
        if ballx >= 1255:
            playerscore += 1
            newset(280)
            t = 2
            
        ball = pygame.draw.circle(screen, (255, 255, 255), [ballx, bally], 10, 0)
        
        bally2 = bally - 75
        
        def cpulevel(speeed): #cpu ai
            global y2
            global bally2

            sped = (speeed / 2) + 0.75    
            if y2 > bally2 and y2 > 0:  
                y2 -= sped
                
            elif y2 < bally2 and y2 < screenheight - height: 
                y2 += sped
            paddle2 = pygame.draw.rect(screen, (255, 255, 255), (x2, y2, width, height))
        
        level = playerscore - cpuscore + 1  #sets level based off of difference in score
        if level < 1:
            level = 1
        if level > highestlevel:
            highestlevel = level

        cpulevel(level) #bases cpu difficult of level



      
            

        
    #renders scores and the level
    text = font.render(str(playerscore), True, (255, 255, 255))
    screen.blit(text, (450, -75))
    text2 = font.render(str(cpuscore), True, (255, 255, 255))
    screen.blit(text2, (740, -75))
    text3 = scorefont.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(text3, (5, -5))
    text4 = scorefont.render("Highest Level Reached: " + str(highestlevel), True, (255, 255, 255))
    screen.blit(text4, (1050, -5))

        

    pygame.display.update()

    

pygame.quit


