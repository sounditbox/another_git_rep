class Human:
    def hello(self):
        print('Hello!')

    def goodbye(self):
        print('Goodbye!')

    def tell(self, text):
        print(f'I am telling you this: {text}')

h1 = Human()
h2 = Human()
h1.hello()
h2.hello()
h1.tell('Peace and freedom')