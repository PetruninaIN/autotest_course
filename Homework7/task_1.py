# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код
import math

class Segment:
    def __init__(self, point1, point2):
        """
        Инициализация отрезка по двум точкам.
        :param point1: кортеж (x1, y1) — первая точка
        :param point2: кортеж (x2, y2) — вторая точка
        """
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def length(self):
        """
        Возвращает длину отрезка с округлением до 2 знаков после запятой.
        :return: float — длина отрезка
        """
        length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return round(length, 2)

    def x_axis_intersection(self):
        """
        Проверяет, пересекает ли отрезок ось абсцисс (OX).
        Отрезок пересекает OX, если точки лежат по разные стороны от оси (y1 * y2 <= 0),
        но не обе лежат на оси (y1 != 0 или y2 != 0).
        :return: bool — True, если пересекает, иначе False
        """
        # Точки лежат по разные стороны от OX или одна из них на оси
        if self.y1 * self.y2 <= 0:
            # Исключаем случай, когда обе точки лежат на оси OX
            if not (self.y1 == 0 and self.y2 == 0):
                return True
        return False

    def y_axis_intersection(self):
        """
        Проверяет, пересекает ли отрезок ось ординат (OY).
        Отрезок пересекает OY, если точки лежат по разные стороны от оси (x1 * x2 <= 0),
        но не обе лежат на оси (x1 != 0 или x2 != 0).
        :return: bool — True, если пересекает, иначе False
        """
        # Точки лежат по разные стороны от OY или одна из них на оси
        if self.x1 * self.x2 <= 0:
            # Исключаем случай, когда обе точки лежат на оси OY
            if not (self.x1 == 0 and self.x2 == 0):
                return True
        return False

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
