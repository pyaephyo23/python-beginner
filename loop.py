num = int(input("Please Enter a numbe : "))
a= 2;
bl=True;
b=1

if num<=1 :
    bl=False;
elif num==2:
    bl=True
else:
    while a<=num :
        if num%a==0 and num==a :
            bl=True
            break
       
        else :
            a=a+1

if bl==True:
    print("It is a prime number");
else :
    print("It is not a prime number")



