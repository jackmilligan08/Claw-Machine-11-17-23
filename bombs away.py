#LIBRARY 
#pygame is used for sound
#re is used for quit feature of game
#turtle is the main library that allows our game to operate
#random is used to randomize bomb spawns 

import turtle
from turtle import * 
import random
import pygame
import re
from pygame import mixer 

#NOTES
#Download all gif images and sounds from google drive folder (found on github)
#Make sure .py file is in a folder with all the items 
#Make sure caps lock is off
#Raise Volume for optimal experience 


#MUSIC 
#must use quit (q) key to stop music
#otherwise you have to close entire idle shell

#fuction plays background audio for the game, out of main loop 
def play_audio():
    global pause 
    if not pause:
        pygame.init()
        #loading in sound 
        backgroundsound="sound2.wav"
        pygame.mixer.music.load(backgroundsound)
        #-1 allows music to always play 
        pygame.mixer.music.play(-1)

    
#MOVEMENT FUNCTIONS
#function for both players movement and borders
def shipmovement():
    turtle.onkey(p1right, "d")
    turtle.onkey(p1left, "a")
    turtle.onkey(p2right, "Right")
    turtle.onkey(p2left, "Left")
    turtle.onkey(Quit, "q")
    turtle.onkey(pausegame, "space") 
    
    p1borders()
    p2borders()


#function occurs when "d" key is pressed
#changes shape of player 2 boat to right facing 
#takes in global pause for pause feature of game
def p1right():
    global pause 
    if not pause:
        p1xcor = player1.xcor()
        player1.setx(p1xcor+playerxVelright)
        player1.shape("penguin.gif")


#function occurs when "a" key  is pressed
#changes shape of player 2 boat to left facing 
#takes in global pause for pause feature of game
def p1left():
    global pause 
    if not pause:
        p1xcor = player1.xcor()
        player1.setx(p1xcor+playerxVelleft)
        player1.shape("penguin.gif")


#function occurs when right arrow keyis pressed
#changes shape of player 2 boat to right facing 
#takes in global pause for pause feature of game
def p2right():
    global pause 
    if not pause:
        p2xcor = player2.xcor()
        player2.setx(p2xcor+playerxVelright)
        player2.shape("penguin2.gif")


#function occurs when left key  is pressed
#changes shape of player 2 boat to left facing 
#takes in global pause for pause feature of game
def p2left():
    global pause
    if not pause:
        p2xcor = player2.xcor()
        player2.setx(p2xcor+playerxVelleft)
        player2.shape("penguin2.gif")


#function detects collison of player 1 with any of the edges(-440 or 440),
#and sends the boat to the opposite side  
def p1borders():
    p1xcor = player1.xcor()
    if p1xcor>RIGHT_EDGE:
        player1.setx(-1*p1xcor+25)
    if p1xcor<LEFT_EDGE:
        player1.setx(-1*p1xcor-25)


#function detects collison of player 2 with any of the edges(-440 or 440),
#and sends the boat to the opposite side  
def p2borders():
    p2xcor = player2.xcor()
    if p2xcor>RIGHT_EDGE:
        player2.setx(-1*p2xcor+25)
    if p2xcor<LEFT_EDGE:
        player2.setx(-1*p2xcor-25)
    return

#function detects if player 1 has been hit by a bomb
#plays the explosion sound effect and removes health from player 1
#moves the bomb that hit to a random position at the top of the screen
def p1collisions():
    global p1health
    
    bombposy=random.randint(275, 285)
    bombposx=random.randint(-475,475)
    
    for currbomb in range(0, numbombs):
        if abs(bomblist[currbomb].xcor() - player1.xcor())<45 and abs(bomblist[currbomb].ycor() - player1.ycor())<20:
            currbomby = bomblist[currbomb].ycor()
            bomblist[currbomb].sety(bombposy)
            bomblist[currbomb].setx(bombposx)
            bombsound = mixer.Sound("explosion2.wav") 
            bombsound.play()
                
            #CHANGE BOMB DAMAGE
            p1health -= 10

#function detects if player 2 has been hit by a bomb
#plays the explosion sound effect and removes health from player 2
#moves the bomb that hit to a random position at the top of the screen
def p2collisions():
    global p2health
    
    bombposy=random.randint(275, 285)
    bombposx=random.randint(-475,475)
    
    for currbomb in range(0, numbombs):
        if abs(bomblist[currbomb].xcor() - player2.xcor())<45 and abs(bomblist[currbomb].ycor() - player2.ycor())<20:

            currbomby = bomblist[currbomb].ycor()
            bomblist[currbomb].sety(bombposy)
            bomblist[currbomb].setx(bombposx)
            bombsound = mixer.Sound("explosion2.wav") 
            bombsound.play()
            
            #CHANGE BOMB DAMAGE 
            p2health -= 10


#BOMB FUNCTIONS


#function to call the other bomb functions
def callbombfunctions():
    createbombs()
    bombmovement()
    shipmovement()
    p1collisions()
    p2collisions()
    bombrespawning()

#detects if bombs have reached the bottom of the screen
#moves the bomb to a random position at the top of the screen
def bombrespawning():
    bombposy=random.randint(275, 310)
    bombposx=random.randint(-475,475)
    
    for currbomb in range(0, numbombs):
        currbomby = bomblist[currbomb].ycor()
        if currbomby < -200:
            bomblist[currbomb].sety(bombposy)
            bomblist[currbomb].setx(bombposx)

#creates the specified number of bombs (variable MAXBOMBS)
#spawns them in random positions at the top of the screen
#gives the bombs a 270 degree heading (down) and other needed qualities
def createbombs():
    global MAXBOMBS, numbombs, bomblist, neededbombs
    
    numbombs = len(bomblist)
    
    if numbombs >= MAXBOMBS:
        pass
    else:
        neededbombs = MAXBOMBS - numbombs
        for currbomb in range(0, neededbombs):
            bomblist.append(Turtle())
            bombposx=random.randint(-475,475)
            bombposy=random.randint(275, 300)

            bomblist[currbomb].hideturtle()
            bomblist[currbomb].penup()
            bomblist[currbomb].setx(bombposx)
            bomblist[currbomb].sety(bombposy)
            bomblist[currbomb].speed(0)
            bomblist[currbomb].shape('circle')
            bomblist[currbomb].shapesize(stretch_len=1.5,stretch_wid=1.5)
            bomblist[currbomb].color("light blue")
            bomblist[currbomb].showturtle()

            bomblist[currbomb].setheading(270)
        return

#allows the bombs to move, and gives each of them a random speed between 10-30
def bombmovement():
    for currbomb in range(0, numbombs):

        #CHANGE BOMB SPEED 
        bombspeed=random.randint(10, 30)
        bomblist[currbomb].forward(bombspeed)



#SCOREBOARD FUNCTIONS

#allows the players to choose their names prior to the game starting
def chooseplayernames():
    player_names()

#creates the player's names in the scoreboard if they do not make a custom one
#creates the space for the custom names
def writescoreboard():
    scoreboard.clear() 
    p1text = playernames[0]
    p2text = playernames[1]

    #variables 
    bothplayer = p1text + "   " + p2text
    noplayer = "P1" + "        "+  "P2"
    nop1 = "P1" + "      " + p2text 
    nop2 = p1text + "     " +  "P2"
    
    #both no name 
    if playernames[0] == "" and playernames[1] == "": 
        scoreboard.write(noplayer,  font=("Courier",45, "bold"), align = "center")
    #no player1 name 
    elif playernames[0] == "":
        scoreboard.write(nop1, font=("Courier",45, "bold"), align = "center")
         
    #no player 2 name    
    elif playernames[1] == "": 
        scoreboard.write(nop2,  font=("Courier",45, "bold"), align = "center")
    #both player names 
    else:
        scoreboard.write(bothplayer, font=("Courier",45, "bold"), align = "center")

#displays the current health of each player in the scoreboard
#calls the winning function when a player's health reaches 0
def healthscoreboard():
    global p1, p2
    scoreboard2.clear()
    healthprompt = "Health: " + str(p1health) + "           "  "Health: "  + str(p2health)
    scoreboard2.write(healthprompt, font=("Courier", 25, "bold"), align = "center")
    winning()

#inputs the custom names into the scoreboard
def player_names():
    p1name = screen.textinput("Player 1", "Player 1's name?")
    playernames.append(p1name)
    p2name = screen.textinput("Player 2", "Player 2's name")
    playernames.append(p2name) 

#creates the text that is displayed when the game is paused
def pause_hud():
    scoreboard3.clear()
    pauseprompt = "Game Paused"
    scoreboard3.write(pauseprompt ,font=("Courier", 50, "bold"), align = "center")
    
#called in health scoreboard
#calls winning feature of game
#if a player has 0 health the function will run

#creates the screen the is displayed when a player reaches 0 health,
#and the other player wins
def winning(): 
    global p1, p2, pause
    
    if p1health<= 0:
        pause = True
        screen.bgpic(picname="bg4.gif")
        
        #changing scoreboard to red 
        scoreboard3.clear()
        scoreboard3.color("dark blue")
        
        #hiding other playerers turtle 
        player2.hideturtle()
        player1.hideturtle()

        player1.shape("winpenguin.gif")
        player1.setx(-20)
        player1.sety(-80)
        player1.showturtle() 
        #clearing health scoreboard 
        scoreboard2.clear() 
        scoreboard2.goto(1000,1000)
        
        #hiding bombs on screen 
        for currbomb in range(0, numbombs):
           bomblist[currbomb].hideturtle()
        
        if playernames[0] == "" and playernames[1] == "":
            scoreboard3.write("Player 2 Wins!", font=("Courier", 75, "bold"), align = "center")
        else:
            scoreboard3.write(playernames[1] + " Wins ", font=("Courier", 75, "bold"), align = "center")

            
    if p2health<= 0:
        pause = True
        screen.bgpic(picname="bg4.gif")
        #changing scoreboard 
        scoreboard3.clear()
        scoreboard3.color("lightblue")
        
        #hiding other player 
        player1.hideturtle()
        player2.hideturtle()

        player1.shape("winpenguin2.gif")
        player2.setx(-20)
        player2.sety(-80)
        player2.showturtle() 
    
        #clearing health scoreboard 
        scoreboard2.clear() 
        scoreboard2.goto(1000,1000)

        #hiding bombs on screen 
        for currbomb in range(0, numbombs):
            bomblist[currbomb].hideturtle()
        

        if playernames[0] == "" and playernames[1] == "":  
            scoreboard3.write("Player 1 Wins!", font=("Courier", 75, "bold"), align = "center")
        else:
            scoreboard3.write(playernames[0] + " Wins ", font=("Courier", 75, "bold"), align = "center")
    



#PAUSE AND QUIT GAME

#called when space bar is pressed
#makes pausen True upon pressing
#displays the pause words and suspends gameplay until pressed again
def pausegame():
    global pause
    if (pause == True):
        scoreboard3.reset()
        scoreboard3.penup()
        scoreboard3.goto(0,-10) 
        scoreboard3.hideturtle()
        pause = False

    elif (pause == False):
        pause_hud() 
        pause = True  
        
    return 

#called when "q" key is pressed
#requests player to confirm Yes or No
#quits the game if Yes, or anything starting with "Y" is entered
#continues as usual if No or anything else not starting with "Y" is entered
def Quit():
    global running
    running = False
    gamequit = screen.textinput("Quit", "(Quit: Yes or No?)")
    if re.match("^[Y, y]", gamequit):
        pygame.mixer.music.stop() 
        turtle.bye()
        
    else:
        running = True


#lists
playernames = []
bomblist=[]


#Global
running = True

pause = False  
p1health = 10
p2health = 10

#CHANGE MAX BOMBS 
MAXBOMBS=12

#Constants
playerxVelright = 30
playerxVelleft = -30

RIGHT_EDGE=440
LEFT_EDGE=-440

#Screen Setup (Version1) 
screen=turtle.Screen()
screen.setup(850,515)
screen.title("Bombs Away")
screen.bgcolor("skyblue")
screen.tracer(0)  
screen.bgpic(picname="bg3.gif")


#Adding Turtles
#adding player1 (aircraft carrier) 
player1=Turtle()

player1.penup() 
turtle.addshape(name="penguin.gif", shape=None)
player1.shape("penguin.gif")
player1.setx(-200)
player1.sety(-158) 

#adding player2 (#helicopter carrier)
player2=Turtle()

player2.penup() 
turtle.addshape(name="penguin2.gif", shape=None)
player2.shape("penguin2.gif")
player2.setx(200)
player2.sety(-160) 


turtle.addshape(name="winpenguin2.gif", shape=None)
turtle.addshape(name="winpenguin.gif", shape=None) 

#Adding shapes 
turtle.addshape(name="player1right.gif", shape=None)
turtle.addshape(name="player1left.gif", shape=None)
turtle.addshape(name="player2right.gif", shape=None)
turtle.addshape(name="player2left.gif", shape=None)
turtle.addshape(name="nuke.gif", shape=None)


#creating scoreboard
scoreboard=turtle.Turtle()
scoreboard.penup()
scoreboard.goto(0,200) 
scoreboard.hideturtle()
scoreboard.color("Black")

#health scoreboard 
scoreboard2=turtle.Turtle()
scoreboard2.penup()
scoreboard2.goto(0,170) 
scoreboard2.hideturtle()
scoreboard2.color("Red")

#pause prompt 
scoreboard3=turtle.Turtle()
scoreboard3.penup()
scoreboard3.goto(0,-10) 
scoreboard3.hideturtle()
scoreboard3.color("Black") 


#audio for later
bombsound = "explosion.wav" 

#Functions not used in while true loop
chooseplayernames()
#out of main loop to prevent lag 
writescoreboard() 
play_audio()


#main loop
while running:
    screen.update()
    turtle.listen()
    if not (pause):
        healthscoreboard()
        callbombfunctions()
        shipmovement() 

