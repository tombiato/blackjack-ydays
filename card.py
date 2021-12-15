class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def display(self):
        print(str(self.getValue()) + ' ' + str(self.getColor()))
