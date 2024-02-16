class parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        p = 2 * (self.a + self.b)
        return p

    def square(self):
        s = self.b * self.h
        return s

data = parallelogram(2, 5.2, 4)
print(data.square())