
from time import sleep
import pygame ,sys
from pygame.locals import *
pygame.init()  
clock =pygame.time.Clock()
life = 4
score =0
level =1
jump = False
speed= 10
color = (0,150,200) 
black = ( 200,200,0)
screenwidth =800
screenheight =800
screen =pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("RUN M2ADgame")
mainloop = False

class object :
  def __init__(self, x, y, width ,height ,step ,image):
    self.x =x + 1000
    self.y =y
    self.height = height
    self.width =width
    self.step =step
    self.moves =0
    self.image=image
    self.frame = (self.x  ,self.y ,self.width ,self.height )
  def draw(self ,screen ):
     self.move()
     screen.blit(self.image,(self.x,self.y))
     #pygame.draw.rect(screen ,(0,23,89),self.frame,2)  
  def move(self):
    global score ,life
    if self.x - self.step <= mr.x and self.y  - self.height <= mr.y  and self.x >= 200: 
      global music
      #music.stop()
      #pygame.mixer.Sound("/home/kali/Desktop/game1/music/try.wav").play()
      screen.fill((0,0,0))
      sleep(.2)
      life -= 1
      if life <= 0 : 
       mainloop = False
       
    self.x -= self.step
    if self.x < 0 :
      self.x = 3000
      score += 1
      self.step+=.3

class player :
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
  def draw(self ,screen ):
    self.move()
    if self.step > 0 :
     screen.blit(walk_right[self.moves],(self.x,self.y))
     self.moves += 1
     if self.moves == 5:
       self.moves = 0
    self.frame = (self.x ,self.y ,self.width ,self.height)
    self.health = (self.x +10  ,self.y-40 ,20,20 )
    
    #pygame.draw.rect(screen ,(0,23,89),self.frame,2)  
    
    #pygame.draw.rect(screen ,(0,23,89),self.health,2)  
    pygame.draw.rect(screen ,(100,100,100),mr.health,1)   
  def move(self):
    self.x += 0
      
      
      
mr = player(200 ,600 ,130,200 ,51) 
king_right=pygame.image.load("photo/pl1.png")
king=pygame.image.load("photo/pin.png")
pin1=pygame.image.load("photo/pin1.png")
car =pygame.image.load("photo/car.png")
nice =pygame.image.load("photo/nice.png")
girl=pygame.image.load("photo/girl.png")
mountein=pygame.image.load("photo/mountein.png")
bg = pygame.image.load("photo/bg.png")
kick=[pygame.image.load("photo/k1.png"),pygame.image.load("photo/k2.png"),pygame.image.load("photo/k3.png")]
walk=[pygame.image.load("photo/r1.png"),pygame.image.load("photo/r4.png"),pygame.image.load("photo/r2.png"),pygame.image.load("photo/r3.png"),pygame.image.load("photo/r5.png"),pygame.image.load("photo/r1.png"),pygame.image.load("photo/r4.png"),pygame.image.load("photo/r2.png"),pygame.image.load("photo/r3.png"),pygame.image.load("photo/r5.png")]
walk_right=[pygame.image.load("photo/l1.png"),pygame.image.load("photo/l3.png"),pygame.image.load("photo/l2.png"),pygame.image.load("photo/l3.png"),pygame.image.load("photo/l5.png")]
music=pygame.mixer.Sound("music/song17.mp3")
music.play(-1,0)
jumpsound=pygame.mixer.Sound("music/missedkik.wav")
o =object(500,600,100,200,10,car)
o1 =object(600,600,100,200,10,car)
o4 =object(1000,600,100,200,10,nice)
o5 =object(1100,600,100,200,10,girl)
o7 =object(1600,600,100,200,10,car)
o8 =object(1500,600,100,200,10,king)
o9 =object(1900,600,100,200,10,car)
o10 =object(4000,600,100,200,10,girl) 
o3 =object(2900,600,100,200,10,car)
o6 =object(3000,600,100,200,10,car)
while True :
  #screen.blit(bg,(0,-180))
  f=pygame.font.SysFont("comicsans",40,True,True)
  star1= f.render("CONTANUE >F1 or RIGHT",True,(255,56,100))
  star2= f.render("""NEW GAME >F2""",True,(255,56,100))
  star3= f.render("SETTIN MUSIC >F3 , F4",True,(255,56,100))
  star4= f.render("""FULL SCREEN >F5 , F6""",True,(255,56,100))
  star5= f.render("EXIT >F12",True,(255,56,100))
  final= f.render("""YOUR  LAST SCORE IS { """+str(score)+" }",True,(0,0,0))
  pygame.draw.rect(screen ,(0,23,89),(20,80,400,30),20) 
  pygame.draw.rect(screen ,(0,23,89),(40,130,400,30),20) 
  pygame.draw.rect(screen ,(0,23,89),(80,170,400,30),20)
  pygame.draw.rect(screen ,(0,23,89),(120,230,400,30),20) 
  pygame.draw.rect(screen ,(0,23,89),(160,270,400,30),20) 
  pygame.draw.rect(screen ,(100,23,89),(0,400,1250,600))
  m=400 
  pygame.draw.rect(screen ,(0,123,89),(200,m,400,30),20)
  screen.blit(star1,(20,80))
  screen.blit(star2,(40,130))
  screen.blit(star3,(80,170))
  screen.blit(star4,(120,230))
  screen.blit(star5,(160,270))
  screen.blit(final,(200,400))
  clock.tick(50)
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
        quit()
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_F1 or event.key == pygame.K_RIGHT  : 
       sleep(1)
       mainloop = True
       life = 4
       score = 0
       #color = (100,150,200)
     elif event.key == (pygame.K_F2 ) : 
       pass
     elif event.key == (pygame.K_F3 ) : music.stop()
     elif event.key == (pygame.K_F4 ) : music.play(-1,0)
     elif event.key == (pygame.K_F5 ) : 
       screenwidth =1250
       screenheight =900
       screen =pygame.display.set_mode((screenwidth,screenheight))
     elif event.key == (pygame.K_F6 ) : 
       screenwidth =800
       screenheight =700
       screen =pygame.display.set_mode((screenwidth,screenheight))
     elif event.key == (pygame.K_F12 ) : exit()
     elif event.key == (pygame.K_SPACE) : 
      if mainloop == False : mainloop = True
      else : mainloop = False
     elif event.key == (pygame.K_UP ) : m = m - 10
     pygame.display.update 
  if mainloop :
   level =0
   screen.fill(color)
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_UP : 
      jump = True
      jumpsound.play(0,0) 
     if event.key == pygame.K_DOWN and mr.y + mr.height +10 <= screenheight  : mr.y += 10    
   if jump :
    if speed >= -10:
     neg = 1
     if speed<0 :
       neg = -1
     mr.y -=(mr.step ** 2)*1 * neg
     speed-=.5
    else : 
         speed =10
         jump=False
         mr.y= 550
   mr.draw(screen)
   o.draw(screen)
   o1.draw(screen)
   o3.draw(screen)
   o4.draw(screen)
   o5.draw(screen)
   o6.draw(screen)
   o7.draw(screen)
   o8.draw(screen)
   o9.draw(screen)
   o10.draw(screen)
   f=pygame.font.SysFont("comicsans",40,True,True)
   f1=pygame.font.SysFont("comicsans",40,True,True)
   text= f.render("SCORE >>"+str(score),True,(98,56,100))
   text1= f.render("Level : "+str(level),True,(255,0,0))
   text2= f.render(""+str(life),True,(255,0,0))
   screen.blit(text,(480,20))
   screen.blit(text1,(200,20))
   screen.blit(text2,(mr.health[0],mr.health[1]))
   if score >= 30 :
     level = 2
     color = (0,0,0)
   if life <= 0 :mainloop = False
  
  pygame.display.update()
