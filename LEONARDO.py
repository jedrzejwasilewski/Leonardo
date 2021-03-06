# Importy
import pygame
import random
import time
# Zaimportowanie klawiszy
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
# Inicjalizacja pygame
pygame.init()

#nazwa okna i ikonka
pygame.display.set_caption ("Leonardo")
icon = pygame.image.load ("C:/Users/Jędrzej/Desktop/ludzik11.png")
pygame.display.set_icon (icon)

#muzyka w tle
pygame.mixer.music.load('C:/Users/Jędrzej/Desktop/backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)

# Wysokość i szerokośćekranu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
back=pygame.image.load("C:/Users/Jędrzej/Desktop/bgrnd.png")
# Klasa głównej postaci
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/ludzik11.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.position = pygame.math.Vector2(400, 300)
        self.mask = pygame.mask.from_surface(self.surf)
        self.zycie=3
    #Ruch postaci
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
        #slow motion
        if pressed_keys[K_LCTRL]:
            if pressed_keys[K_LCTRL]:
                for i in range(2):
                    self.rect.move_ip(0,-3)
                    pygame.time.wait(int(50))
        #skok i grawitacja
        if pressed_keys[K_SPACE]:
            self.rect.move_ip(0,-3)
        elif not pressed_keys[K_SPACE]:
            self.rect.move_ip(0,3)

        # Granice poruszania się
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
    def get_podloga(self):
        return self.rect.bottom    

# Klasa laczków spadających z góry
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

    # Spadanie kapci i usuwanie ich z ekranu
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right < 0:
            self.kill()

#Klasa jabłek do zebrania
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

    # Spadanie jabłek i usuwanie ich z ekranu
    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right < 0:
            self.kill()

#Klasa babci
class Babcia(pygame.sprite.Sprite):
    def __init__(self):
        super(Babcia, self).__init__()
        self.surf = pygame.image.load("C:/Users/Jędrzej/Desktop/babcia1.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
    #Poruszanie się babci tak żeby goniła wnuka
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

        #granice poruszania się babci tak, żeby była tylko na górze
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT/8:
            self.rect.bottom = SCREEN_HEIGHT/8

#Pierwotna klasa owoca, zawiera potrzebne funkcje do zbierania jablek
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
#Klasa platform
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

#Funkcja kolizji
def adjust_on_collision(player, platforms):
    for platform in platforms:
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            player.rect.bottom = hits[0].rect.top
# player.rect.bottom = player.position

#2 funkcja kolizji
def obstacleHit_or_not(player, platforms):
    for platform in platforms:
        hit = pygame.sprite.collide_rect(player, platform)
        if hit:
            return True and adjust_on_collision(player, platforms)
    return False
    player.rect.bottom=player.position

#Czcionka i wyświetlanie życia oraz zebranych jablek
font=pygame.font.Font("freesansbold.ttf",20)
textX=650
textY=550
def show_time(x, y):
    zycie=font.render("Życia: "+str(player.get_zycie()),True,(255,255,255))
    jablka=font.render("Jabłka do zdobycia: "+str(owoc.get_jablka()),True,(255,255,255))
    screen.blit(zycie,(x,y))
    screen.blit(jablka,(580,575))

# Wyświetlanie ekranu gry
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# żróło: https://www.codegrepper.com/code-examples/python/pygame+text+on+screen+multiple+lines
#funkcja wyświetlania i zawijania tekstu
def blit_text(surface, text, pos, font, color = pygame.Color('yellow')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

#Początkowy tekst
babcia = "Babcia"
babcia_opis = "Lubi robić na drutach i rozwiązywać krzyżówki." \
       "\nNa zamku, gdzie mieszka nigdy nie brakuje jej ulubionych lukrecjowych słodyczy." \
       "\nDla wszystkich wydaje się przemiłą starszą panią, ale to tylko pozory." \
       "\nNie lubi swoich wnuków."
wnuczek = "Wnuczek"
wnuczek_opis = "Lubi czytać komiksy o superbohaterach i grać w gry komputerowe." \
               "\nNienawidzi lukrecji i ciemnych, zimnych pomieszczeń." \
               "\nNa wakacje rodzice wysyłają go do babci."
info = "Żeby mieć siłę wrócić do domu (i wygrać grę), musisz zebrać 5 jabłek." \
             "\nUważaj! Możesz dostać kapciem w głowę albo spaść z platformy i stracić przez to życie!"
info2 = "Sterowanie:" \
       "\n [lewa strzałka] - ruch w lewo" \
       "\n [prawa strzałka] - ruch w prawo" \
       "\n [spacja] - podskok" \
       "\n [lewy control] - zwalnianie kapci po zebraniu jabłka (5 sekund)"
#czcionka
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

blit_text(screen, info2, (20, 250), font1)
pygame.display.update()
pygame.time.wait(7000)
screen.fill(pygame.Color("black"))
pygame.display.update()

# Pojawianie się kapci
ADDENEMY = pygame.USEREVENT + 5
pygame.time.set_timer(ADDENEMY, 1250)

# Pojawianie się owoców
ADDJAPKO = pygame.USEREVENT + 1
pygame.time.set_timer(ADDJAPKO, 1250)
# Wywołanie klas
player = Player()
babcia= Babcia()
owoc=Owoc()
def gdzie_owoc(x, y):
    owoc.rect = owoc.surf.get_rect(center=(x,y))

gdzie_owoc(100,100)
gdzie_owoc(200,200)
# Stworzenie grup kapci oraz owoców, dodanie pozostałych obiektów do all sprites
enemies = pygame.sprite.Group()
japka = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(babcia)
all_sprites.add(owoc)
all_sprites.add(platforms)

Touching_laczek = False
Touching_jablko = False
# Zmienna dotycząca głównej pętli gry
running = True

#
#Główna pętla gry
while running:
    for event in pygame.event.get():
        # Sprawdzanie czy gracz wcisnął klawisz
        if event.type == KEYDOWN:
            # Escape kończy grę
            if event.key == K_ESCAPE:
                running = False

        #Kliknięcie krzyżyka kończy grę.
        elif event.type == QUIT:
            running = False
        #Koniec gry gdy skończy się życie
        elif player.get_selfrect()==600:
            player.odejmij_zycie()
            print("tracisz zycko")
            if player.get_zycie()<=0:
                running = False
                print("Game Over")
        #dotknięcie podłogi kończy grę
        elif player.get_podloga() >= SCREEN_HEIGHT:
            running = False
            print("Game Over")
# Eventy z pojawianiem się kapci i owoców
        elif event.type == ADDENEMY:
            #Kapcie
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

            new_enemy2 = Enemy()
            enemies.add(new_enemy2)
            all_sprites.add(new_enemy2)

            #owoc
            nowe_japko = New_japko()
            japka.add(nowe_japko)
            all_sprites.add(nowe_japko)
        # zamykanie programu po naciśnięciu x w oknie pygame
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Skorzystanie z funkcji pygamemowej wciskania klawiszy, potrzebnej do sterowania
    pressed_keys = pygame.key.get_pressed()
    # Update sterowania gracza
    player.update(pressed_keys)
    # Update pozostałych obiektów
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

# Wyświetlanie tła ekranu i "narysowanie" wszystkich obiektów
    screen.blit(back, [0, 0])
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    show_time(textX,textY)
    pygame.display.flip()

#Plansza końcowa z napisem game over lub zwycięstwo
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

#Źródła
#https://realpython.com/pygame-a-primer/#background-and-setup
#https://www.youtube.com/watch?v=FfWpgLFMI7w&t=6140s
#https://coderslegacy.com/python/pygame-platformer-game-development/ 
#https://www.youtube.com/watch?v=pN9pBx5ln40
#https://www.youtube.com/watch?v=BKtiVKNsOYk
#https://gamedev.stackexchange.com/questions/172975/how-to-make-player-land-on-platforms-more-than-one-in-pygame
#https://www.youtube.com/watch?v=Dspz3kaTKUg
#https://www.codegrepper.com/code-examples/python/pygame+text+on+screen+multiple+lines
