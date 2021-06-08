# Import the pygame module
import pygame
import random
import time
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# soundObj = pygame.mixer.Sound('C:/Users/Jędrzej/Desktop/leomusic1.wav')
# soundObj.play()
pygame.mixer.music.load('C:/Users/Jędrzej/Desktop/leomusic1.wav')
pygame.mixer.music.play(-1, 0.0)


#Szerokość i wysokość ekranu + obrazek na background
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
back=pygame.image.load("C:/Users/Jędrzej/Desktop/bgrnd.png")
# klasa playera, wybór 1/2 odnosi się do wyboru postaci
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        print("wybierz postac")
        wybor=int(input())
        if wybor==1:
            self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/ludzik11.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        elif wybor==2:
            self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/g5.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.zycie=3
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
        if pressed_keys[K_SPACE]:
            czas=pygame.time.get_ticks()
            print(czas)
            if czas<5000:
                self.rect.move_ip(0,-3)
                czas=0
        elif not pressed_keys[K_SPACE]:
            self.rect.move_ip(0,3)

        # granice poruszania się
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.bottom>=300 and self.rect.right>300:
            self.rect.top=300
    def get_selfrect(self):
        return self.rect.bottom
    def get_zycie(self):
        return self.zycie
    def odejmij_zycie(self):
        self.zycie-=1


# klasa kapci, które spadają z góry
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/laczek.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH - 600, SCREEN_WIDTH - 10),
                (SCREEN_HEIGHT/16),
            )
        )
        self.speed = 1

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right < 0:
            self.kill()

#klasa babci
class Babcia(pygame.sprite.Sprite):
    def __init__(self):
        super(Babcia, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/babcia1.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_s]:
            self.rect.y += 3
        if keystate[pygame.K_d]:
            self.rect.x += 3
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        #granice jej ruchu
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT/8:
            self.rect.bottom = SCREEN_HEIGHT/8

#klasa owoca
class Owoc(pygame.sprite.Sprite):
    def __init__(self):
        super(Owoc, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/jablko.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH - 500),(SCREEN_HEIGHT/4)))
#klasa platformy
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Jędrzej/Desktop/platform1.png")
        self.surf = pygame.Surface((SCREEN_WIDTH, 30))
        self.surf.fill((94,51,23))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/5, SCREEN_HEIGHT - 50))

#wyświetlanie żyć na ekreanie
font=pygame.font.Font("freesansbold.ttf",32)
textX=600
textY=550
def show_life(x, y):
    zycie=font.render("Życia:"+str(player.get_zycie()),True,(255,255,255))
    screen.blit(zycie,(x,y))

#stworzenie głownego ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Pojawianie się nowych kapci co jakis czas
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1250)
#wywołanie wszystkich klas
player = Player()
babcia= Babcia()
owoc=Owoc()
P1 = platform()
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(babcia)
all_sprites.add(owoc)
all_sprites.add(P1)
# Variable to keep the main loop running
running = True
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # wychodzenie z gry i odejmowanie życia
        elif event.type == QUIT:
            running = False
        elif player.get_selfrect()==600:
            player.odejmij_zycie()
            print("tracisz zycko")
            soundObj = pygame.mixer.Sound('C:/Users/Jędrzej/Desktop/jumpsound.wav')
            soundObj.play()
            if player.get_zycie()<=0:
                soundObj = pygame.mixer.Sound('C:/Users/Jędrzej/Desktop/jumpsound.wav')
                soundObj.play()
                time.sleep(1)
                running = False
                print("Game Over")

# dodawanie kapci
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    # Update enemy position
    enemies.update()
    babcia.update()
    owoc.update()
    P1.update()
# Fill the screen with white
    screen.fill((0,0,0))


# Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
    surf.fill((255, 255, 255))
    rect = surf.get_rect()

# This line says "Draw surf onto the screen at the center"
# Put the center of surf at the center of the display
    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )

# Draw surf at the new coordinates
      # Draw the player on the screen
    # screen.blit(player.surf, player.rect)
    # Draw all sprites
    screen.blit(back, [0, 0])
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    show_life(textX,textY)
    pygame.display.flip()
