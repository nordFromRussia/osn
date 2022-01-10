class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):
        if ((other.x > self.x + self.w) or (other.y > self.y + self.h) or
                (self.x > other.x + other.w) or (self.y > other.y + other.h)):
            print('None')
        else:
            R3 = Rectangle(0, 0, 0, 0)
            R3.x = max(self.x, other.x)
            R3.w = min(self.x + self.w, other.x + other.w) - R3.x
            R3.y = max(self.y, other.y)
            R3.h = min(self.y + self.h, other.y + other.h) - R3.y
            return R3