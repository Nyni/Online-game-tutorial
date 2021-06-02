import pygame
from network import Network

width = 500
height = 500


win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client)")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height) #redefine rect to move it

def read_pos(s):
#    print(s)
    s1 = s.split(",")
#    print(s1[0])
#    print(s1[1])
    return int(s1[0]), int(s1[1])

def make_pos(tup): #takes a tuple
    return str(tup[0]) + "," + str(tup[1]) #changed to match the server on the video







def redrawWindow(win,player,player2):

    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()



def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
#    startPos = n.getPos()

    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,255,0))

    clock = pygame.time.Clock()


    while run:
        #every frame update, send pos and get other player's pos

#        p2Pos = read_pos(n.send(make_pos((p.x,p.y))))

        print(n.send(make_pos((p.x,p.y))))
 #       p2Pos = read_pos("100,100")

 #       p2.x = p2Pos[0]
  #      p2.y = p2Pos[1]
        p2.update()


        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win,p, p2)

main()



