import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Школьная анимация')

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
SKY_BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Загрузка логотипа (путь к изображению логотипа)
try:
    school_logo = pygame.image.load('D:\Zona Downloads\sf.jpg')  # Путь к логотипу школы
    school_logo = pygame.transform.scale(school_logo, (150, 150))  # Масштабируем логотип
except pygame.error as e:
    print(f"Ошибка загрузки логотипа: {e}")
    sys.exit()

# Школьное здание
class SchoolBuilding:
    def __init__(self):
        self.x = window_width // 2 - 150
        self.y = window_height - 300  # Здание будет стоять на земле
        self.width = 300
        self.height = 200
        self.color = (200, 200, 255)  # Светлый цвет для здания

    def draw(self, window):
        # Рисуем само здание
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

        # Крыша (многоугольник, создаем треугольник)
        pygame.draw.polygon(window, (150, 75, 0), [(self.x - 20, self.y),
                                                   (self.x + self.width + 20, self.y),
                                                   (self.x + self.width // 2, self.y - 50)])

        # Окна
        pygame.draw.rect(window, WHITE, (self.x + 50, self.y + 50, 50, 50))  # Левое окно
        pygame.draw.rect(window, WHITE, (self.x + 200, self.y + 50, 50, 50))  # Правое окно

        # Дверь
        pygame.draw.rect(window, (150, 75, 0), (self.x + 120, self.y + 100, 60, 100))  # Дверь

# Падающие школьные принадлежности
class SchoolItem:
    def __init__(self, item_type):
        self.x = random.randint(0, window_width)
        self.y = random.randint(-50, -10)
        self.size = random.randint(10, 20)
        self.speed = random.uniform(1, 3)
        self.item_type = item_type
        self.angle = random.uniform(-0.1, 0.1)  # Плавное вращение

    def update(self):
        self.y += self.speed  # Обновляем позицию вниз
        self.x += self.angle  # Слегка отклоняется в стороны
        if self.y > window_height:  # Когда предмет выходит за пределы окна
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, window_width)

    def draw(self, window):
        # Рисуем в зависимости от типа предмета
        if self.item_type == 'pencil':
            pygame.draw.rect(window, YELLOW, (self.x, self.y, self.size, self.size // 2))  # Карандаш
        elif self.item_type == 'book':
            pygame.draw.rect(window, BROWN, (self.x, self.y, self.size, self.size))  # Книга
        elif self.item_type == 'ruler':
            pygame.draw.rect(window, GREEN, (self.x, self.y, self.size, self.size // 5))  # Линейка

# Флаг школы
class SchoolFlag:
    def __init__(self):
        self.x = window_width // 2 - 40
        self.y = window_height - 350  # Поднимем флаг на верх здания
        self.width = 80
        self.height = 40
        self.color = RED  # Начальный цвет флага (красный)

    def update(self):
        # Мигаем флагом
        if random.random() < 0.02:  # С вероятностью 2% меняем цвет флага
            self.color = RED if self.color == YELLOW else YELLOW

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))  # Рисуем флаг

# Деревья на школьном дворе
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trunk_height = 50
        self.trunk_width = 20
        self.foliage_radius = 40

    def draw(self, window):
        # Ствол дерева
        pygame.draw.rect(window, BROWN, (self.x - self.trunk_width // 2, self.y, self.trunk_width, self.trunk_height))
        # Листья
        pygame.draw.circle(window, GREEN, (self.x, self.y - 40), self.foliage_radius)

# Создание падающих предметов
school_items = [SchoolItem(random.choice(['pencil', 'book', 'ruler'])) for _ in range(50)]  # 50 падающих предметов

# Создание флага
school_flag = SchoolFlag()

# Создание дерева на школьном дворе
trees = [Tree(random.randint(50, window_width - 50), window_height - 120) for _ in range(3)]

# Школьное здание
school_building = SchoolBuilding()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона (голубое небо и зелёная трава или школьный фон)
    window.fill(SKY_BLUE)
    pygame.draw.rect(window, GREEN, (0, window_height - 100, window_width, 100))  # Трава

    # Отображение школьного здания
    school_building.draw(window)

    # Отображение логотипа в левом верхнем углу
    window.blit(school_logo, (10, 10))  # Позиция логотипа в левом верхнем углу

    # Обновление и отрисовка предметов
    for item in school_items:
        item.update()
        item.draw(window)

    # Обновление и отрисовка флага
    school_flag.update()
    school_flag.draw(window)

    # Отображение деревьев
    for tree in trees:
        tree.draw(window)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)

# Завершение работы
pygame.quit()
sys.exit()
