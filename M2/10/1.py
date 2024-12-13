
class Base:
    # public protected private
    greet = 'Hello'

    def greetings(self):
        print(self.greet)


class Derived(Base):
    def __init__(self):
        self.greetings()


    def __private(self):
        print('(not actually) private method')

d = Derived()
