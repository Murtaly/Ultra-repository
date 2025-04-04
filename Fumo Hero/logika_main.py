from pygame import *
import random
import math

font.init()
mixer.init() 

screen = display.set_mode((900, 720))
display.set_caption("Fumo Hero")

background = transform.scale(image.load("Fumo Hero/sprites/background_space.jpg"), (900, 720))

screen.blit(background, (0, 0))

game = "menu"
win_width = 900
win_height = 720
Fumo_spawn_y = -65
allbullets = []
enemy_bullets = []
bombitem = []
healitem = []
round_over = False
random_number = random.randint(0, 9)
last_shoot_time = 0
shoot_delay = 100
font = font.SysFont("arial", 36)
last_hit_time = 0
hit_delay = 100
music = 'Fumo Hero/sounds/bgm.ogg'
mixer.music.load(music)

mixer.music.play(-1)
mixer.music.set_volume(0.5)
counter_time = 0




baka = mixer.Sound("Fumo Hero/sounds/baka-cirno.mp3")

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
    health_counter = 3 #3
    bomb_counter = 3 #3

    Health_image = transform.scale(image.load("Fumo Hero/sprites/Health.png"), (64, 64))

    bomb_image = transform.scale(image.load("Fumo Hero/sprites/bomb.png"), (64, 64))

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
        # keys = key.get_pressed()
        # if keys[K_r] and self.bomb_counter > 0:
        #     self.counter_s_attack += 0.05
        #     self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.cirno_s_attack[int(self.counter_s_attack)]}"), (65, 65))
                    
        #     if self.counter_s_attack >= len(self.cirno_s_attack) - 1:
        #         self.counter_s_attack = 0

        #     self.bomb_counter -= 1
        #     print (self.bomb_counter)
        #     enemy_bullets.clear()

        if e.type == KEYDOWN:
            if e.key == K_r and self.bomb_counter > 0:
                self.bomb_counter -= 1
                enemy_bullets.clear()

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
        
        self.enemy_image = transform.scale(original_image, Enemy.size)
        self.enemy_image = transform.rotate(self.enemy_image, -angle - 90)  # Поворот на вказаний кут
        self.rect = self.enemy_image.get_rect(center=(bullet_x, bullet_y))
        self.speed = speed
        self.angle = angle

    def draw_bullet(self):
        screen.blit(self.enemy_image, self.rect.topleft)
            
    def update(self):

        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))

        if self.rect.y > win_height or self.rect.y < 0 or self.rect.x > win_width or self.rect.x < 0:
            self.kill()

class Enemy(GameSprite):
    def __init__(self, player_image, playerX, playerY, player_speed, width, heigth, enemy_health, max_health):
        super().__init__(player_image, playerX, playerY, player_speed, width, heigth)
        self.direction = "left"
        self.shoot_delay = 300  # Delay between shots
        self.last_shot_time = 0
        self.current_pattern_index = 0
        self.enemy_health = enemy_health
        self.max_health = max_health
        self.start_time = None
        self.end_time = None
        self.bullet_image = "Fumo Hero/sprites/Bullet.png"
        
    size = (20, 36)
    lvl = 2
    sakuya_idle = ["Sakuya_idle1.png", "Sakuya_idle2.png", "Sakuya_idle3.png", "Sakuya_idle4.png", "Sakuya_idle5.png", "Sakuya_idle6.png"]
    sakuya_attack = ["Sakuya_attack1.png", "Sakuya_attack2.png", "Sakuya_attack3.png", "Sakuya_attack4.png", "Sakuya_attack5.png", "Sakuya_attack6.png", "Sakuya_attack7.png"]
    sakuya_start = ["Sakuya_start1.png", "Sakuya_start2.png", "Sakuya_start3.png", "Sakuya_start4.png", "Sakuya_start5.png", "Sakuya_start6.png", "Sakuya_start7.png", "Sakuya_start8.png", "Sakuya_start9.png", "Sakuya_start10.png", "Sakuya_start11.png", "Sakuya_start12.png", "Sakuya_start13.png", "Sakuya_start14.png", "Sakuya_start15.png", "Sakuya_start16.png"]
    marisa_idle = ["Marisa_idle1.png", "Marisa_idle2.png", "Marisa_idle3.png", "Marisa_idle4.png", "Marisa_idle5.png", "Marisa_idle6.png", "Marisa_idle7.png", "Marisa_idle8.png", "Marisa_idle9.png", "Marisa_idle10.png"]
    marisa_attack = ["Marisa_attack_2_1.png", "Marisa_attack_2_2.png", "Marisa_attack_2_3.png", "Marisa_attack_2_4.png", "Marisa_attack_2_5.png", "Marisa_attack_2_6.png", "Marisa_attack_2_7.png"]
    marisa_start = ["Marisa_start1.png", "Marisa_start2.png", "Marisa_start3.png", "Marisa_start4.png", "Marisa_start5.png", "Marisa_start6.png", "Marisa_start7.png", "Marisa_start8.png", "Marisa_start9.png", "Marisa_start10.png", "Marisa_start11.png"]
    remilia_idle = ["Remilia_idle1.png", "Remilia_idle2.png", "Remilia_idle3.png", "Remilia_idle4.png", "Remilia_idle5.png", "Remilia_idle6.png", "Remilia_idle7.png", "Remilia_idle8.png"]
    remilia_attack = ["Remilia_attack1.png", "Remilia_attack2.png", "Remilia_attack3.png", "Remilia_attack4.png", "Remilia_attack5.png", "Remilia_attack6.png", "Remilia_attack7.png", "Remilia_attack8.png"]
    remilia_start = ["Remilia_start1.png", "Remilia_start2.png", "Remilia_start3.png", "Remilia_start4.png", "Remilia_start5.png", "Remilia_start6.png", "Remilia_start7.png", "Remilia_start8.png", "Remilia_start9.png", "Remilia_start10.png"]
    counter_attack = 0
    counter_idle = 0
    counter_start = 0

    def idle(self):
        if self.lvl == 0:
            self.counter_idle += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.sakuya_idle[int(self.counter_idle)]}"), (50, 102))
                
            if self.counter_idle >= len(self.sakuya_idle) - 1:
                self.counter_idle = 0

        if self.lvl == 1:
            self.counter_idle += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.marisa_idle[int(self.counter_idle)]}"), (57, 100))
                
            if self.counter_idle >= len(self.marisa_idle) - 1:
                self.counter_idle = 0
        
        if self.lvl == 2:
            self.counter_idle += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.remilia_idle[int(self.counter_idle)]}"), (119, 111))
                
            if self.counter_idle >= len(self.remilia_idle) - 1:
                self.counter_idle = 0

    def attack(self):
        if self.lvl == 0:
            self.counter_attack += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.sakuya_attack[int(self.counter_attack)]}"), (65, 102))
                    
            if self.counter_attack >= len(self.sakuya_attack) - 1:
                self.counter_attack = 0

        if self.lvl == 1:
            self.counter_attack += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.marisa_attack[int(self.counter_attack)]}"), (65, 102))
                    
            if self.counter_attack >= len(self.marisa_attack) - 1:
                self.counter_attack = 0
            
        if self.lvl == 2:
            self.counter_attack += 0.05
            self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.remilia_attack[int(self.counter_attack)]}"), (112, 123))
                    
            if self.counter_attack >= len(self.remilia_attack) - 1:
                self.counter_attack = 0
    
    def start_anim(self):
        if self.lvl == 0:
            if self.rect.y < 720:
                self.counter_start += 0.045
                self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.sakuya_start[int(self.counter_start)]}"), (95, 125))
            
                if self.counter_start >= len(self.sakuya_start) - 1:
                    self.counter_start = 0

        if self.lvl == 1:
            if self.rect.y < 720:
                self.counter_start += 0.04
                self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.marisa_start[int(self.counter_start)]}"), (107, 125))
            
                if self.counter_start >= len(self.marisa_start) - 1:
                    self.counter_start = 0

        if self.lvl == 2:
            if self.rect.y < 720:
                self.counter_start += 0.04
                self.image = transform.scale(image.load(f"Fumo Hero/sprites/{self.remilia_start[int(self.counter_start)]}"), (126, 122))
            
                if self.counter_start >= len(self.remilia_start) - 1:
                    self.counter_start = 0


    def update(self):
        global music
        global background
        global game
        global round_over
        if Bad_Fumo.enemy_health <= 0 :
            round_over = True
            if self.start_time is None:  # Перевіряємо, чи ще не ініціалізовано start_time
                self.start_time = time.get_ticks()
            # Викликаємо створення предметів після смерті
            items.create_item_bomb()
            items.create_item_health()

            # Встановлюємо позицію боса в "далеко" після його смерті
            Bad_Fumo.rect.x = 10000000

        if round_over:
            current_time = time.get_ticks()  # Отримуємо поточний час в мілісекундах
            elapsed_time = current_time - self.start_time  # Різниця в мілісекундах
            if elapsed_time >= 5000:
                self.end_time = time.get_ticks()
                game = "round_over"


        
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

        if self.lvl == 0:
            self.bullet_image = "Fumo Hero/sprites/Bullet.png"
            Enemy.size = (20, 36)
        if self.lvl == 1:
            if music == 'Fumo Hero/sounds/Sakuya_music.mp3':
                background = transform.scale(image.load("Fumo Hero/sprites/Marisa_bg.jpg"), (900, 720))
                music = 'Fumo Hero/sounds/Marisa_music.mp3'
                mixer.music.load(music)
                mixer.music.play(-1)
                self.bullet_image = "Fumo Hero/sprites/Marisa_bullet.png"
                Enemy.size = (32, 32)
        if self.lvl == 2: 
            self.bullet_image = "Fumo Hero/sprites/Remilia_bullet.png"
            Enemy.size = (24, 30)


    def none(self):
        None

    def Bad_fumo_fight(self):
        global random_number
        if 110 < self.enemy_health :
            self.start_anim()
            self.current_pattern_index = 10
            self.direction = "up"
            if self.rect.y <= 64:
                self.enemy_health = 100
                self.direction = "right"

        elif self.enemy_health <= 100:
            self.attack()
            self.current_pattern_index = random_number
            if self.rect.x > win_width - 100:
                self.direction = "left"
            if self.rect.x < 100:
                self.direction = "right"
        
        if 60 <= self.enemy_health <= 75:
            self.idle()
            random_number = random.randint(0, 9)
            self.current_pattern_index = 10
            self.speed = 0
            
        if 35 <= self.enemy_health <= 60:
            self.attack()
            self.speed = 2
            self.current_pattern_index = random_number
            if self.rect.x > win_width - 100:
                self.direction = "left"
            if self.rect.x < 100:
                self.direction = "right"

        if 20 <= self.enemy_health <= 35:
            self.idle()
            random_number = random.randint(0, 9)
            self.current_pattern_index = 10
            self.speed = 0

        if 0 <= self.enemy_health <= 20:
            self.attack()
            self.speed = 2
            self.current_pattern_index = random_number
            if self.rect.x > win_width - 100:
                self.direction = "left"
            if self.rect.x < 100:
                self.direction = "right"


        # Additional patterns can be added here
        # Example: Circle pattern

    def Spiral_pattern(self):
        num_bullets = 10  # Number of bullets in the spiral
        angle_step = 180 / num_bullets  # How much angle to increase for each bullet
        for i in range(num_bullets):
            angle = i * angle_step
            bullet = EnemyBullet(self.bullet_image, self.rect.x + 25, self.rect.y + 25, 2, angle)
            enemy_bullets.append(bullet)


    def V_shape(self):
        angles = [23, 45, 67, 90, 111, 135, 157]
        for angle in angles:
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)

    def Laser_Beam_pattern(self):
        rows = 2
        cols = 3
        bullet_spacing = 100  # Distance between each bullet
        for i in range(rows):
            for j in range(cols):
                bullet_x = self.rect.x + (j - cols // 2) * bullet_spacing
                bullet_y = self.rect.y + (i - rows // 2) * bullet_spacing
                bullet = EnemyBullet(self.bullet_image, bullet_x, bullet_y, 3,90)
                enemy_bullets.append(bullet)
        bullet = EnemyBullet(self.bullet_image, self.rect.x + 25, self.rect.y + 25, 5)
        bullet.angle = 90  # Straight down
        

    def Wave_pattern(self):
        num_bullets = 5
        for i in range(num_bullets):
            angle = 90 + (i * 15 - (num_bullets // 2) * 15)  # Робимо хвилю розширюючою
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)

    def Random_Spray_pattern(self):
        import random
        num_bullets = 8
        for _ in range(num_bullets):
            angle = random.randint(0, 180)  # Випадковий кут
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)

    def Spiral_Expanding_pattern(self):
        num_bullets = 20
        for i in range(num_bullets):
            angle = (i * 18) % 360  # Обертання на 18 градусів кожного разу
            speed = 1 + (i / 5)  # Збільшуємо швидкість поступово
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, speed, angle)
            enemy_bullets.append(bullet)
    def Funnel_pattern(self):
        num_bullets = 5
        for i in range(num_bullets):
            angle = 15 * i
            distance = 50 + (i * 10)
            bullet_x = self.rect.centerx + distance * math.cos(math.radians(angle))
            bullet_y = self.rect.centery + distance * math.sin(math.radians(angle))
            bullet = EnemyBullet(self.bullet_image, bullet_x, bullet_y, 2, angle)
            enemy_bullets.append(bullet)


    def Diagonal_Rain_pattern(self):
        num_bullets = 10
        for i in range(num_bullets):
            angle = 45 + (i * 10)
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)
            angle = 135 + (i * 10)
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 2, angle)
            enemy_bullets.append(bullet)

    def Explosive_Radial_pattern(self):
        num_bullets = 16
        for i in range(num_bullets):
            angle = (i * 360 / num_bullets)
            bullet = EnemyBullet(self.bullet_image, self.rect.centerx, self.rect.centery, 4, angle)
            enemy_bullets.append(bullet)

    def Concentric_Circles_pattern(self):
        num_bullets = 10
        for i in range(3):
            radius = 30 * (i + 1)
            for j in range(num_bullets):
                angle = (j * 360 / num_bullets)
                bullet_x = self.rect.centerx + radius * math.cos(math.radians(angle))
                bullet_y = self.rect.centery + radius * math.sin(math.radians(angle))
                bullet = EnemyBullet(self.bullet_image, bullet_x, bullet_y, 2, angle)
                enemy_bullets.append(bullet)
    

    patterns = [V_shape, Spiral_pattern, Laser_Beam_pattern, Wave_pattern, Random_Spray_pattern, Spiral_Expanding_pattern, Funnel_pattern, Diagonal_Rain_pattern, Explosive_Radial_pattern, Concentric_Circles_pattern, none]

    def draw_hp_bar(self, max_health, enemy_health):
        draw.rect(screen, (255,0,0), (50, 25, win_width - 100, 20))
        
        draw.rect(screen, (0,255,0), (50, 25, (enemy_health / max_health) * (win_width - 100), 20))
    
    def hp_del(self):
        self.enemy_health -= 1

    def draw_hp_bar(self, max_health, enemy_health):
        draw.rect(screen, (255,0,0), (50, 25, win_width - 100, 20))
        
        draw.rect(screen, (0,255,0), (50, 25, (enemy_health / max_health) * (win_width - 100), 20))
    
    def hp_del(self):
        self.enemy_health -= 1
        
def show_end_menu(elapsed_time):
    text = font.render(f"Ви пройшли рівень за {elapsed_time / 1000:.2f} секунд!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))  # Розміщуємо текст по центру екрану
    screen.blit(text, text_rect)

    instructions = font.render("Натисніть Enter для продовження", True, (255, 255, 255))
    instructions_rect = instructions.get_rect(center=(400, 350))  # Знову розміщаємо по центру
    screen.blit(instructions, instructions_rect)
    display.flip()

def restart_game():
    global start_time_game
    global round_over
    global game
    game = "game"
    Enemy.lvl += 1
    start_time_game = time.get_ticks()
    end_time = None
    Bad_Fumo.rect.x = win_width / 2
    Bad_Fumo.rect.y = 1000
    Bad_Fumo.enemy_health = 1000
    round_over = False


Fumo_destroyer = Player('Fumo Hero/sprites/Cirno0.png', (win_width / 2) - 65, win_height - 160, 4, 64,64)
Fumo_destroyer_hitbox = GameSprite('Fumo Hero/sprites/hitbox.png', Fumo_destroyer.rect.x, Fumo_destroyer.rect.y, 4, 16, 16)

Bad_Fumo = Enemy('Fumo Hero/sprites/Cirno9.webp', (win_width / 2) -50, 1000, 2, 50,102, 1000, 100)

clock = time.Clock()
frames = 144

last_hit_health_time = 0
hit_health_delay = 2000

btn_play = GameSprite("Fumo Hero/sprites/button_play.png", 260, 80, 0, 320, 132) #transform.scale(image.load("Fumo Hero/button_play.png"), (192, 80))

btn_exit = GameSprite("Fumo Hero/sprites/button_exit.png", 260, 280, 0, 320, 132)#transform.scale(image.load("Fumo Hero/button_exit.png"), (192, 80))

btn_settings = GameSprite("Fumo Hero/sprites/button_settings.png", 260, 492, 0, 320, 132)#transform.scale(image.load("Fumo Hero/Button_settings.png"), (192, 92))

btn_sound = GameSprite("Fumo Hero/sprites/button_sound.png", 102, 280, 0, 150, 140)

btn_back = GameSprite("Fumo Hero/sprites/button_back.png", 5, 10, 0, 320, 132)

start_time_game = None
game = "menu"
running = True
mute = False
while running:
    counter_time += 1
    current_time = time.get_ticks()

    for e in event.get():
        Fumo_destroyer.use_bomb()

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
        if e.type == KEYDOWN:
            if e.key == K_RETURN and round_over == True:
                restart_game() 


    if game == "round_over":
        
        screen.blit(background, (0,0))
        elapsed_time = current_time - start_time_game
        show_end_menu(elapsed_time)
        



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
        if start_time_game is None:  # Перевіряємо, чи ще не ініціалізовано start_time
            start_time_game = time.get_ticks()
        if music == 'Fumo Hero/sounds/bgm.ogg':
            music = 'Fumo Hero/sounds/Sakuya_music.mp3'
            mixer.music.load(music)
            mixer.music.play(-1)
            

        if mute == True:
            mixer.music.load("Fumo Hero/Sounds/baka-cirno.mp3")

        screen.blit(background, (0, 0))
        Fumo_destroyer.reset()
        Fumo_destroyer_hitbox.reset()
        Fumo_destroyer.update()
        Fumo_destroyer.idle()
        Fumo_destroyer.move_right()
        Fumo_destroyer.move_left()
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