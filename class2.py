class Clothes:

    count = 20;
    def __init__(self):
        
        self.type = input("Please enter cloth type :")
        self.brand = input("Enter brand :")
        self.size = input("Enter cloth size :")
    
    def is_new(self):
        if self.type=='shirt' and self.brand=='gussi' and self.size=='l' :
            print('It is available')
        else :
            print("it is not available");

    @classmethod
    def clcount(cls):
        print(f'There are {cls.count} in this shop');

# print(Clothes.count);
#Clothes.clcount();




 #aa= Clothes(type,brand,size)

# aa.is_new();

# aa =Clothes();
# aa.is_new();




