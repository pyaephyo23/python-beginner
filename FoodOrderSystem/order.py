class FoodOrder:
    food={
        'apple':2000,
        'orange':2500,
        'watermalon' :3000,
        'mango' :1500,
        'grape' :1700,
        'lemon':700
        
        }
    totalorder=[]

    totalPrice=0
    
    def __init__(self) -> None:
        pass
       
    @classmethod
    def orderFood(self):
        self.orders= input("Please Order your food :")
        while True:
            if self.orders in self.food:
                self.totalorder.append(self.orders)
                self.totalPrice+=self.food[self.orders]
                break
            else :
                self.orders=input("Please choose the correct order :")
                continue
    
    @classmethod
    def checkbill(self):
        print(f'Your Bill is :')
        for tempOrder in self.totalorder:
            print(f"{tempOrder} : {self.food[tempOrder]}")
            print(f"Total Price is : {self.totalPrice}")
    


    
       
