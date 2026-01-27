class dog:
    species = "animal"

    def __init__(self,name,age):
        self.name = name
        self.age=age
gogo = dog("gogo",10)
sogo = dog("sogo",15)
print("gogo is a ",gogo.species)
print("sogo is a ",sogo.species)
print(gogo.name , " is " ,gogo.age,"years old")
print(sogo.name , " is " ,sogo.age,"years old")