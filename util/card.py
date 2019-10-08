import random

class MakeCard:
    def __init__(self, value):
        self.value = value
        self.showing = False

    def __repr__(self):
        if self.showing:
            return str(self.value)
        else:
            return "card"

class Deck: 
    def __init__(self):
        cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        random.shuffle(cards)
        
        self.cards = []

        for card in cards:
            self.cards.append(MakeCard(card))

    def __repr__(self):
        return str(len(self.cards))
    
    def draw(self):
        return self.cards.pop()