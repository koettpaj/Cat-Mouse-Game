import pygame
import random
import math
import matplotlib.pyplot as plt

class Game:
    sizes = [100,85,64,50,30,15]

    pygame.init()
    display_w=1920
    display_h=1080
    black = (0,0,0)
    red = (255,0,0)
    gameDisplay = pygame.display.set_mode((display_w,display_h))
    pygame.display.set_caption("PointerTest")
    clock = pygame.time.Clock()
    crashed = False
    index=0
    xcord=0
    ycord=0
    oldx=0
    oldy=0
    circlelist=[]
    latesttime=0
    listofdists=[]
    dictdata={}
    draw=True


    def __init__(self):
        for size in self.sizes:
            for number in range(100):
                self.circlelist.append(Circle(size,self.display_w,self.display_h))
        for index in range(1,len(self.circlelist)):
            self.circlelist[index].dist=self.calculateDist(self.circlelist[index], self.circlelist[index - 1])


        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                elif event.type == pygame.MOUSEBUTTONUP:

                    if self.gameDisplay.get_at(pygame.mouse.get_pos())==(255,0,0,255):

                        if self.index==0:

                            self.latesttime=pygame.time.get_ticks()
                        else:
                            self.circlelist[self.index].timetoclick=pygame.time.get_ticks()-self.latesttime
                        print("DISTANCE OF "+str(self.circlelist[self.index].dist)+ " TOOK "+str(self.circlelist[self.index].timetoclick)+" to click.")
                        self.latesttime=pygame.time.get_ticks()

                        if self.index==len(self.circlelist)-1:
                            self.draw=False
                            self.getData()
                        self.index += 1








            self.gameDisplay.fill(self.black)
            self.drawRect()


            pygame.display.update()
            self.clock.tick(100)
        pygame.quit()


    def calculateDist(self,c1,c2):
        xdiff=c1.xcord-c2.xcord
        ydiff = c1.ycord - c2.ycord

        dist= math.sqrt(math.pow(xdiff,2)+math.pow(ydiff,2))
        return int(dist)

    def getData(self):
        for size in self.sizes:
            distlist=[]
            timelist = []
            for circle in self.circlelist:
                if circle.dist!=0 and circle.size==size:
                    print(str(circle.size)+" "+str(circle.dist)+" "+str(circle.timetoclick))
                    distlist.append(circle.dist)
                    timelist.append(circle.timetoclick)
            self.dictdata[size]=[distlist, timelist]

        plt.xlabel("Avstånd i pixlar")
        plt.ylabel("Tid i ms")
        for size in self.sizes:
            plt.scatter(self.dictdata[size][0],self.dictdata[size][1],label=size)
        plt.legend()
        plt.show()

        #or circle in self.circlelist:
         #   if circle.dist==0:



    def drawRect(self):
        if(self.draw):
            pygame.draw.circle(self.gameDisplay, self.red, (self.circlelist[self.index].getCords()), self.circlelist[self.index].getSize(), 0)


class Circle:
    xcord=0
    ycord=0
    size=0
    dist=0
    timetoclick=0

    def __init__(self,size,w,h):
        self.xcord = random.randrange(size, w - size)
        self.ycord = random.randrange(size, h - size)
        self.size=size


    def getCords(self):
        return self.xcord, self.ycord

    def getSize(self):
        return self.size
Game()