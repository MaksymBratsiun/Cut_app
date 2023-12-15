class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = None
        self.y = None


def place_rectangles(rectangles, container_width, container_height):
    # Сортуємо прямокутники в порядку спадання їх площі
    rectangles.sort(key=lambda r: r.width * r.height, reverse=True)

    # Створюємо список для зберігання координат розташування прямокутників
    coordinates = [(0, 0)]

    for rect in rectangles:
        for x, y in coordinates:
            print(coordinates)
            if x + rect.width <= container_width and y + rect.height <= container_height:
                # Якщо прямокутник поміщається в поточному місці, додаємо його координати
                rect.x = x
                rect.y = y
                coordinates.remove((x, y))
                # Додаємо нові координати для подальших розташувань
                coordinates.append((x + rect.width, y))
                coordinates.append((x, y + rect.height))
                coordinates.append((x + rect.width, y + rect.height))
                break
        else:
            # Якщо прямокутник не може бути розміщений вже існуючими, додаємо нові координати
            rect.x = 0
            rect.y = 0
            coordinates.append((0, rect.height))
            coordinates.append((rect.width, 0))
            print('new sheet', coordinates)


if __name__ == "__main__":
    # Приклад використання
    r1 = Rectangle(4, 2)
    r2 = Rectangle(2, 3)
    r3 = Rectangle(3, 1)
    r4 = Rectangle(1, 2)
    r5 = Rectangle(3, 2)
    r6 = Rectangle(3, 1)

    rectangles = [r1, r2, r3, r4, r5, r6]

    container_width = 5
    container_height = 5

    place_rectangles(rectangles, container_width, container_height)

    for rect in rectangles:
        print(f"Rectangle ({rect.width}x{rect.height}) at ({rect.x}, {rect.y})")