from abc import ABC,abstractmethod
class abstractclass(ABC):
    def print(self,x):
        print("the passed value is ",x)
    @abstractmethod
    def task(self):
        print("we are nside Abstractclass task")
class test_class(abstractclass):
    def task(self):
        print("we are indies test_vlass task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)