import math

class krug:
    def __int__(self, r):
        self.r = r
    def lenght(self):
        dovzhyna = 2 * self.r *  math.pi
        return dovzhyna
    def square(self):
        ploshcha = math.pi * self.r**2
        return ploshcha


