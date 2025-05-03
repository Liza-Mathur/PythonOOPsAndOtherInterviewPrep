class Circle():

    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2 * 3.1416 * self.radius

    def area(self):
        return 3.1416 * self.radius**2

if __name__=="__main__":
    circle = Circle(7)
    print(circle.perimeter())
    print(circle.area())