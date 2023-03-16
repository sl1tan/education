class Nikola:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if other == 'Николай':
            self.__name = other
        else:
            self.__name = f'Я не {other}, я Николай'

    def __str__(self):
        return f'Name: {self.__name}\nAge: {self.__age}'

n = Nikola('oleg', 20)
print(n)
