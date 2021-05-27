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

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
back=pygame.image.load("C:/Users/Jędrzej/Desktop/bgrnd.png")
# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
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
            self.rect.move_ip(0,-3)
        elif not pressed_keys[K_SPACE]:
            self.rect.move_ip(0,3)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    def get_selfrect(self):
        return self.rect.bottom
    def get_zycie(self):
        return self.zycie
    def odejmij_zycie(self):
        self.zycie-=1

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
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


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT/8:
            self.rect.bottom = SCREEN_HEIGHT/8

class Owoc(pygame.sprite.Sprite):
    def __init__(self):
        super(Owoc, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/jablko.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH - 500),(SCREEN_HEIGHT/4)))
    # self.speed = 1
#Create basic platform class
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Jędrzej/Desktop/platform1.png")
        self.surf = pygame.Surface((SCREEN_WIDTH, 30))
        self.surf.fill((94,51,23))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/5, SCREEN_HEIGHT - 50))

font=pygame.font.Font("freesansbold.ttf",32)
textX=650
textY=550
def show_time(x, y):
    zycie=font.render("Życia:"+str(player.get_zycie()),True,(255,255,255))
    screen.blit(zycie,(x,y))
P1 = platform()
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.font.init()

font = pygame.font.SysFont("Courier", 24)
Grandma_text = font.render("Babcia lubi robić na drutach i rozwiązywać krzyżówki.", False, [255, 215, 5])
screen.blit(Grandma_text, [44, 100])
pygame.display.flip()
# screen.fill(pygame.Color("black"))
# pygame.display.update()

# Grandma_text2 = font.render("Lubi robić na drutach i rozwiązywać krzyżówki.", False, [255, 215, 5])
# screen.blit(Grandma_text2, [0, 0])
# pygame.display.flip()
#
Grandma_text3 = font.render("Na zamku, gdzie mieszka nigdy nie brakuje jej ulubionych lukrecjowych słodyczy.", False, [255, 215, 5])
screen.blit(Grandma_text3, [44,200])
pygame.display.flip()
#
# Grandma_text4 = font.render("Dla wszystkich wydaje się przemiłą starszą panią, ale uwaga!", False, [255, 215, 5])
# screen.blit(Grandma_text4, [0, 0])
# pygame.display.flip()
#
# Grandma_text5 = font.render("Nie lubi swoich wnuków!", False, [255, 215, 5])
# screen.blit(Grandma_text5, [0, 0])
# pygame.display.flip()
#
# Grandson_text1 = font.render("Wnuczek", False, [255, 215, 5])
# screen.blit(Grandson_text1, [394, 400])
# pygame.display.flip()
#
# Granddaughter_text1 = font.render("Wnuczka", False, [255, 215, 5])
# screen.blit(Granddaughter_text1, [394, 400])
# pygame.display.flip()
#
# Grandchild_text1 = font.render("Lubi czytać komiksy o superbohaterach i grać w gry komputerowe.", False, [255, 215, 5])
# screen.blit(Grandchild_text1, [0, 0])
# pygame.display.flip()
#
# Grandchild_text2 = font.render("Nienawidzi lukrecji i ciemnych, zimnych pomieszczeń.", False, [255, 215, 5])
# screen.blit(Grandchild_text2, [0, 0])
# pygame.display.flip()
#
# Grandson_text2 = font.render("Na wakacje rodzice wysyłają go do babci.", False, [255, 215, 5])
# screen.blit(Grandson_text2, [0, 0])
# pygame.display.flip()
#
# Granddaughter_text2 = font.render("Na wakacje rodzice wysyłają ją do babci.", False, [255, 215, 5])
# screen.blit(Granddaughter_text2, [0, 0])
# pygame.display.flip()
#
# Info_text1 = font.render("Żeby wrócić do domu musisz znaleźć wszystkie cenne przedmioty strzeżone przez babcię.", False, [255, 215, 5])
# screen.blit(Info_text1, [0, 0])
# pygame.display.flip()
#
# Info_text2 = font.render("Ostrożnie! Babcia atakuje!", False, [255, 215, 5])
# screen.blit(Info_text2, [0, 0])
# pygame.display.flip()
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1250)
# Instantiate player. Right now, this is just a rectangle.
player = Player()
babcia= Babcia()
owoc=Owoc()
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

# screen.fill((0,0,0))
# time.sleep(5)
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        elif player.get_selfrect()==600:
            player.odejmij_zycie()
            print("tracisz zycko")
            if player.get_zycie()<=0:
                running = False
                print("Game Over")
# Add a new enemy?
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
    show_time(textX,textY)
    pygame.display.flip()
