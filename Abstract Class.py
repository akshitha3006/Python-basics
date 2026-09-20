from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        pass
class test_class(Absclass):
      def task(self):
          print("This is an abstract method")
test_obj = test_class()
test_obj.task()
test_obj.print(10)          
