class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self,radius):
        return 3.14 * self.radius * self.radius
    def parimeter(self,radius):
        return 2 * 3.14 *self.radius
radius = int(input("enter the radius"))
r = circle(radius)
print(r.area(radius))
print(r.parimeter(radius))