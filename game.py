import pygame ,sys
from pygame.locals import *
pygame.init()  
clock =pygame.time.Clock()
score =0
jump = False
speed= 10 
black = ( 200,200,200)
screenwidth =720
screenheight =800
screen =pygame.display.set_mode((screenwidth,screenheight))
fires =[]
toleft=True
toright=False
forward = False
miss=pygame.mixer.Sound("music/missedkik.wav")
painvoice =pygame.mixer.Sound("music/pain.wav")
def dark():
 screen.fill(black)
################# fire ############
class fire :
  def __init__(self, x ,y ,radius ,color ,direction,step ):
    self.x =x 
    self.y =y
    self.radius =radius
    self.color =color
    self.direction =direction
    self.step = step * direction
  def draw(self ,screen):
    pygame.draw.circle(screen ,self.color ,(self.x ,self.y) ,self.radius)
      
class player():
  def __init__(self, x, y, width, height):
    self.x =x
    self.y =y
    self.height = height
    self.width =width
    self.step =20
    self.left =False
    self.right =False
    self.kick = False
    self.kick_right = False
    self.push =False
    self.push_right = False
    self.moves =0
    self.speed =5
    self.isJump =False
    self.stand =False    
man = player( 500,400, 130,200)    
####################### enemy #######################
class enemy :
  def __init__(self, x, y, width ,height ,end ):
    self.x =x
    self.y =y
    self.height = height
    self.width =width
    self.start =x
    self.end = end
    self.step =4
    self.moves =0
    self.frame = (self.x  ,self.y ,self.width ,self.height )
    self.health = (self.x  ,self.y-20 ,self.width +10,self.height -180 )
    man.health = (man.x  ,man.y-20 ,man.width +10,man.height -180 )
    self.scale = man.x -self.x
  def draw(self ,screen ):
    self.move()
    if forward:
      if self.x - self.step < self.start:
        self.step *= -1
      else : self.x += self.step 
    if self.step < 0 :
     screen.blit(walk[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 10:
       self.moves = 0
    elif round(self.x +self.step )>round(man.x ) -round(self.width -10 ) :
     
     screen.blit(attack[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 7:
       self.moves = 0
    elif self.x - self.step >= round(man.x )  :
     screen.blit(attack[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 7:
       self.moves = 0
       
    elif self.x - self.step < round(man.x ) and forward :####
     screen.blit(attack[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 7:
       self.moves = 0
    else :
     screen.blit(walk_right[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 5:
       self.moves = 0
    self.frame = (self.x ,self.y ,self.width ,self.height)
    self.health = (self.x-30  ,self.y-40 ,self.width -10,self.height -180 )
    
    pygame.draw.rect(screen ,(0,23,89),self.health,2)  
    pygame.draw.rect(screen ,(0,23,89),man.health,2)   
  def move(self):
    if self.step > 0:
      forward= False
      if round(self.x +self.step )>=round(man.x ) -round(self.width -10 )  :
           self.step = .1
           #miss.play()
           if round(self.x +self.step )<=round(man.x ) -round(self.width -10 )  :self.step =10 ####
           
      else : self.step =3 
      if self.x +self.step >self.end :
        self.step =5
        self.step *= -1
      else : self.x += self.step
    else :
      if self.x - self.step < self.start:
        self.step *= -1
      else : self.x += self.step 
evil_show =False  
#bgin =pygame.mixer.music.load("music/é.mp3")
#pygame.mixer.Sound("music/e.wav")
#pygame.mixer.play()
miss=pygame.mixer.Sound("music/missedkik.wav")
painvoice =pygame.mixer.Sound("music/pain.wav")  
#walkvoice =pygame.mixer.Sound("")
winvoice =pygame.mixer.Sound("music/try.wav")    
man.frame = (man.x ,man.y ,man.width ,man.height)
evil = enemy(1 ,400 ,130,200 ,500) 
king_right=pygame.image.load("photo/pl1.png")
king=pygame.image.load("photo/p1.png")
bg = pygame.image.load("photo/background.jpg")
kick=[pygame.image.load("photo/k1.png"),pygame.image.load("photo/k2.png"),pygame.image.load("photo/k3.png")]
push=[pygame.image.load("photo/p1.png"),pygame.image.load("photo/p2.png"),pygame.image.load("photo/p3.png"),pygame.image.load("photo/p4.png")]
kick_right=[pygame.image.load("photo/kl1.png"),pygame.image.load("photo/kl2.png"),pygame.image.load("photo/kl3.png")]
push_right=[pygame.image.load("photo/pl1.png"),pygame.image.load("photo/pl2.png"),pygame.image.load("photo/pl3.png"),pygame.image.load("photo/pl4.png")]
walk=[pygame.image.load("photo/r1.png"),pygame.image.load("photo/r4.png"),pygame.image.load("photo/r2.png"),pygame.image.load("photo/r3.png"),pygame.image.load("photo/r5.png"),pygame.image.load("photo/r1.png"),pygame.image.load("photo/r4.png"),pygame.image.load("photo/r2.png"),pygame.image.load("photo/r3.png"),pygame.image.load("photo/r5.png")]
walk_right=[pygame.image.load("photo/l1.png"),pygame.image.load("photo/l3.png"),pygame.image.load("photo/l2.png"),pygame.image.load("photo/l3.png"),pygame.image.load("photo/l5.png")]
attack=[pygame.image.load("photo/pl1.png"),pygame.image.load("photo/pl2.png"),pygame.image.load("photo/pl3.png"),pygame.image.load("photo/pl4.png"),pygame.image.load("photo/kl1.png"),pygame.image.load("photo/kl2.png"),pygame.image.load("photo/kl3.png")]
ball= fire(550,20,90,black,1,0 )
ball1= fire(3,20,90,black,1,0 ) 
while True :
   clock.tick(10)
   screen.blit(bg,(0,0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m :
          if len(fires) <= 5 :
            direction = 0
          if toleft :
            direction = -1
          else : direction = 1
          fuck =fire(round(man.x + man.width //4) ,round(man.y + man.height //4),1,(200,40,10),direction,20)
          fires.append(fuck)
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_n : 
         screen.blit(push[man.moves],(man.x,man.y))
         man.moves += 1
         if man.moves == 3:
           man.moves = 0
           ##########        
   man.speed = 5
   man.isJump = False
   
   
   ###controll
   keys =pygame.key.get_pressed()
   if keys[pygame.K_t] and screenwidth - 100 >= ball.x -ball.step >= 0:
     ball.x += ball.step *2
      
   if keys[pygame.K_LEFT] and man.x -man.step >= 0:
     #man.x -= man.step
     man.left = False
     man.right = False 
     man.push = False
     man.push_right = False
     man.kick = False
     man.kick_right = False   
   elif keys[pygame.K_RIGHT] and man.x + man.step + man.width -screenwidth   <=0 :
     man.x += man.step
   else : 
     man.left = False
     man.right = False
     
   if keys[pygame.K_a] :
     man.push = True
     man.push_right = False
     man.kick = False
     man.kick_right = False
     man.left =False
     man.right =False
     miss.play() 
     if man.x - evil.frame[0]-evil.width< 5 :
      score += 1 
      painvoice.play() 
   elif keys[pygame.K_k] :
     man.push = False 
     man.push_right = True
     man.kick = False
     man.kick_right = False
     man.left =False
     man.right =False
     miss.play()
     #for kick
   elif keys[pygame.K_s] :
     man.kick = True
     man.kick_right = False
     man.left =False
     man.right =False
     man.push = False
     man.push_right = False
     miss.play()
     if man.x - evil.frame[0]-evil.width< 5 :score += 1.5
   elif keys[pygame.K_l] :
     man.kick = False 
     man.kick_right = True
     man.left =False
     man.right =False
     man.push = False
     man.push_right = False
     score += 1
     evil_show =False
     miss.play()
   else :
     man.kick = False
     man.kick_right = False
     man.push = False
     man.push_right = False
   
   
   # key for fire and conditions of movement ################################################
   for fire in fires :
     if fire.x + fire.step <man.frame[0] - 50   : fires.remove(fire) 
     if fire.x > evil.frame[0] and fire.x < evil.frame[0] +evil.frame[2]:
       if fire.y > evil.frame[1] and fire.x < evil.frame[1] +evil.frame[3]:
         fires.remove(fire) 
         print("fire")
         score += 1 
     if fire.x < screenwidth and fire.x > 0:
       fire.x += fire.step
     else :
       fires.remove(fire)
   
   if keys[pygame.K_f] :
     if len(fires) <= 10 :
       direction = 0
       if toleft :
         direction = -1
       else : direction = 1
       fires.append(fire(round(man.x + man.width //4) ,round(man.y + man.height //4),8,(200,40,10),direction,20)) 
   # for show  fire on screen  ==🤣️ for fire in fires :fire.draw(screen)
   ################################################################################ 
     
   if keys[pygame.K_DOWN] and man.y + man.step + man.height - screenheight <=0 : man.y += man.step
   if keys[pygame.K_UP] and man.y - man.step >=0 : man.y -= man.step
   
   if jump :
    if speed >= -10:
     neg = 1
     if speed<0 :
       neg = -1
     man.y -=(man.step ** 2)*.1 * neg
     speed-=1
    else : 
         speed =10
         jump=False
          
   if keys[pygame.K_SPACE]:
     if toleft and man.x-man.step >=evil.frame[0]+evil.width :
      direc = -1
      man.left = True
      if man.x -man.step >= 0: man.x += man.step  *direc
      if toleft and round(man.x +man.step )<=round(evil.x ) +round(evil.width )+30  :
        pass#man.step =0.1  ##
      else: step =5
     else :# 
      direc= 1
      man.rigt = True
      #if man.x -man.step >= 0: man.x += man.step  *direc
      if man.x + man.step + man.width -screenwidth   <=0 : man.x += man.step  *direc
   
   if keys[pygame.K_v]:
      jump = True   
   if keys[pygame.K_RIGHT]:
      toright=True
      toleft =False
   elif keys[pygame.K_LEFT]:
      toleft =True
      toright= False
   if man.left :
     screen.blit(walk[man.moves],(man.x,man.y))
     man.moves += 1
     if man.moves == 10:
       man.moves = 0
   elif man.right :
     screen.blit(walk_right[man.moves],(man.x,man.y))
     man.moves += 1
     if man.moves == 5:
       man.moves = 0
       ##########
   elif man.kick :
     screen.blit(kick[man.moves],(man.x,man.y))
     man.moves += 1
     if man.moves == 3:
       man.moves = 0
   elif man.kick_right : 
     screen.blit(kick_right[man.moves],(man.x,man.y))
     man.moves += 1
     if man.moves == 3:
       man.moves = 0
       ##########
   elif man.push:
     screen.blit(push[man.moves],(man.x,man.y))
     man.moves += 1
     if man.moves == 4:
       man.moves = 0
   elif man.push_right : 
     screen.blit(push_right[man.moves],(man.x,man.y))                   
     man.moves += 1
     if man.moves == 4:
       man.moves = 0
   else : #pass #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     if toright :
      screen.blit(king_right,(man.x,man.y))
     elif toleft :
       screen.blit(king,(man.x,man.y))
     else :screen.blit(king,(man.x,man.y))
   #evil_show= False
   def evil_show():
    if score <= 100 : evil.draw(screen)
   pygame.font.get_fonts()
   f=pygame.font.SysFont("comicsans",40,True,True)
   f1=pygame.font.SysFont("comicsans",40,True,True)
   text= f.render("SCORE >>"+str(score),True,(98,56,100))
   h1 ="########"
   h2 ="    you"
   h3 ="#########"
   evil_show()
   if score  >=10 : h1 = "########"
   if score  >=20 : h1 = "######"
   if score  >=30 : h1 = "#####"
   if score  >=70 : h1 = "####"
   if score >= 80 : h1 = "###"
   if score >= 85 : h1 = "##"
   if score >= 90 : h1 = "#"
   if score  >=100 : h1 =""
   if score  >= 100 :
    evil.x = 0
    evil.y =0
    evil = enemy(0 ,0 ,0,0 ,0) 
    text= f.render("you win",True,(0,0,0))
    next= f.render("press F1 for next level",True,(255,0,0))
    screen.blit(next,(200,200))
   #################################
   if score == 100 : winvoice.play()
   text2= f1.render(""+str(h1),True,(255,0,0))
   text3= f.render(""+str(h2),True,(255,0,255))
   text4= f.render("Level : 1",True,(0,0,0))
   text5= f.render(""+str(h3),True,(0,255,0))  
   ball.draw(screen)
   pygame.draw.rect(screen,black,(0,0,120,40))
   screen.blit(text,(480,20))
   man.health = (man.x +10  ,man.y-30 ,man.width +10,man.height -180 )
   screen.blit(text2,(evil.health[0],evil.health[1]))
   screen.blit(text3,(man.health[0],man.health[1]-30))
   screen.blit(text5,(man.health[0],man.health[1]))
   screen.blit(text4,(5,3))
   man.frame = (man.x ,man.y ,man.width ,man.height)
   #pygame.draw.rect(screen ,(255,200,255),man.frame,1) 
   for fire in fires :fire.draw(screen) 
   pygame.display.update()         
 
 
     

