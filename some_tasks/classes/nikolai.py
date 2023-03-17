class Nikola(object):
    __slots__ = ['__name', '__age']

    def __init__(self, name, age):
        self.__name = None
        self.__age = age
        self.name = name

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
# n.www = '231'
n.name = 'John'
print(n)
