from pygame import *
import random
mixer.init()

screen = display.set_mode((1000, 1080))
display.set_caption("Fumo Hero")

background = transform.scale(image.load("background_space.jpg"), (1000, 1080))

screen.blit(background, (0, 0))

win_width = 1000
win_height = 1080
Fumo_spawn_y = -65
allbullets = []
last_shoot_time = 0
shoot_delay = 100

last_hit_time = 0
hit_delay = 100

baka = mixer.Sound("baka-cirno.mp3")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, playerX, playerY, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def show_player(self):
        screen.blit(Fumo_destroyer, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        global last_shoot_time
        global shoot_delay
        current_time = time.get_ticks()
        
        
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
        
        if keys[K_e] and current_time - last_shoot_time >= shoot_delay:
            
            Bullet.create_bullet(self, allbullets)
            last_shoot_time = current_time

        

class Bullet(sprite.Sprite):
    def __init__(self, color, bullet_x, bullet_y, wall_width, wall_height, speed):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = bullet_x
        self.rect.y = bullet_y
        self.speed = speed
        

    def draw_bullet(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    direction = "up"

    def create_bullet(self, allbullets):
        bullet = Bullet("green", Fumo_destroyer.rect.x + 25, Fumo_destroyer.rect.y, 15, 15, 2)
        allbullets.append(bullet)

    def update(self):
        if self.rect.y >= win_height - 20:
            self.direction = "up"
    
        if self.direction == "up":
            self.rect.y -= self.speed



class Enemy(GameSprite):
    direction = "down"

    def update(self):
        if self.rect.y <= win_height + 70:
            self.direction = "down"

        if self.direction == "down":
            self.rect.y += self.speed

        if self.rect.y < -70:
            self.rect.y = Fumo_spawn_y
            self.rect.x = random.randint(10, 1070)
            
        if self.rect.y > win_height:
            self.rect.y = Fumo_spawn_y
            self.rect.x = random.randint(10, 1070)
            


Fumo_destroyer = Player('kostichka.jpg', (win_width / 2) - 65, win_height - 160, 4)
Bad_Fumo = Enemy('Cirno9.webp', (win_width / 2) -50, 0, 1)

clock = time.Clock()
frames = 144

finish = False
running = True
can_shoot = True
while running:
    current_time = time.get_ticks()
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif type == KEYUP:
            if event.key == K_e:
                can_shoot = True
    if finish != True:
        screen.blit(background, (0, 0))
        Fumo_destroyer.update()
        Bad_Fumo.update()

        Fumo_destroyer.reset()
        Bad_Fumo.reset()
        for i in allbullets:
            i.draw_bullet()
            if i.rect.y < 0:
                allbullets.remove(i)
            i.update()
            if sprite.collide_rect(i, Bad_Fumo):
                allbullets.remove(i)
                if current_time - last_hit_time >= hit_delay:
                    last_hit_time = current_time
                    mixer.Sound.play(baka)
                    


    display.update()
    clock.tick(frames)