class UserrTest:

    adminName= 'Pyae Phyo Kyaw'
    adminPsw='12345'

    
    username=''
    userpassword=''

    def __init__(self) -> None:
        pass
        
    
    @classmethod
    def testu(self):
        self.temp=input("Are you a customer or server? c/s?")

        while True:
            if self.temp=='c':
                FoodOrder.orderFood()
                FoodOrder.checkbill()
            elif self.temp=='s':
                while True:
                    self.username=input("Please Enter username :")
                    self.userpassword=input("Please Enter Password :")
                    if self.username==self.adminName and self.userpassword==self.adminPsw :
                        print(f"Welcome {self.adminName}")
                        break
                    else :
                        print('There is something wrong wtih your sign in !')
                        continue
        

TestUser.testu();
                
                
                

    
