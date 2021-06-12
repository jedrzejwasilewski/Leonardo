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
    K_LCTRL,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Initialize pygame
pygame.init()

pygame.mixer.music.load('C:/Users/Jędrzej/Desktop/backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
back=pygame.image.load("C:/Users/Jędrzej/Desktop/bgrnd.png")
# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/ludzik11.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.position = pygame.math.Vector2(400, 300)
        self.mask = pygame.mask.from_surface(self.surf)
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
        if pressed_keys[K_LCTRL]:
            if pressed_keys[K_LCTRL]:
                for i in range(2):
                    self.rect.move_ip(0,-3)
                    pygame.time.wait(int(50))
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
        self.mask = pygame.mask.from_surface(self.surf)
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

class New_japko(pygame.sprite.Sprite):
    def __init__(self):
        super(New_japko, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/jablko.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH - 600, SCREEN_WIDTH - 10),
                (SCREEN_HEIGHT/16),
            )
        )
        self.speed = 3

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
        self.jablka = 5
    def get_jablka(self):
        return self.jablka
    def odejmij_jablka(self):
        self.jablka-=1


    # self.speed = 1
#Create basic platform class
class new_platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/platform1.png")
        self.image.set_colorkey(255, 255)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.surf)

platforms = pygame.sprite.Group() #(szerokość, wysokość, obe.lock, idk)
P1 = new_platform(150, 250, 68, 1)
P2 = new_platform(550, 450, 68, 1)
P3 = new_platform(378, 250, 68, 1)
# P4 = new_platform(random.randint(1, 790), random.randint(1, 590), 68, 1)
P4 = new_platform(450, 47, 68, 1)
P5 = new_platform(310, 370, 68, 1)
P6 = new_platform(635, 362, 68, 1)
P7 = new_platform(713, 301, 68, 1)
P8 = new_platform(30, 474, 68, 1)
P9 = new_platform(250, 100, 68, 1)
P10 = new_platform(532, 155, 68, 1)
P11 = new_platform(160, 400, 68, 1)
P12 = new_platform(600, 250, 68, 1)
platforms.add(P1)
platforms.add(P2)
platforms.add(P3)
platforms.add(P4)
platforms.add(P5)
platforms.add(P6)
platforms.add(P7)
platforms.add(P8)
platforms.add(P9)
platforms.add(P10)
platforms.add(P11)
platforms.add(P12)

def adjust_on_collision(player, platforms):
    for platform in platforms:
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            player.rect.bottom = hits[0].rect.top
# player.rect.bottom = player.position


def obstacleHit_or_not(player, platforms):
    for platform in platforms:
        hit = pygame.sprite.collide_rect(player, platform)
        if hit:
            return True and adjust_on_collision(player, platforms)
    return False
    player.rect.bottom=player.position

font=pygame.font.Font("freesansbold.ttf",20)
textX=650
textY=550
def show_time(x, y):
    zycie=font.render("Życia: "+str(player.get_zycie()),True,(255,255,255))
    jablka=font.render("Jabłka do zdobycia: "+str(owoc.get_jablka()),True,(255,255,255))
    screen.blit(zycie,(x,y))
    screen.blit(jablka,(580,575))

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# żróło: https://www.codegrepper.com/code-examples/python/pygame+text+on+screen+multiple+lines
def blit_text(surface, text, pos, font, color = pygame.Color('yellow')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
#
babcia = "Babcia"
babcia_opis = "Lubi robić na drutach i rozwiązywać krzyżówki." \
       "\nNa zamku, gdzie mieszka nigdy nie brakuje jej ulubionych lukrecjowych słodyczy." \
       "\nDla wszystkich wydaje się przemiłą starszą panią, ale to tylko pozory." \
       "\nNie lubi swoich wnuków."
wnuczek = "Wnuczek"
wnuczek_opis = "Lubi czytać komiksy o superbohaterach i grać w gry komputerowe." \
               "\nNienawidzi lukrecji i ciemnych, zimnych pomieszczeń." \
               "\nNa wakacje rodzice wysyłają go do babci."
info = "Żeby mieć siłę wrócić do domu (i wygrać grę), musisz zebrać wszystkie jabłka." \
             "\nUważaj! Możesz dostać kapciem w głowę albo spaść z platformy i stracić przez to życie!"
#
font1 = pygame.font.SysFont('Courier', 24)
screen.fill(pygame.Color('black'))

blit_text(screen, babcia, (394, 300), font1)
pygame.display.update()
pygame.time.wait(2000)
screen.fill(pygame.Color("black"))
pygame.display.update()

blit_text(screen, babcia_opis, (20, 220), font1)
pygame.display.update()
pygame.time.wait(10000)
screen.fill(pygame.Color("black"))
pygame.display.update()

blit_text(screen, wnuczek, (360, 300), font1)
pygame.display.update()
pygame.time.wait(2000)
screen.fill(pygame.Color("black"))
pygame.display.update()

blit_text(screen, wnuczek_opis, (20, 260), font1)
pygame.display.update()
pygame.time.wait(6500)
screen.fill(pygame.Color("black"))
pygame.display.update()

blit_text(screen, info, (20, 250), font1)
pygame.display.update()
pygame.time.wait(4500)
screen.fill(pygame.Color("black"))
pygame.display.update()

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 5
pygame.time.set_timer(ADDENEMY, 1250)

ADDJAPKO = pygame.USEREVENT + 1
pygame.time.set_timer(ADDJAPKO, 1250)
# Instantiate player. Right now, this is just a rectangle.
player = Player()
babcia= Babcia()
owoc=Owoc()
def gdzie_owoc(x, y):
    owoc.rect = owoc.surf.get_rect(center=(x,y))

gdzie_owoc(100,100)
gdzie_owoc(200,200)
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
japka = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(babcia)
all_sprites.add(owoc)
all_sprites.add(platforms)

Touching_laczek = False
Touching_jablko = False
# Variable to keep the main loop running
running = True

#
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

            new_enemy2 = Enemy()
            enemies.add(new_enemy2)
            all_sprites.add(new_enemy2)

            nowe_japko = New_japko()
            japka.add(nowe_japko)
            all_sprites.add(nowe_japko)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    # Update enemy position
    enemies.update()
    babcia.update()
    owoc.update()
    platforms.update()
    japka.update()

    print(obstacleHit_or_not(player, platforms))

    # kolizje z laczkami
    if Touching_laczek == False and pygame.sprite.spritecollideany(player, enemies, pygame.sprite.collide_mask):
        Touching_laczek = True
        player.odejmij_zycie()
        soundObj = pygame.mixer.Sound('C:/Users/Jędrzej/Desktop/lifesound.wav')
        soundObj.play()
        if player.get_zycie() <= 0:
                running = False
                print("Game Over")
    if Touching_laczek == True and not pygame.sprite.spritecollideany(player, enemies, pygame.sprite.collide_mask):
        Touching_laczek = False



    # kolizje z jabłkami
    if Touching_jablko == False and pygame.sprite.spritecollideany(player, japka):
        Touching_jablko = True
        owoc.odejmij_jablka()
        if owoc.get_jablka() <= 0:
            running = False
            print("Gratulacje, zwycięstwo!")
    if Touching_jablko == True and not pygame.sprite.spritecollideany(player, japka):
        Touching_jablko = False

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

gameover = "GAME OVER"
win = "Zwycięstwo!"
font2 = pygame.font.SysFont('impact', 50)
if player.get_zycie() <= 0:
    screen.fill(pygame.Color('black'))
    blit_text(screen, gameover, (300, 300), font2)
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill(pygame.Color("black"))
    pygame.display.update()

if owoc.get_jablka() <= 0:
    screen.fill(pygame.Color('black'))
    blit_text(screen, win, (300, 300), font2)
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill(pygame.Color("black"))
    pygame.display.update()
