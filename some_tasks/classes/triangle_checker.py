class MyTriangleChecker:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_triangle(self):
        is_int = True
        is_num = True
        is_good = False
        for key, value in self.__dict__.items():
            if not isinstance(value, int):
                is_int = False
            else:
                if value < 0:
                    is_num = False
        if is_num and is_int:
            if self.x + self.y > self.z or self.y + self.z > self.x or self.z + self.x > self.y:
                is_good = True


        if is_num and is_int and is_good:
            print('Можно построить треугольник!')
        elif not is_num:
            print('Отрицательные нельзя')
        elif not is_int:
            print('Параметры должны быть числами')
        else:
            print('построить треугольник нельзя')


class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

t = TriangleChecker([1, 2, 3])
t2 = TriangleChecker([1, 2, -3])
t3 = TriangleChecker([1, '2', 3])
t4 = TriangleChecker([1, 2, 100])
t.is_triangle()
t2.is_triangle()
t3.is_triangle()
t4.is_triangle()