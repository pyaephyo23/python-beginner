class fruit:
    menu = {
        'apple':2000,
        'orange':2500,
        'watermalon' :3000,
        'mango' :1500,
        'grape' :1700,
        'lemon':700

    }
    def __init__(self):
        self.total=0
        self.orders=[]

    # def checkOrder(self,order):
    #     while True:
    #         if order in self.menu:
    #             break
    #         else:
    #             order =input("Please order your item again! ")

             

    def addOrder(self,order):
        
        self.orders.append(order)
        self.total += self.menu[order]
        
    
    def checkBill(self):
        print("Your order are ")
        for order in self.orders:
            print(f'{order} : {self.menu[order]}')
        print(f"Total Amount ={self.total}")



def startProgram():
    order= fruit();

    while True:
       oo= input("Please order your item : ")
      # order.checkOrder(oo)
       order.addOrder(oo)
       a = input("Do you want to order more? y/n :")

       if a=='y':
           continue
       if a=='n':
           order.checkBill()
           break 
       else:
           a=input("Please enter y/n :");

startProgram()





