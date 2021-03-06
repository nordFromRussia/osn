import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, *groops):
        super().__init__(groops)
        self.image = load_image('data/car2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.direction = 1  # 1 - right, -1 - left

    def update(self, *args):
        self.rect.x += 200 / 60 * self.direction
        print(self.rect.x)
        if self.rect.x < 0 or self.rect.x > width - self.image.get_width():
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


pygame.init()
size = width, height = 600, 95

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()
rr = 60
Car(all_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rr = 10
        if event.type == pygame.MOUSEBUTTONUP:
            rr = 60
    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    clock.tick(rr)
    pygame.display.flip()

pygame.quit()