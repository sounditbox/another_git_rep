class B:
    def __init__(self):
        raise FileNotFoundError


class A:
    def __init__(self):
        self.b = B.__init__()


a = A()