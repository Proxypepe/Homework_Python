class C32:
    def __init__(self):
        self.position = 'A'

    def slip(self):
        if self.position == 'A':
            self.position = 'B'
            return 0
        elif self.position == 'B':
            self.position = 'C'
            return 1
        elif self.position == 'C':
            self.position = 'D'
            return 3
        elif self.position == 'E':
            self.position = 'C'
            return 7
        elif self.position == 'F':
            self.position = 'G'
            return 8
        elif self.position == 'G':
            self.position = 'C'
            return 11
        else:
            raise RuntimeError()

    def hop(self):
        if self.position == 'B':
            return 2
        elif self.position == 'E':
            self.position = 'F'
            return 6
        elif self.position == 'F':
            self.position = 'B'
            return 9

        else:
            raise RuntimeError()

    def join(self):
        if self.position == 'D':
            self.position = 'H'
            return 5
        elif self.position == 'G':
            self.position = 'H'
            return 10
        else:
            raise RuntimeError()

    def rev(self):
        if self.position == 'D':
            self.position = 'E'
            return 4
        else:
            raise RuntimeError()


if __name__ == '__main__':
    try:
        o = C32()
        print(o.slip())
        print(o.hop())

        print(o.slip())
        print(o.slip())
        print(o.rev())

        print(o.hop())
        print(o.slip())

    except RuntimeError:
        print("RuntimeError")


