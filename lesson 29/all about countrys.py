class bmw():
    def speed(self):
        print("bmw is very fast with 300kmph")
    def mileage(self):
        print("crazy range of 700km")
    def hp(self):
        print("average of 400whp")
class ferrari():
    def speed(self):
        print("crazy top speed of 370kmph")
    def mileage(self):
        print("mild range of 400km")
    def hp(self):
        print("crazy ph of 1000whp")
obj_bmw = bmw ()
obj_ferrari = ferrari()
for brand in (obj_bmw,obj_ferrari):
    brand.speed()
    brand.mileage()
    brand.hp()