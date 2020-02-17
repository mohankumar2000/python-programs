class Square:
    def __init__(self,side, price):
        self.side=side
        self.price=price
    def perimeter(self):
        return self.side*4
    def area(self):
        return self.side*self.side
    def total_cost(self):
        return self.area()*self.price
sq1=Square(4,6)
print(sq1.total_cost())
