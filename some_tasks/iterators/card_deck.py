class CardDeck:
    def __init__(self):
        self.len = 51
        self.suits = {0: 'Черви', 1: 'Буби', 2: 'Пик', 3: 'Крести'}

    def __iter__(self):
        return self

    def __next__(self):
        if self.len == -1:
            raise StopIteration
        else:
            current_suit = self.suits[self.len % 4]
            current_num = 14 - self.len // 4
            self.len -= 1
            return f'{current_num}  {current_suit}'


deck = CardDeck()
a = [a for a in deck]
print(len(a))
print(a)
