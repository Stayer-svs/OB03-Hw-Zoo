# 1. Создать базовый класс `Animal`, который будет содержать общие атрибуты (например,
# `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализовать наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют
# от класса `Animal`. Добавить специфические атрибуты и переопределить методы, если требуется
# (например, различный звук для `make_sound()`).
# 3. Продемонстрировать полиморфизм: создать функцию `animal_sound(animals)`, которая принимает список
# животных и вызывает метод `make_sound()` для каждого животного.
# 4. Использовать композицию для создания класса `Zoo`, который будет содержать информацию о животных и
# сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создать классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Добавить дополнительные функции в программу, такие как сохранение информации о зоопарке в файл и
# возможность её загрузки, чтобы у «Зоопарка» было "постоянное состояние" между запусками программы.

# Создаем базовый класс Animal
class Animal:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def make_sound(self):   # Звук животного

        return "Звук издаваемый животным (Some generic animal sound)"

    def eat(self):      # Процесс еды

        return f"{self.name} is eating (ест)"

    def to_string(self):    # Преобразуем информацию о животном в строку для сохранения в файл

        return f"{self.__class__.__name__},{self.name},{self.age}"

# Создаем дочерний класс Bird (Птица) - наследник класса Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span): # название, возраст, размах крыльев

        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.wing_span = wing_span

    def make_sound(self):   # издает звук птицы

        return "карр (cawing)"

    def to_string(self):    # преобразуем информацию о птице в строку для сохранения в файл

        return f"{super().to_string()},{self.wing_span}"

# Создаем дочерний класс Mammal (Млекопитающих) - наследник класса Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color): # название, возраст, цвет шерсти млекопитающего

        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self): # млекопитающее издает звук

        return "рычание (Roar)"

    def to_string(self):    # преобразуем информацию о млекопитающем в строку для сохранения в файл

        return f"{super().to_string()},{self.fur_color}"

# Создаем дочерний класс Reptile (Рептилия) - наследник класса Animal
class Reptile(Animal):
    def __init__(self, name, age, is_venomous): # наименование, возраст, ядовитая ли (True или False) рептилия

        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):   # рептилия издает звук

        return "шипение (Hiss)"

    def to_string(self):    # преобразуем информацию о рептилии в строку для сохранения в файл

        return f"{super().to_string()},{self.is_venomous}" #

def animal_sound(animals):  # демонстрирует полиморфизм: вызывает метод make_sound() для
                            # каждого животного в списке.
                            # параметр animals - список объектов класса Animal или его подклассов.

    for animal in animals:
        print(f"{animal.name} произносит : {animal.make_sound()}")

# Создаем класс Zoo - инициализируем списки для хранения животных и персонала
class Zoo:
    def __init__(self):

        self.animals = []
        self.staff = []

    def add_animal(self, animal):   # добавляет животное в "Зоопарк"

        self.animals.append(animal) # animal - объект класса Animal или его подкласса

    def add_staff(self, staff_member):  # добавляет сотрудника в "Зоопарк"

        self.staff.append(staff_member) # staff_member - объект класса ZooKeeper или Veterinarian

    def save_to_file(self, filename): # Сохраняет информацию о зоопарке (животных и персонале) в файл.
                                      # filename - имя файла для сохранения данных.

        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(animal.to_string() + '\n')
            for staff in self.staff:
                file.write(staff.to_string() + '\n')

    @staticmethod
    def load_from_file(filename):   # Загружает информацию о зоопарке из файла.
                                    # filename - имя файла для загрузки данных.

        zoo = Zoo()         # Объект класса Zoo, содержащий загруженные данные
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                class_name = data[0]
                if class_name == "Bird":
                    animal = Bird(data[1], int(data[2]), float(data[3]))
                    zoo.add_animal(animal)
                elif class_name == "Mammal":
                    animal = Mammal(data[1], int(data[2]), data[3])
                    zoo.add_animal(animal)
                elif class_name == "Reptile":
                    animal = Reptile(data[1], int(data[2]), data[3] == 'True')
                    zoo.add_animal(animal)
                elif class_name == "ZooKeeper":
                    staff = ZooKeeper(data[1])
                    zoo.add_staff(staff)
                elif class_name == "Veterinarian":
                    staff = Veterinarian(data[1])
                    zoo.add_staff(staff)
        return zoo

# создаем класс ZooKeeper (Смотритель). name - имя смотрителя зоопарка
class ZooKeeper:
    def __init__(self, name):

        self.name = name

    def feed_animal(self, animal):  # Описывает процесс кормления животного. animal - объект класса Animal

        return f"{self.name} кормит {animal.name}"

    def to_string(self): # Преобразует информацию о смотрителе в строку для сохранения в файл

        return f"{self.__class__.__name__},{self.name}" # информация о смотрителе

# создаем класс Veterinarian (Ветеринар). name - имя ветеринара зоопарка
class Veterinarian:
    def __init__(self, name):

        self.name = name

    def heal_animal(self, animal): # описывает процесс лечения животного. animal - объект класса Animal

        return f"{self.name} лечит {animal.name}" # информация о процессе лечения

    def to_string(self): # Преобразует информацию о ветеринаре в строку для сохранения в файл

        return f"{self.__class__.__name__},{self.name}"

if __name__ == "__main__":
    # Создание экземпляров животных
    crow = Bird("crow (ворон)", 2, 0.9)
    lion = Mammal("lion (лев)", 5, "желто-серый")
    snake = Reptile("cobra (кобра)", 3, True)

    # Создание экземпляров сотрудников
    keeper = ZooKeeper("смотритель Васильев")
    vet = Veterinarian("ветеринар Иванов")

    # Создание зоопарка и добавление животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(crow)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Демонстрация взаимодействия сотрудников с животными
    print(keeper.feed_animal(lion))
    print(vet.heal_animal(snake))

    # Сохранение и загрузка данных о зоопарке
    zoo.save_to_file("zoo_data.txt")
    loaded_zoo = Zoo.load_from_file("zoo_data.txt")
    print(f"Loaded zoo has {len(loaded_zoo.animals)} animals and {len(loaded_zoo.staff)} staff members.")