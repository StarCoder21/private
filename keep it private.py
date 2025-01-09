class myclass:
    __privateVar=21
    def __privmeth(self):
        print("I m inside the class myclass")
    def Hello(self):
        print("Private variable value is ",myclass.__privateVar)
obj=myclass()
obj.Hello()
obj.__privmeth
