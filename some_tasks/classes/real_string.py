from functools import total_ordering


@total_ordering
class RealString(str):
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.string) == len(other)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.string) < len(other)


r = RealString('Apple')
print(r > 'Яблоко')

print('Молоко' < 'Абрикосы')
print(RealString('Молоко') < RealString('Абрикосы'))
