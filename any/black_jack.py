import random

class Card:
    def __init__(self,rank:str, suit:str):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        if self.rank in ['Валет','Дама','Король','Туз']:
            return 10
        else:
            return " 123456789".index(self.rank)

    def get_rank(self):
        return f'{self.suit}{self.rank}'

class DeckCard:
    def __init__(self):
        _rank = ['1','2','3','4','5','6','7','8','9','Валет','Дама','Король','Туз']
        _suit = ['Пика ','Кресть ','Буба ','Червь ']
        self.__cards = [Card(r,s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self):
        return self.__cards.pop()

class Player():
    def __init__(self, name:str)-> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self):
        return f' Карты на руках => {self._hand}; Сумма значений {self.count}'

    @hand.setter
    def hand(self,card:Card):
        self.count += card.get_value()
        self._hand.append(card.get_rank())

class Dealer(Player):
    def get_card(self,cards:DeckCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break
class Game:
    def __init__(self,player_name:str):
        self.cards = DeckCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name='Dealer')

    def print(self):
        return f'\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}'

    def check_count(self):
        if self.player.count > 21:
            print(f'Вы проиграли', self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f'Вы победили!', self.print())
        elif self.dealer.count == self.player.count:
            print(f'Ничья', self.print())
        elif self.dealer.count > self.player.count:
            print(f'Вы проиграли', self.print())
        elif self.dealer.count < self.player.count:
            print(f'Вы победили!', self.print())


    def start(self):
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)

        while self.player.count < 21:
            answer = input('Желаете взять еще карту? y/n')
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_card(self.cards)
                break
        self.check_count()


def main():
    name = input('Ваше имя')
    game = Game(name)
    game.start()

main()
