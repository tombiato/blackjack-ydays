from cards import Cards


class Game:
    values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def play(self):
        deck = Cards()
        deck.shuffle()

        bank = []
        player = []

        totalPlayer = 0
        totalBank = 0

        for i in range(2):
            player.append(deck.draw())
            bank.append(deck.draw())

        for card in player:
            totalPlayer += self.values[card.getValue()]

        for card in bank:
            totalBank += self.values[card.getValue()]

        '''
        Print hands
        '''
        print('Banks hand:')
        for card in bank:
            print(card.display())

        print('\n')

        print('Players hand: ')
        for card in player:
            print(card.display())

        print('\n')

        '''
        Draw phase
        '''
        response = input('Card? [y/n] (default y): ')

        while response == 'y':
            card = deck.draw()

            print("Card draw: ")
            print(card.display())

            print('\n')

            player.append(card)

            totalPlayer += self.values[card.getValue()]

            if totalPlayer > 21:
                print("You're out 21. You loose.")
                return

            response = input('Card? [y/n] (default y): ')

        while totalBank < 17:
            card = deck.draw()

            print("Card draw:")
            print(card.display())

            print('\n')

            bank.append(card)

            totalBank += self.values[card.getValue()]

            if totalBank > 21:
                print("Bank is out 21. You win.")
                return

        if (totalBank > totalPlayer):
            print('Bank win with: ' + str(totalBank))
        elif (totalBank < totalPlayer):
            print('You win, banks hand was: ' + str(totalBank))


game = Game()
game.play()
