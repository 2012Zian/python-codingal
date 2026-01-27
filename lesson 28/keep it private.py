class myclass:
    __privateevar = 27

    def __privmeth(self):
        print("i am inside myclss")
    
    def hello(self):
        print("private varible value",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.privmeth()