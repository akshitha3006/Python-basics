class MyClass:
    __privateVar = 36
    def __privmeth(self):
       print("This is a private method")
    def hello(self):
        print(self.__privateVar)   
obj = MyClass()
obj.hello()

    