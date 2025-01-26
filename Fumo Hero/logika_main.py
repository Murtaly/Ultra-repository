from pygame import *
import random
mixer.init()

screen = display.set_mode((900, 720))
display.set_caption("Fumo Hero")

background = transform.scale(image.load("Fumo Hero/background_space.jpg"), (900, 720))

screen.blit(background, (0, 0))

win_width = 900
win_height = 720
Fumo_spawn_y = -65
allbullets = []
last_shoot_time = 0
shoot_delay = 100



last_hit_time = 0
hit_delay = 100

baka = mixer.Sound("Fumo Hero/baka-cirno.mp3")

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
    cirno_idle = ["Cirno0.png", "Cirno1.png", "Cirno2.png", "Cirno3.png", "Cirno4.png", "Cirno5.png"]
    cirno_right = ["Cirnowalk0.png", "Cirnowalk1.png", "Cirnowalk2.png", "Cirnowalk3.png", "Cirnowalk4.png", "Cirnowalk5.png", "Cirnowalk6.png", "Cirnowalk7.png"]
    cirno_left = ["Cirnowalk_-0.png", "Cirnowalk_-1.png", "Cirnowalk_-2.png", "Cirnowalk_-3.png", "Cirnowalk_-4.png", "Cirnowalk_-5.png", "Cirnowalk_-6.png", "Cirnowalk_-7.png"]
    counter_idle = 0
    counter_right = 0
    counter_left = 0
    def update(self):
        global last_shoot_time
        global shoot_delay
        current_time = time.get_ticks()
        
        
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
        
        if keys[K_SPACE] and current_time - last_shoot_time >= shoot_delay:
            
            Bullet.create_bullet(self, allbullets)
            last_shoot_time = current_time

    def idle(self):
        keys = key.get_pressed()
        if not keys[K_a] and not keys[K_d] and not keys[K_w] and not keys[K_s] and not keys[K_SPACE]:
            self.counter_idle += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/{self.cirno_idle[int(self.counter_idle)]}"), (65, 65))
                
            if self.counter_idle >= len(self.cirno_idle) - 1:
                self.counter_idle = 0
        #if self.move_right():
            #self.counter -= self.counter



    def move_right(self):
            keys = key.get_pressed()
            if keys[K_d]:
                self.counter_right += 0.05
                self.image = transform.scale(image.load(f"Fumo Hero/{self.cirno_right[int(self.counter_right)]}"), (65, 65))
                    
                if self.counter_right >= len(self.cirno_right) - 1:
                    self.counter_right = 0

    def move_left(self):
            keys = key.get_pressed()
            if keys[K_a]:
                self.counter_left += 0.05
                self.image = transform.scale(image.load(f"Fumo Hero/{self.cirno_left[int(self.counter_left)]}"), (65, 65))
                    
                if self.counter_left >= len(self.cirno_left) - 1:
                    self.counter_left = 0


        

class Bullet(sprite.Sprite):
    def __init__(self, bullet_image, bullet_x, bullet_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(bullet_image), (20, 36))
        self.rect = self.image.get_rect()
        self.rect.x = bullet_x
        self.rect.y = bullet_y
        self.speed = speed
        

    def draw_bullet(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    direction = "up"

    def create_bullet(self, allbullets):
        bullet = Bullet("Fumo Hero/Bullet.png", Fumo_destroyer.rect.x + 25, Fumo_destroyer.rect.y, 2)
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
            


Fumo_destroyer = Player('Fumo Hero/Cirno0.png', (win_width / 2) - 65, win_height - 160, 4)
Bad_Fumo = Enemy('Fumo Hero/Cirno9.webp', (win_width / 2) -50, 0, 1)

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
            if event.key == K_SPACE:
                can_shoot = True
    if finish != True:
        screen.blit(background, (0, 0))
        Fumo_destroyer.reset()
        Fumo_destroyer.update()
        Fumo_destroyer.idle()
        Fumo_destroyer.move_right()
        Fumo_destroyer.move_left()
        Bad_Fumo.reset()
        Bad_Fumo.update()
        

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