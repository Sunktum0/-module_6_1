class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        # Вызываем метод класса Plant для проверки, является ли пища съедобной
        if food.is_edible():
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    # Определяем атрибут edible на уровне класса
    edible = False

    def __init__(self, name):
        self.name = name

    def is_edible(self):
        return self.edible

class Mammal(Animal):
    pass  # Наследуем поведение от Animal

class Predator(Animal):
    pass  # Наследуем поведение от Animal

class Flower(Plant):
    pass  # Наследуем поведение от Plant

class Fruit(Plant):
    # Переопределяем атрибут edible на уровне класса
    edible = True

    def __init__(self, name):
        super().__init__(name)

# Создание экземпляров классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов и вызов метода eat
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)  # Волк пробует есть цветок (не съедобный)
a2.eat(p2)  # Хатико ест фрукт (съедобный)
print(a1.alive)
print(a2.fed)