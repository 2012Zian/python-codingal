class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken")
    def type(self):
        print("hindi is a developing country")
class USA():
    def capital(self):
        print("washington D,C is the capitl of USA")
    def language(self):
        print("english is the primary language of USA")
    def type(self):
        print("USA is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()