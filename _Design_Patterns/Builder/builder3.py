class Card:
    def __init__(self):
        self.other = []
    
    @staticmethod
    def create():
        return CardBuilder()

class CardBuilder:
    def __init__(self):
        self.__placeholder = Card()

    def add_parameter(self, param):
        self.__placeholder.other.append(param)
        return self

    def __str__(self):
        return str(self.__placeholder)
    
    def show(self):
        for item in self.__placeholder.other:
            print(item)

if __name__ == '__main__':
    bolt = Card.create()
    bolt.add_parameter("Lightning Bolt")\
    .add_parameter("Wali 3 dipsy w dowolny cel")

    bolt.show()
