class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new = range(new_floor)
        if self.number_of_floors < new_floor:
            print("Ошибка")
        else:
            for i in new:
                print(i)
                if (i + 1) == new_floor:
                    print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название:{self.name} , кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if type(value) == int:
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        value + self.number_of_floors
        return self

h1 = House("ЖК Кифир", 10)
h2 = House("ЖК Дыра", 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
