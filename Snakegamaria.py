# A Modified Unconventional Snake game with some more interesting features like a Score Meter; Another Competitor as Computer. 
# The player level meter decreases if Computer's level meter increases and vice versa
# Importing required Modules Pygame, random, time 
import pygame
import random
import time 
# Class in which the whole game operates
class SnakeGame:
    def __init__(self) :
        pygame.init()
        self.SCR_HEIGHT=650
        self.SCR_WIDTH=900
        self.SCREEN=pygame.display.set_mode((self.SCR_WIDTH,self.SCR_HEIGHT))
        self.X_VELOCITY=0
        self.Y_VELOCITY=0
        self.X=450
        self.Y=325
        self.FPS=60
        self.CLOCK=pygame.time.Clock()
        self.PLAYER_SPEED=5
        self.AI_SPEED=3
        self.SNAKE_HEAD=pygame.image.load('Snake Head.png')
        self.SNAKE_BODY=pygame.image.load('Snake Body.png')
        self.INITIAL=pygame.transform.flip(self.SNAKE_HEAD,False,False)
        self.FOOD_X=random.randrange(5,820)
        self.FOOD_Y=random.randrange(5,640)
        self.FROG=pygame.transform.scale(pygame.image.load('Frog.png'),(20,20))
        self.AI_SNAKE=pygame.image.load('AI_Snake Head.png')
        self.AI_SNAKE_BODY=pygame.image.load('AI_Snake Body.png')
        self.AI_X=50
        self.SNAKE_LENGTH=0
        self.SNAKE_CORDINATE=[]
        self.SCORE=0
        self.AI_LEVEL=0
        self.AI_Y=50
        self.AI_SNAKE_CORDINATE=[]
        self.AI_SNAKE_LENGTH=0
        self.PLAYER_LEVEL=0
        self.RUNNING_STATUS=True
        pygame.display.update()
    # Function carrying code which decides when to declare Snake Collided 
    def Snake_Die(self):
        # Checking if coordinates self.SNAKE_HEAD_CORDINATE(carrying current cordinate of head) are in the self.SNAKE_CORDINATE[:-1](list carrying coordinates of each circular unit of snake except the last(head) one)
            # If coordinates of head of snake matched with any of other coordintes present in the list it will consider that the head is collided with any of its body parts
            if self.SNAKE_HEAD_CORDINATE in self.SNAKE_CORDINATE[:-1]:
                print(self.SNAKE_CORDINATE[:-1].index(self.SNAKE_HEAD_CORDINATE))
                # Calling self.Notifier funtion to tell the player that he had collided 
                self.Notifier('FONT 4.ttf',50,(250,130,20),'Opps!!',300,250)
                self.Notifier('FONT 4.ttf',50,(150,100,255),'SO TOXIC!!',200,350)
                self.Notifier('FONT 2.ttf',30,(150,100,255),'The Snake has bitten its own body',200,450)
                pygame.display.update()
                # stopping the process to allow the player to read the message
                time.sleep(5)
                # Turning boolean value of self.RUNNING_STATUS into False to exit from the game loop
                self.RUNNING_STATUS=False
    #Function deciding when to declare winner or whom to declare.   
    def Winner(self):
        # 630 is the maximum height of the bar of level meter

        # Decision of declaring when to declare player as winner
        if self.PLAYER_LEVEL>=630:
            self.Notifier('FONT 4.ttf',60,(50,250,100),'Player',250,200)
            self.Notifier('FONT 4.ttf',100,(250,200,10),'WON!!',210,300)
            pygame.display.update()
            time.sleep(5)
            self.RUNNING_STATUS=False
        # Decision of declaring when to declare player as winner
        elif self.AI_LEVEL>=630:
            self.Notifier('FONT 4.ttf',30,(250,100,50),'Opponnent',280,100)
            self.Notifier('FONT 4.ttf',30,(250,200,10),'WON!!',350,150)
            self.Notifier('FONT 4.ttf',100,('red'),'LOOSE!!',140,300)
            self.Notifier('FONT 4.ttf',30,(50,250,100),'Player',320,250)
            pygame.display.update()
            time.sleep(5)
            # Turning boolean value of self.RUNNING_STATUS into False to exit from the game loop
            self.RUNNING_STATUS=False
    # Function randomly deciding where to blit the image of food
    # and also increasing and decreasing level meter simultaneously of player and computer depending who matched the coordinates of its head with the coordinates of food (who ate first)
    def Froggy(self):
        self.SCREEN.blit(self.FROG,(self.FOOD_X,self.FOOD_Y))
        # Condition if player ate the food first then blitting(showing) another image of food anywhere else and increasing player's level meter and decreasing computer's
        if self.FOOD_X-10<self.X<self.FOOD_X+10 and self.FOOD_Y-10<self.Y<self.FOOD_Y+10:
            self.FOOD_X=random.randrange(5,750)
            self.FOOD_Y=random.randrange(5,640)
            # Snake length determines what is the actual length of snake per unit circle 
            self.SNAKE_LENGTH+=1
            self.PLAYER_SPEED+=0.25
            self.SCORE+=1
            self.PLAYER_LEVEL+=30
            if self.AI_LEVEL>0:
                self.AI_LEVEL-=10
                self.AI_SPEED+=0.1
         # Condition if computer ate the food first then blitting(showing) another image of food anywhere else and increasing computer's level meter and decreasing player's
        elif self.FOOD_X-10<self.AI_X<self.FOOD_X+10 and self.FOOD_Y-10<self.AI_Y<self.FOOD_Y+10 :
            self.FOOD_X=random.randrange(5,890)
            self.FOOD_Y=random.randrange(5,640)
            self.AI_SNAKE_LENGTH+=1
            self.AI_LEVEL+=20
            if self.PLAYER_LEVEL>0:
                self.PLAYER_LEVEL-=10
    # Function Combining all Functions of this code to coordinate with each other 
    def Combinor(self):
        # Blitting screen of background
        self.BG=self.SCREEN.blit(pygame.transform.scale(pygame.image.load("B G.jpg"),(900,650)),(0,0))
        self.Player()
        self.Froggy()
        self.Score_Manager()
        self.AI_Snake()
        self.Score_Meter()
        self.Snake_Length()
        self.AI_Snake_Length()
        self.Winner()
        self.Notifier('FONT 4.ttf',10,'white','Use Arrow keys to control the Snake',450,20)
        pygame.display.update()
    #Function for managing level meter and score meter.  
    def Score_Meter(self):
        #  to blit level meter 
        self.SCREEN.blit(pygame.transform.scale(pygame.image.load('Level_Meter.png'),(50,670)),(850,-10))
        #  default position of both Snakes 
        self.SCREEN.blit(self.SNAKE_HEAD,(858,0))
        self.SCREEN.blit(self.AI_SNAKE,(878,0))
        # Level bar of level meter of player
        pygame.draw.rect(self.SCREEN,'green',(862,645-self.PLAYER_LEVEL,10,self.PLAYER_LEVEL))
        # Level bar of level meter of computer snake
        pygame.draw.rect(self.SCREEN,'red',(881,645-self.AI_LEVEL,10,self.AI_LEVEL))
        # Changing level bar colour into yellow depending upon who won
        if self.AI_LEVEL>=630:
            pygame.draw.rect(self.SCREEN,'yellow',(881,645-self.AI_LEVEL,10,self.AI_LEVEL))
        elif self.PLAYER_LEVEL>=630:
            pygame.draw.rect(self.SCREEN,'yellow',(862,645-self.PLAYER_LEVEL,10,self.PLAYER_LEVEL))
    # Function managing coordinates of PLAYER's snake and its length 
    def Snake_Length(self):
        self.SNAKE_HEAD_CORDINATE=[]
        self.SNAKE_HEAD_CORDINATE.append(self.X)
        self.SNAKE_HEAD_CORDINATE.append(self.Y)
        self.SNAKE_CORDINATE.append(self.SNAKE_HEAD_CORDINATE)
        # Condition to keep a check on length of lists with respect to length of snake, if number of elements in list is more than self.SNAKE_LENGTH than deleting the first element
        if len(self.SNAKE_CORDINATE)>self.SNAKE_LENGTH:
            del self.SNAKE_CORDINATE[0]
        # Calling self. Snake_Die() which is carrying the criteria to declare when the snake collapsed
        self.Snake_Die()
    # Function managing coordinates of PLAYER's snake and its length     
    def AI_Snake_Length(self):
        self.AI_SNAKE_HEAD_CORDINATE=[]
        self.AI_SNAKE_HEAD_CORDINATE.append(self.AI_X)
        self.AI_SNAKE_HEAD_CORDINATE.append(self.AI_Y)
        self.AI_SNAKE_CORDINATE.append(self.AI_SNAKE_HEAD_CORDINATE)
        # Condition to keep a check on length of lists with respect to length of snake, if number of elements in list is more than self.SNAKE_LENGTH than deleting the first element
        if len(self.AI_SNAKE_CORDINATE)>self.AI_SNAKE_LENGTH:
            del self.AI_SNAKE_CORDINATE[0]
    # Function just to blit the score
    def Score_Manager(self):
        self.Notifier('FONT3.TTF',30,'red','Score '+str(self.SCORE),200,10)
    # Function that controls COMPUTER SNAKE movement and coordinate it with its blitting 
    def AI_Snake(self):
        self.SCREEN.blit(self.AI_SNAKE,(self.AI_X,self.AI_Y))
        for x, y in self.AI_SNAKE_CORDINATE:
            self.SCREEN.blit(self.AI_SNAKE_BODY,(x,y))
            self.SCREEN.blit(self.AI_SNAKE,(self.AI_X,self.AI_Y))
        # Conditions that controls the COMPUTER SNAKE movement    
        if self.AI_X>self.FOOD_X:
            self.AI_X-=self.AI_SPEED
        if self.AI_X<self.FOOD_X:
            self.AI_X+=self.AI_SPEED
        if self.AI_Y>self.FOOD_Y:
            self.AI_Y-=self.AI_SPEED
        if self.AI_Y<self.FOOD_Y:
            self.AI_Y+=self.AI_SPEED
    # Function that controls PLAYER SNAKE movement and coordinate it with its blitting      
    def Player(self):
        for x, y in self.SNAKE_CORDINATE:
            self.SCREEN.blit(self.SNAKE_BODY,(x,y))
        self.SCREEN.blit(self.INITIAL,(self.X,self.Y))
        # Conditons that allow the player to go thorugh one end of the screen and appear from the oppostite end
        if self.X<0:
            self.X=850
        if self.X>850:
            self.X=0
        if self.Y>650:
            self.Y=0
        if self.Y<0:
            self.Y=650
    #Function Carrying the loop which carry on the game until the given criterias fulfilled  
    def Game_loop(self):
        while self.RUNNING_STATUS:
            for events in pygame.event.get():
                if events.type==pygame.QUIT or (events.type==pygame.KEYDOWN and events.key==pygame.K_ESCAPE ):
                    self.RUNNING_STATUS=False
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_UP or events.key==pygame.K_8:
                        self.Y_VELOCITY-=self.PLAYER_SPEED
                        self.X_VELOCITY=0
                        self.INITIAL=pygame.transform.rotate(self.SNAKE_HEAD,270)
                    if events.key==pygame.K_DOWN or events.key==pygame.K_2:
                        self.Y_VELOCITY+=self.PLAYER_SPEED
                        self.X_VELOCITY=0
                        self.INITIAL=pygame.transform.rotate(self.SNAKE_HEAD,90)
                    if events.key==pygame.K_LEFT or events.key==pygame.K_4:
                        self.X_VELOCITY-=self.PLAYER_SPEED
                        self.Y_VELOCITY=0
                        self.INITIAL=pygame.transform.flip(self.SNAKE_HEAD,False,False)
                    if events.key==pygame.K_RIGHT or events.key==pygame.K_6:
                        self.INITIAL=pygame.transform.flip(self.SNAKE_HEAD,True,False)
                        self.X_VELOCITY+=self.PLAYER_SPEED
                        self.Y_VELOCITY=0
            self.X=self.X+self.X_VELOCITY
            self.Y=self.Y+self.Y_VELOCITY
            self.CLOCK.tick(self.FPS)
            # Calling the comn=bining funtion to finally implement all the funtions in loop
            self.Combinor()
            pygame.display.update()
    # This function is for blitting texts on game screen
    def Notifier(self,font_type,fontsize,fontcolor,message,X_Text,Y_Text):
        font=pygame.font.Font(font_type,fontsize)
        render=font.render(message,True,fontcolor,)
        self.SCREEN.blit(render,(X_Text,Y_Text))
    
if __name__=='__main__':
    SnakeGame().Game_loop()
    