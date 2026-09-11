class employee:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("Destructor called, employee deleted")
def Create_obj():
    print("Making object...")
    obj = employee()
    print("Function end...")   
    return obj
print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End...")
         