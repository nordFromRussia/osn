import os
import sys
import pygame
from math import sqrt

pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# Загрузка изображения
def load_image(name, re=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image



# Создание карабля
spase_ship = pygame.sprite.Group()
bomb_image = load_image("ufo.png")
bomb_image = pygame.transform.rotozoom(bomb_image,16,1)
bomb_image = pygame.transform.scale(bomb_image, (70, 70))

bomb = pygame.sprite.Sprite(spase_ship)

bomb.image = bomb_image
bomb.rect = bomb.image.get_rect()
bomb.rect.x = 0
bomb.rect.y = 0


# Передвижение карабля
def strelka(peremeh_y, peremeh_x):
    new_x = bomb.rect.x + peremeh_x
    new_y = bomb.rect.y + peremeh_y
    if new_x < 0 or new_y < 0 or new_x > width or new_y > height:
        return None
    if new_x + 70 < 0 or new_y + 70 < 0 or new_x + 70 > width or new_y + 70 > height:
        return None
    bomb.rect.x = new_x
    bomb.rect.y = new_y


# Класс пуль
class osteroid(pygame.sprite.Sprite):
    image = load_image("g11.jpg", 1)

    image = pygame.transform.scale(image, (10, 10))

    def __init__(self, x, y, group, xy):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = bullet.image
        self.rect = self.image.get_rect()

        # начальные кординаты пули
        self.rect.x = x + 35
        self.rect.y = y + 35

        # её скорость
        self.speed = 30.0

        # кординаты мыши
        nx, ny = xy

        # синус и косинус
        sin = (-x + nx) / sqrt((x - nx) ** 2 + (y - ny) ** 2)
        cos = (-y + ny) / sqrt((x - nx) ** 2 + (y - ny) ** 2)

        # перемешение по икс и игрик
        self.nx, self.ny = round(sin * 10.0), round(cos * 10.0)
        self.pr = 0

        print(1)


# Класс пуль
class bullet(pygame.sprite.Sprite):
    image = load_image("g11.jpg", 1)

    image = pygame.transform.scale(image, (10, 10))

    def __init__(self, x ,y, group, xy):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = bullet.image
        self.rect = self.image.get_rect()

        # начальные кординаты пули
        self.rect.x = x + 35
        self.rect.y = y + 35

        # её скорость
        self.speed = 30.0

        # кординаты мыши
        nx, ny = xy

        # синус и косинус
        sin = (-x + nx) / sqrt((x - nx)**2 + (y - ny)**2)
        cos = (-y + ny) / sqrt((x - nx) ** 2 + (y - ny) ** 2)

        # перемешение по икс и игрик
        self.nx, self.ny = round(sin * 10.0), round(cos * 10.0)
        self.pr = 0

        print(1)

    def update(self):
        self.rect.x = self.rect.x + self.nx
        self.rect.y = self.rect.y + self.ny

        self.pr += self.speed

        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > width or self.rect.y > height:
            return False


vv = False
vn = False

x, y = 0, 0

pr = False
lev = False
rabota = True
zagim = False

bul = pygame.sprite.Group()

oster = pygame.sprite.Group()

dlitelnost = 0

while rabota:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rabota = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vv = True

            if event.key == pygame.K_DOWN:
                vn = True

            if event.key == pygame.K_LEFT:
                pr = True

            if event.key == pygame.K_RIGHT:
                lev = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                vv = False

            if event.key == pygame.K_DOWN:
                vn = False

            if event.key == pygame.K_LEFT:
                pr = False

            if event.key == pygame.K_RIGHT:
                lev = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            zagim = True
            bullet(bomb.rect.x,bomb.rect.y,bul, event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            zagim = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    if vv:
        verh = -3
    else:
        verh = 0

    if vn:
        vniz = 3
    else:
        vniz = 0

    if pr:
        vrpr = -3
    else:
        vrpr = 0

    if lev:
        vlev = 3
    else:
        vlev = 0

    for i in bul:
        if i.update() == False:
            bul.remove(i)

    print(len(bul))

    if not zagim:
        dlitelnost = 0

    if zagim:
        dlitelnost += 1
        if dlitelnost % 10 == 0:
            bullet(bomb.rect.x, bomb.rect.y, bul, [x, y])

    osteroid(200, 200, oster, [0 , 0])
    strelka(verh + vniz, vrpr + vlev)
    if pygame.sprite.spritecollideany(bomb, oster):
        rabota = False
    oster.draw(screen)
    bul.draw(screen)
    spase_ship.draw(screen)
    pygame.display.flip()
    screen.fill(pygame.Color('black'))
    clock.tick(100)
