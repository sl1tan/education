class MyIterator:
    def __init__(self, first_num, stream):
        """first_num - число относительно которого начнется отсчет
            stream = 1/-1 указывает направление следующего числа
        """
        self.__first_num = first_num
        self.__stream = stream

    def __iter__(self):
        return self

    def __next__(self):
        self.__first_num = self.__first_num + 1 * self.__stream
        return self.__first_num


if __name__ == '__main__':
    iterator = MyIterator(3, 1)
    print(next(iterator))
    for x in range(5):
        print(next(iterator))
