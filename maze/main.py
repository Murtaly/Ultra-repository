from pygame import *
mixer.init()

screen = display.set_mode((1000, 700))

display.set_caption("Cool Maze")

background = transform.scale(image.load("maze/field.jpg"), (1000, 700))

screen.blit(background, (0, 0))

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
        screen.blit(player, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

win_width = 1200
win_height = 700

player = Player('maze/kostichka.jpg', 5, win_height - 80, 4)
monster = Enemy('maze/spider.png', win_width - 80, 280, 2)
final = GameSprite('maze/big booty black man.webp', win_width - 120, win_height - 80, 0)
wall1 = Wall(20, 20, 20, 250, 0, 50, 400)
wall2 = Wall(20, 20, 20, 400, 220, 300, 50)
wall3 = Wall(20, 20, 20, 400, 350, 220, 50)
wall4 = Wall(20, 20, 20, 700, 220, 50, 180)
wall5 = Wall(20, 20, 20, 300, 0, 200, 50)

clock = time.Clock()

FPS = 60

finish = False
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if finish != True:
        screen.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        


    display.update()
    clock.tick(FPS)