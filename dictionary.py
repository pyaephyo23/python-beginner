person={
    'name':'Pyae Phyo Kyaw',
    'sex':'male',
    'age':23,
    'relationship': 'single',

}

# print(person)

# if 'name' in person :
    # print('yes');

person['hair_color']= 'black';
# print(person)

person_key = list(person.keys());
print(person_key)
person_values= list(person.values());
print(person_values)
if 'name' in person_key:
    print('yes');
