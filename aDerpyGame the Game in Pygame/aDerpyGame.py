import pygame
pygame.init()

window = pygame.display.set_mode((1720,880))

pygame.display.set_caption("a Derpy Game")





#variables
windowWidth = 1720
windowHeight= 880


x = windowWidth / 2
y = windowHeight / 2

vel=7#velocity

clock = pygame.time.Clock()

#Derp width and height pending screen size
derpWidth = windowWidth / 8.6
derpHeight = windowHeight / 5.5

#Derpy coordinates and puts derpy center of screen
derpX = x - derpWidth / 2 + 15
derpY = y - derpHeight / 2 + 35

#Derpy Center
derpCenterX = x + windowWidth / 2
derpCenterY = x + windowHeight / 2

 #Derp Left, Right, Top, Bottom
derpLeft = derpX + windowWidth/40
derpRight = derpX + derpWidth - windowWidth/41
derpTop = derpY + windowHeight/21
derpBottom = derpY + derpHeight - windowHeight/27
  
#InsaneDerp Variables
IDerpLeft = 240 + windowWidth/1.423276501111935
IDerpRight = 240+ derpWidth - windowWidth/1.423276501111935
DerpTop = 300 + windowHeight/1.147715196599362
IDerpBottom = 300 + derpHeight - windowHeight/1.147715196599362

#--image loading--
bg_1=pygame.image.load('bg_1.png')
bg_1=pygame.transform.scale(bg_1, (windowWidth,windowHeight))

Derpy=pygame.image.load('Derpy.png')
Derpy=pygame.transform.scale(Derpy, (derpWidth,derpHeight))
#--incase i ever need it for animating character--
# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# bg = pygame.image.load('bg.jpg')
# char = pygame.image.load('standing.png')





  


#------------------------WHATshowsUP----------------------
#this is basically the draw function remade so i dont have to keep making things show up ----Draw Here----

def redrawGameWindow():
    global walkCount#takes this variable to be a global varaible for hte whole game to use

    #window.fill((255,255,255)) SOLID BACKGROUND
    window.blit(bg_1, (0,0)) #PIC BACKGROUND
    window.blit(Derpy, (derpX,derpY))

    
    
    #pygame.draw.rect(window, (255,0,0),())

    #renders the text
    derpyXYtext= font.render("derpyX and derpyY : "+ str(derpX) + ", " + str(derpY),1,(0,0,0))
    derpyLefttext=font.render("derpLeft :"  + str(derpLeft),1,(0,0,0))
    derpyRighttext=font.render("derpRight : "  + str(derpRight),1,(0,0,0))
    derpyToptext=font.render("derpTop : "  + str(derpTop),1,(0,0,0))
    derpyBottomtext=font.render("derpBottom : "  + str(derpBottom),1,(0,0,0))

    #draws the text coords on screen
    window.blit(derpyXYtext,(20,20))
    window.blit(derpyLefttext,(20,40))
    window.blit(derpyRighttext,(20,60))
    window.blit(derpyToptext,(20,80))
    window.blit(derpyBottomtext,(20,100))

    
    pygame.draw.line(window, (255,0,0), (derpLeft, derpTop), (derpRight, derpTop),1) #Top of hit box
    pygame.draw.line(window,(255,0,0),(derpLeft, derpBottom), (derpRight, derpBottom),1) #Bottom of hit box
    pygame.draw.line(window,(255,0,0),(derpLeft, derpTop), (derpLeft, derpBottom),1) #Left hitbox
    pygame.draw.line(window,(255,0,0),(derpRight, derpTop), (derpRight, derpBottom),1) #Right hitbox
  
  
# InsaneDerp Hitbox
#   line(IDerpLeft, IDerpTop, IDerpRight, IDerpTop)
#   line(IDerpLeft, IDerpBottom, IDerpRight, IDerpBottom)
    
    pygame.display.update()














#-----------------------------------------------------------BEHIND the SCENES--------------------------------------------------
#mainLoop
#-----------------------Pygame window quit-----------------------

font = pygame.font.SysFont('comicsans', 15)#adds font and how big the text is
run = True
while run:
    clock.tick(60)#frame rate new
    #pygame.time.delay(50)#frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
#-----------------------------------------------------------------


#----------------movement---------------
    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] and derpX > vel-40:
        derpX-=vel
        derpLeft-=vel
        derpRight-=vel
        #probably wont need it but ill write it anyway
        # left = True
        # right=False

    elif keys[pygame.K_d] and derpX < windowWidth - derpWidth - vel+40:
        derpX+=vel
        derpLeft+=vel
        derpRight+=vel
        #probably wont need it but ill write it anyway
        # left=False
        # right=True

    #probably wont need it but ill write it anyway
    #else:
        # left:False
        # right=False
        # walkCount = 0


    elif keys[pygame.K_w] and derpY > vel-40: 
        derpY-=vel
        derpTop-=vel
        derpBottom-=vel
        #probably wont need it but ill write it anyway
        # left=False
        # right=False
        # walkCount=0


    elif keys[pygame.K_s] and derpY < windowHeight - derpHeight - vel + 30:
        derpY+=vel
        derpTop+=vel
        derpBottom+=vel
        #probably wont need it but ill write it anyway
        # left=False
        # right=False
        # walkCount=0

    redrawGameWindow() #calling function




pygame.quit()