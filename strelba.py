import pygame, os, random
from math import sqrt

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
running = True
screen.fill((255, 255, 255))
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("g11.jpg", 1)
    w, h = 100, 100
    image = pygame.transform.scale(image, (w, h))

    def __init__(self, group):
        w, h = 100, 100
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200


class bullet(pygame.sprite.Sprite):
    image = load_image("g11.jpg", 1)

    image = pygame.transform.scale(image, (10, 10))

    def __init__(self, group, xy):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.speed = 1.0
        nx, ny = xy
        self.rast = sqrt((200 - nx) ** 2 + (200 - ny) ** 2)
        sin = (-200 + nx) / sqrt((200 - nx)**2 + (200 - ny)**2)
        cos = (-200 + ny) / sqrt((200 - nx) ** 2 + (200 - ny) ** 2)
        self.nx, self.ny = round(sin * 50.0), round(cos * 50.0)
        self.pr = 0
        print(1)

    def update(self):
        self.rect.x = self.rect.x + self.nx
        self.rect.y = self.rect.y + self.ny
        self.pr += self.speed
        if self.rast < self.pr:
            return False


clock = pygame.time.Clock()

bomb_image = load_image("car2.png")
bomb_image = pygame.transform.scale(bomb_image, (100, 100))
all_sprites = pygame.sprite.Group()
bul = pygame.sprite.Group()
for _ in range(1):
    Bomb(all_sprites)
gh = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gh = True
            bullet(bul, event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            gh = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    for i in bul:
        if i.update() == False:
            bul.remove(i)
    print(len(bul))
    if not gh:
        ji = 0
    if gh:
        ji += 1
        if ji % 10 == 0:
            bullet(bul, [x, y])

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    bul.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()