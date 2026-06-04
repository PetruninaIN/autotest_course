# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код

from collections import Counter

class PersonInfo:
    def __init__(self, full_name, age, *departments):
        """
        Инициализация сотрудника.
        :param full_name: строка 'Имя Фамилия'
        :param age: возраст сотрудника (число)
        :param departments: подразделения от головного до текущего (переменное количество аргументов)
        """
        self.full_name = full_name
        self.age = age
        self.departments = departments

    def short_name(self):
        """
        Возвращает строку в формате 'Фамилия И.'
        :return: str — сокращённое имя
        """
        name_parts = self.full_name.split()
        first_name = name_parts[0]  # Имя
        last_name = name_parts[1]  # Фамилия
        initial = first_name[0].upper()  # Инициал имени с заглавной буквы
        return f"{last_name} {initial}."

    def path_deps(self):
        """
        Возвращает путь подразделений в формате
        'Головное подразделение --> ... --> Конечное подразделение'
        :return: str — путь подразделений
        """
        return " --> ".join(self.departments)

    def new_salary(self):
        """
        Вычисляет новую зарплату по формуле:
        1337 * Возраст * суммарное кол-во вхождений трёх наиболее часто встречающихся букв
        из списка подразделений (регистр имеет значение).
        :return: int — новая зарплата
        """
        # Объединяем все подразделения в одну строку
        all_text = "".join(self.departments)

        # Считаем частоту каждой буквы
        letter_counts = Counter(all_text)

        # Получаем три наиболее частые буквы и их частоты
        top_three = letter_counts.most_common(3)

        # Суммируем частоты трёх самых частых букв
        sum_top_three = sum(count for letter, count in top_three)

        # Вычисляем зарплату по формуле
        salary = 1337 * self.age * sum_top_three

        return salary


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
