import pygame

pygame.init()

#ekran, szerokosc i wysokosc
screen=pygame.display.set_mode((800, 600))

#tytul i ikonka
pygame.display.set_caption("Leonardo")
#player
grafikapostaci=pygame.image.load("C:/Users/Jędrzej/Desktop/ludzik1.png")
playerx=300
playery=200
playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(grafikapostaci,(x,y))

#petla ktora sprawia ze gra dziala
running=True
while running:
#sterowanie strzalkami
    for event in pygame.event.get():
        #wyjscie po kliknieciu x w rogu
        if event.type == pygame.QUIT:
            running = False
        #kiedy klawisz jest wcisniety
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_DOWN:
                playerY_change=0.2
            if event.key==pygame.K_SPACE:
                playerY_change=-0.3
        #kiedy puszczamy klawisz
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
            if event.key==pygame.K_DOWN:
                playerY_change=0
            if event.key==pygame.K_SPACE:
                playerY_change=0.3



#wyświetlanie koloru tła
    screen.fill((0,10,0))
#ruch gracza
    playerx+=playerX_change
    playery+=playerY_change
#granice mapy    
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    elif playery<=0:
        playerY_change=0
    elif playery>=360:
        playerY_change=0
    player(playerx,playery)
    pygame.display.update()