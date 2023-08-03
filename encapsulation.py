class Customer:
    def __init__(self,name,accountNo,mobileNo):
        self.name=name
        self._mobileNo=mobileNo
        self.__accountNo=accountNo
    def display(self):
        print("AccountDetails")
class Customer2(Customer):
    def display1(self):
        print("name: ",self.name)
        print("accountno: ",self._Customer__accountNo)
        print("MobileNo: ",self._mobileNo)
obj=Customer2("Ravi",45565,456532)
obj.display()
obj.display1()


