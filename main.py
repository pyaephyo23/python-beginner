
uname = "Pyae Phyo Kyaw";
psw= "15547ppk";

un = input ("Please enter your user name :" );
pw = input ("Please enter your password :");

if un==uname and pw==psw:
    print(f"Welcome come {uname}");

elif un != uname:
    print(f"There is no user name as {un}");
elif pw!=psw :
    print("Your password is wrong");



