# file = open('./text.txt')

# # for line in file:
# #     print(line);


# # file.seek(0);

# # linelist = file.readlines();
# # print(linelist);

# file.seek(20);

# paragarph= file.read(20);
# print(paragarph);
# file.close();

with open('./text.txt') as file:
    for line in file:
        print(line);

