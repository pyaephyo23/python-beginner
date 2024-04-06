students={};
a='y';
while a == 'y':
    
    name= input('Name :')
    age=input('age :')
    year= input('Year :')
    stdID=input('ID :')

    students['name']=name
    students['age']=age
    students['year']=year
    students['ID']=stdID

    a= input("Do you want to continue? y/n ? :")
    if a== 'y':
        continue
    elif a=='n':
        break;
    else :
        a= input("Please enter y/n.");

for (key,values) in students.items() :
    print(f"Student {key} is {values}. ")
