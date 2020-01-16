from random import shuffle
from time import sleep
OPENING_MESSAGE = """
__________________________________
開発するブラックジャックのルール
1.  初期カードは52枚。
2.  引く際にカードの重複は無いようにする。
3.  プレイヤーとディーラーの2人対戦。
4.  プレイヤーは実行者、ディーラーは自動的に実行。
5.  実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。
    引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
6.  その後、先にプレイヤーがカードを引く。
    プレイヤーが21を超えていたら、その時点でゲーム終了
7.  プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
8.  プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
9.  プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
10. JとQとKは10として扱う
11. Aは「1」として扱う。
__________________________________
"""
def game():
    print(OPENING_MESSAGE)
    sleep(1)
game()

SUIT = {
    1: '♡',
    2: '♤',
    3: '♢',
    4: '♧'
}

RANK = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}


class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.deck.append(suit*100 + rank)
        shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()


class Participant:
    def __init__(self, name):
        self.name = name
        self.rank = []
        self.draw_card_history = []

    def get_sum(self):
        return sum(self.rank)

    def get_suit_rank(self, card):
        num_suit = card // 100
        num_rank = card % 100
        display_suit = SUIT[num_suit]
        display_rank = RANK.get(num_rank, str(num_rank))
        return num_suit, num_rank, display_suit, display_rank

    def set_hand(self, card, *, display=True):
        _, num_rank, display_suit, display_rank = self.get_suit_rank(card)
        if display:
            print('{} の引いたカードは {} の {} です'.format(self.name, display_suit, display_rank))
        else:
            print('{} の引いたカードはわかりません'.format(self.name))
        self.rank.append(min(num_rank, 10))
        self.draw_card_history.append(card)

    def over_twenty_one(self):
        if sum(self.rank) > 21:
            return True
        return False

    def display_suit_rank(self, n):
        card = self.draw_card_history[n-1]
        _, _, display_suit, display_rank = self.get_suit_rank(card)
        print('{} が引いた {} 枚目のカードは {} の {} です'.format(self.name, n, display_suit, display_rank))


class Player(Participant):
    def is_continue(self):
        print('{} のスコアは {}'.format(self.name, sum(self.rank)))
        if input('引く場合は y, やめる場合は n\n>') == 'y':
            return True
        return False


class Dealer(Participant):
    def is_continue(self):
        print('{} のスコアは {}'.format(self.name, sum(self.rank)))
        if self.get_sum() < 17:
            return True
        return False


def main():
    deck = Deck()
    player = Player('player')
    dealer = Dealer('dealer')

    player.set_hand(deck.draw_card())
    player.set_hand(deck.draw_card())
    dealer.set_hand(deck.draw_card())
    dealer.set_hand(deck.draw_card(), display=False)

    print()

    while player.is_continue():
        player.set_hand(deck.draw_card())
        if player.over_twenty_one():
            print('21 を越えました')
            print('あなたの負けです')
            break

    print()

    if not player.over_twenty_one():
        dealer.display_suit_rank(2)
        while dealer.is_continue():
            dealer.set_hand(deck.draw_card())

        if dealer.over_twenty_one() or player.get_sum() >= dealer.get_sum():
            print('あなたの勝ちです')
        else:
            print('あなたの負けです')


if __name__ == '__main__':

    main()