class Player:
    def __init__(self, player_number, is_ai):
        self.player_number = player_number
        self.is_ai = is_ai
        self.money = 30
        self.enemy_card = ""
        self.past_card = []
    