class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def show_my_drink(self):
        if self.taste:
            return f'Газировка {self.taste}'
        else:
            return 'Обычная газировка'


soda = Soda()
cool_soda = Soda(taste='апельсиновая')
print(soda.show_my_drink())
print(cool_soda.show_my_drink())
