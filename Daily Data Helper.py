class DilyDataHelper:
    def __init__(self,name):
        self.name=name
    def process_data(self,text,numbers,target):
        print("Uppercase:",text.upper())

        for i, val1 in enumerate(numbers):
            for j, val2 in enumerate(numbers):
                if i != j and val1 + val2 == target:
                    print("Pair found at index",i,"and",j,"(",val1,"+",val2,"=",target,")")
                    return
    def __del__(self):
        print("Session ended for",self.name)
msg = input("Enter a string:")
helper = DilyDataHelper("Daily Data Helper")       
helper.process_data(msg,[10,20,30,40],50)
del helper             