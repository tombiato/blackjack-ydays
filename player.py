class Player:
    main = []

    def draw(self, card):
        self.main.append(card)

    def displayHand(self):
        return print(self.main)
