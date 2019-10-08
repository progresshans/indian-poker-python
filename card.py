import random

class MakeCard(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Deck(list): 
    def __init__(self):
        self.cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        random.shuffle(self.cards)

        for card in self.cards:
            self.append(MakeCard(card))