import pygame


class Enemy(pygame.sprite.Sprite):
    
    HP = 100
    damage = 10
    width = 50
    height = 50
    x = 100
    y = 100
    image = ""
    surface = ""
    rect = ""
 
    def __init__(self, image, width=50,height=50, x=100,y=100, damage=10):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.damage = damage
        self.surface = pygame.image.load(image)

        # Меняем размер изображения
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))

        self.rect = self.surface.get_rect(center=(x,y))

    def draw(self,screen:pygame.Surface):
        self.rect.center = (self.x, self.y)
        screen.blit(self.surface,self.rect)
    def follow(self, player, speed=2):
            # Вычисляем разницу координат между врагом и игроком
            dx = player.x - self.x
            dy = player.y - self.y
            
            # Нормируем вектор движения
            distance = (dx**2 + dy**2) ** 0.5
            if distance > 0:
                dx /= distance
                dy /= distance
            
            # Двигаем врага в направлении игрока
            self.x += dx * speed
            self.y += dy * speed


        