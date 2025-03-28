from pygame import *
import random
import math


mixer.init() 

screen = display.set_mode((900, 720))
display.set_caption("Fumo Hero")

background = transform.scale(image.load("Fumo Hero/sprites/background_space.jpg"), (900, 720))

screen.blit(background, (0, 0))

win_width = 900
win_height = 720
Fumo_spawn_y = -65
allbullets = []
enemy_bullets = []
bombitem = []
healitem = []
last_shoot_time = 0
shoot_delay = 100

last_hit_time = 0
hit_delay = 100

counter_time = 0

#mixer.music.load('Fumo Hero/bgm.ogg')
#mixer.music.play()

baka = mixer.Sound("Fumo Hero/baka-cirno.mp3")

class GameSprite(sprite.Sprite):    
    def __init__(self, player_image, playerX, playerY, player_speed, width, heigth):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, heigth))
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
    cirno_s_attack = ["Cirno_s1.png", "Cirno_s2.png", "Cirno_s3.png", "Cirno_s4.png", "Cirno_s5.png", "Cirno_s6.png", "Cirno_s7.png", "Cirno_s8.png"]
    cirno_right = ["Cirnowalk0.png", "Cirnowalk1.png", "Cirnowalk2.png", "Cirnowalk3.png", "Cirnowalk4.png", "Cirnowalk5.png", "Cirnowalk6.png", "Cirnowalk7.png"]
    cirno_left = ["Cirnowalk_-0.png", "Cirnowalk_-1.png", "Cirnowalk_-2.png", "Cirnowalk_-3.png", "Cirnowalk_-4.png", "Cirnowalk_-5.png", "Cirnowalk_-6.png", "Cirnowalk_-7.png"]
    counter_idle = 0
    counter_s_attack = 0
    counter_right = 0
    counter_left = 0
    health_counter = 100 #3
    bomb_counter = 115 #3

    Health_image = transform.scale(image.load("Fumo Hero/sprites/Health.png"), (64, 64))

    bomb_image = transform.scale(image.load("Fumo Hero/sprites/kostichka.jpg"), (64, 64))

    def update(self):
        
        global last_shoot_time
        global shoot_delay
        current_time = time.get_ticks()

        if self.health_counter >= 5:
            screen.blit(self.Health_image, (256, win_height-64))        
        if self.health_counter >= 4:
            screen.blit(self.Health_image, (192, win_height-64))
        if self.health_counter >= 3:
            screen.blit(self.Health_image, (128, win_height-64))
        if self.health_counter >= 2:
            screen.blit(self.Health_image, (64, win_height-64))
        if self.health_counter >= 1:
            screen.blit(self.Health_image, (0, win_height-64))
        
        if self.bomb_counter >= 5:
            screen.blit(self.bomb_image, (win_width - 320, win_height-64))        
        if self.bomb_counter >= 4:
                screen.blit(self.bomb_image, (win_width - 256, win_height-64))
        if self.bomb_counter >= 3:
                screen.blit(self.bomb_image, (win_width - 192, win_height-64))
        if self.bomb_counter >= 2:
                screen.blit(self.bomb_image, (win_width - 128, win_height-64))
        if self.bomb_counter >= 1:
                screen.blit(self.bomb_image, (win_width - 64, win_height-64))
        
        
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
        
        if keys[K_LSHIFT]:
            self.speed = 1
        else:
            self.speed = 4

    def use_bomb(self):
        keys = key.get_pressed()
        if keys[K_r] and self.bomb_counter > 0:
            self.counter_s_attack += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.cirno_s_attack[int(self.counter_s_attack)]}"), (65, 65))
                    
            if self.counter_s_attack >= len(self.cirno_s_attack) - 1:
                self.counter_s_attack = 0

            self.bomb_counter -= 1
            print (self.bomb_counter)
            enemy_bullets.clear()

        # if event.type == KEYDOWN:
        #     if event.key == K_r and self.bomb_counter > 0:
        #         self.bomb_counter -= 1
        #         enemy_bullets.clear()

    def idle(self):
        keys = key.get_pressed()
        if not keys[K_a] and not keys[K_d] and not keys[K_w] and not keys[K_s] and not keys[K_SPACE]:
            self.counter_idle += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.cirno_idle[int(self.counter_idle)]}"), (65, 65))
                
            if self.counter_idle >= len(self.cirno_idle) - 1:
                self.counter_idle = 0

    def move_right(self):
        keys = key.get_pressed()
        if keys[K_d]:
            self.counter_right += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.cirno_right[int(self.counter_right)]}"), (65, 65))
                
            if self.counter_right >= len(self.cirno_right) - 1:
                self.counter_right = 0

    def move_left(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.counter_left += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.cirno_left[int(self.counter_left)]}"), (65, 65))
                
            if self.counter_left >= len(self.cirno_left) - 1:
                self.counter_left = 0
    def health(self, health_counter):
        global running
        self.health_counter -= 1
        self.rect.x =(win_width / 2) - 65
        self.rect.y = win_height - 160
        if self.health_counter < 0:
            running = False


    def bombadd(self):
        self.bomb_counter += 1
    def healadd(self):
        self.health_counter += 1


class items(GameSprite):
    def update(self):
        self.rect.y += self.speed


    def create_item_bomb():
        bomb_item = items("Fumo Hero/sprites/Bomb.png", Bad_Fumo.rect.x + 50, Bad_Fumo.rect.y, 1, 64, 64)
        bombitem.append(bomb_item)

    def create_item_health():
        heal_item = items("Fumo Hero/sprites/Health.png", Bad_Fumo.rect.x - 50, Bad_Fumo.rect.y, 1, 64, 64)
        healitem.append(heal_item)      


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
        bullet = Bullet("Fumo Hero/sprites/Bullet.png", Fumo_destroyer.rect.x + 25, Fumo_destroyer.rect.y, 5)
        allbullets.append(bullet)

    def update(self):
        if self.rect.y >= win_height - 20:
            self.direction = "up"
    
        if self.direction == "up":
            self.rect.y -= self.speed

class EnemyBullet(sprite.Sprite):
    def __init__(self, bullet_image, bullet_x, bullet_y, speed, angle=0):
        super().__init__()
        original_image = image.load(bullet_image)
        self.image = transform.scale(original_image, (20, 36))
        self.image = transform.rotate(self.image, -angle - 90)  # Поворот на вказаний кут
        self.rect = self.image.get_rect(center=(bullet_x, bullet_y))
        self.speed = speed
        self.angle = angle

    def draw_bullet(self):
        screen.blit(self.image, self.rect.topleft)

    def update(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

        if self.rect.y > win_height or self.rect.y < 0 or self.rect.x > win_width or self.rect.x < 0:
            self.kill()

class Enemy(GameSprite):
    direction = "left"
    shoot_delay = 300  # Delay between shots
    last_shot_time = 0
    current_pattern_index = 0
    counter_idle = 0
    counter_attack = 0
    sakuya_idle = ["Sakuya_idle1.png", "Sakuya_idle2.png", "Sakuya_idle3.png", "Sakuya_idle4.png", "Sakuya_idle5.png", "Sakuya_idle6.png"]
    sakuya_attack = ["Sakuya_attack1.png", "Sakuya_attack2.png", "Sakuya_attack3.png", "Sakuya_attack4.png", "Sakuya_attack5.png", "Sakuya_attack6.png", "Sakuya_attack7.png"]

    def idle(self):
        self.counter_idle += 0.05
        self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.sakuya_idle[int(self.counter_idle)]}"), (50, 102))
                
        if self.counter_idle >= len(self.sakuya_idle) - 1:
            self.counter_idle = 0

    def attack(self):
        self.counter_attack += 0.05
        self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.sakuya_attack[int(self.counter_attack)]}"), (65, 102))
                
        if self.counter_attack >= len(self.sakuya_attack) - 1:
            self.counter_attack = 0

    def update(self):
        if self.direction == "down":
            self.rect.y += self.speed

        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed


        if self.direction == "up":
            self.rect.y -= self.speed

        # Shooting logic
        current_time = time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            
            self.patterns[self.current_pattern_index](self)
            self.last_shot_time = current_time
        self.draw_hp_bar(self.max_health, self.enemy_health)

        self.Bad_fumo_fight()

    def none(self):
        None

    def Bad_fumo_fight(self):

        if self.enemy_health >= 75:
            self.attack()
            self.current_pattern_index = 0
            if self.rect.x > win_width - 200:
                self.direction = "left"
            if self.rect.x < 200:
                self.direction = "right"
        
        if 60 <= self.enemy_health <= 75:
            self.idle()
            self.current_pattern_index = 4
            self.speed = 0
            
        if 35 <= self.enemy_health <= 60:
            self.attack()
            self.speed = 2
            if self.rect.x > win_width - 200:
                self.current_pattern_index = 3
                self.direction = "left"
            if self.rect.x < 200:
                self.current_pattern_index = 3
                self.direction = "right"

        if 20 <= self.enemy_health <= 35:
            self.idle()
            self.current_pattern_index = 4
            self.speed = 0

        if 0 <= self.enemy_health <= 20:
            self.attack()
            self.speed = 2
            if self.rect.x > win_width - 200:
                self.current_pattern_index = 2
                self.direction = "left"
            if self.rect.x < 200:
                self.current_pattern_index = 2
                self.direction = "right"


    def Cross_pattern(self):
        for angle in [0, 90, 180, 270]:
           bullet = EnemyBullet("Fumo Hero/sprites/Bullet.png", self.rect.x + 25, self.rect.y + 25, 2, angle)
           enemy_bullets.append(bullet)

        # Additional patterns can be added here
        # Example: Circle pattern

    def Spiral_pattern(self):
        num_bullets = 10  # Number of bullets in the spiral
        angle_step = 180 / num_bullets  # How much angle to increase for each bullet
        
        for i in range(num_bullets):
            angle = i * angle_step
            bullet = EnemyBullet("Fumo Hero/sprites/Bullet.png", self.rect.x + 25, self.rect.y + 25, 2, angle)
            enemy_bullets.append(bullet)

    def V_shape(self):
        angles = [23, 45, 67, 90, 111, 135, 157]
        for angle in angles:
            bullet = EnemyBullet("Fumo Hero/sprites/Bullet.png", self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)

    def Laser_Beam_pattern(self):
        rows = 2
        cols = 3
        bullet_spacing = 100  # Distance between each bullet

        for i in range(rows):
            for j in range(cols):
                bullet_x = self.rect.x + (j - cols // 2) * bullet_spacing
                bullet_y = self.rect.y + (i - rows // 2) * bullet_spacing
                bullet = EnemyBullet("Fumo Hero/sprites/Bullet.png", bullet_x, bullet_y, 3,90)
                enemy_bullets.append(bullet)

        bullet = EnemyBullet("Fumo Hero/sprites/Bullet.png", self.rect.x + 25, self.rect.y + 25, 5)
        bullet.angle = 90  # Straight down
        
    

    enemy_health = 100
    max_health = 100
    patterns = [V_shape, Cross_pattern, Spiral_pattern, Laser_Beam_pattern, none]

    def draw_hp_bar(self, max_health, enemy_health):
        draw.rect(screen, (255,0,0), (50, 25, win_width - 100, 20))
        
        draw.rect(screen, (0,255,0), (50, 25, (enemy_health / max_health) * (win_width - 100), 20))
    
    def hp_del(self):
        self.enemy_health -= 1


    enemy_health = 100
    max_health = 100
    patterns = [V_shape, Cross_pattern, Spiral_pattern, Laser_Beam_pattern, none]

    def draw_hp_bar(self, max_health, enemy_health):
        draw.rect(screen, (255,0,0), (50, 25, win_width - 100, 20))
        
        draw.rect(screen, (0,255,0), (50, 25, (enemy_health / max_health) * (win_width - 100), 20))
    
    def hp_del(self):
        self.enemy_health -= 1
        

Fumo_destroyer = Player('Fumo Hero/sprites/Cirno0.png', (win_width / 2) - 65, win_height - 160, 4, 64,64)
Fumo_destroyer_hitbox = GameSprite('Fumo Hero/sprites/hitbox.png', Fumo_destroyer.rect.x, Fumo_destroyer.rect.y, 4, 16, 16)

Bad_Fumo = Enemy('Fumo Hero/sprites/Cirno9.webp', (win_width / 2) -50, 64, 2, 50,102)

clock = time.Clock()
frames = 144

last_hit_health_time = 0
hit_health_delay = 2000

btn_play = GameSprite("Fumo Hero/sprites/button_play.png", 260, 80, 0, 320, 132) #transform.scale(image.load("Fumo Hero/button_play.png"), (192, 80))

btn_exit = GameSprite("Fumo Hero/sprites/button_exit.png", 260, 280, 0, 320, 132)#transform.scale(image.load("Fumo Hero/button_exit.png"), (192, 80))

btn_settings = GameSprite("Fumo Hero/sprites/button_settings.png", 260, 492, 0, 320, 132)#transform.scale(image.load("Fumo Hero/Button_settings.png"), (192, 92))

btn_sound = GameSprite("Fumo Hero/sprites/button_sound.png", 102, 280, 0, 150, 140)

btn_back = GameSprite("Fumo Hero/sprites/button_back.png", 5, 10, 0, 320, 132)


game = "menu"
running = True
mute = False
while running:
    counter_time += 1
    current_time = time.get_ticks()

    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN and btn_play.rect.collidepoint(Mouse):
            game = "game"

        if e.type == MOUSEBUTTONDOWN and btn_exit.rect.collidepoint(Mouse):
            running = False

        if e.type == MOUSEBUTTONDOWN and btn_settings.rect.collidepoint(Mouse):
            game = "settings"

        if e.type == MOUSEBUTTONDOWN and btn_back.rect.collidepoint(Mouse):
            game = "menu"

        if e.type == MOUSEBUTTONDOWN and btn_sound.rect.collidepoint(Mouse) and mute == False:
            btn_sound = GameSprite("Fumo Hero/sprites/button_mute_sound.png", 102, 280, 0, 150, 140)
            mute = True

        elif e.type == MOUSEBUTTONDOWN and btn_sound.rect.collidepoint(Mouse) and mute == True:
            btn_sound = GameSprite("Fumo Hero/sprites/button_sound.png", 102, 280, 0, 150, 140)
            mute = False


    if game == "menu":
        btn_back.kill()
        btn_sound.kill()
        Mouse = mouse.get_pos()
        screen.blit(background, (0,0))
        btn_play.reset()
        btn_exit.reset()
        btn_settings.reset()
        if btn_play.rect.collidepoint(Mouse):
            btn_play = GameSprite("Fumo Hero/sprites/button_play_pressed.png", 260, 80, 0, 320, 132)
        elif not btn_play.rect.collidepoint(Mouse):
            btn_play = GameSprite("Fumo Hero/sprites/button_play.png", 260, 80, 0, 320, 132)
            
        if btn_exit.rect.collidepoint(Mouse):
            btn_exit = GameSprite("Fumo Hero/sprites/button_exit_pressed.png", 260, 280, 0, 320, 132)
        elif not btn_exit.rect.collidepoint(Mouse):
            btn_exit = GameSprite("Fumo Hero/sprites/button_exit.png", 260, 280, 0, 320, 132)

        if btn_settings.rect.collidepoint(Mouse):
            btn_settings = GameSprite("Fumo Hero/sprites/button_settings_pressed.png", 260, 492, 0, 320, 132)
        elif not btn_settings.rect.collidepoint(Mouse):
            btn_settings = GameSprite("Fumo Hero/sprites/button_settings.png", 260, 492, 0, 320, 132)

    if game == "settings":
        btn_play.kill()
        btn_exit.kill()
        btn_settings.kill() 
        Mouse = mouse.get_pos()
        screen.blit(background, (0, 0))
        btn_sound.reset()
        btn_back.reset()
        if btn_back.rect.collidepoint(Mouse):
            btn_back = GameSprite("Fumo Hero/sprites/button_back_pressed.png", 5, 10, 0, 320, 132)
        elif not btn_back.rect.collidepoint(Mouse):
            btn_back = GameSprite("Fumo Hero/sprites/button_back.png", 5, 10, 0, 320, 132)

    if game == "game":
        if mute == True:
            mixer.stop()
        if Bad_Fumo.enemy_health <= 0:
            items.create_item_bomb()
            items.create_item_health()
            Bad_Fumo.rect.x = 10000000
        screen.blit(background, (0, 0))
        Fumo_destroyer.reset()
        Fumo_destroyer_hitbox.reset()
        Fumo_destroyer.update()
        Fumo_destroyer.idle()
        Fumo_destroyer.move_right()
        Fumo_destroyer.move_left()
        Fumo_destroyer.use_bomb()
        Bad_Fumo.reset()
        Bad_Fumo.update() 
        Fumo_destroyer_hitbox.rect.x = Fumo_destroyer.rect.x +32
        Fumo_destroyer_hitbox.rect.y = Fumo_destroyer.rect.y +32
        for i in allbullets:
            i.draw_bullet()
            if i.rect.y < 0:
                allbullets.remove(i)
            i.update()
            if sprite.collide_rect(i, Bad_Fumo):
                allbullets.remove(i)
                if current_time - last_hit_time >= hit_delay:
                    last_hit_time = current_time
                    Bad_Fumo.hp_del()
                    mixer.Sound.play(baka)
        
        for i in healitem:
            i.reset()
            if i.rect.y > win_height:
                 healitem.remove(i)
            i.update()
            if sprite.collide_rect(i, Fumo_destroyer):
                Fumo_destroyer.healadd()
                healitem.remove(i)

        for i in bombitem:
            i.reset()
            if i.rect.y > win_height:
                bombitem.remove(i)
            i.update()
            if sprite.collide_rect(i, Fumo_destroyer):
                Fumo_destroyer.bombadd()
                bombitem.remove(i)

        for bullet in enemy_bullets:
            bullet.draw_bullet()
            bullet.update()
            if sprite.collide_rect(bullet, Fumo_destroyer_hitbox) and current_time - last_hit_health_time >= hit_health_delay:
                enemy_bullets.remove(bullet)
                Fumo_destroyer.health(Player.health_counter)
                last_hit_health_time = current_time
                # Handle player hit logic here

    display.update()
    clock.tick(frames)