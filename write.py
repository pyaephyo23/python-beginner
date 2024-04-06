# with open('./write.txt','w') as file :
#     file.write("I am Pyae Phyo Kyaw");


# with open('./write.txt','w') as file :
#     file.write("\n am 23 years old");


# with open('./write.txt','a') as fi:
#     fi.write('\nI am a student')

with open('./write.txt','w') as file :
    text=["I am Pyae Phyo Kyaw","\nI am 23 years old"]

    file.writelines(text)