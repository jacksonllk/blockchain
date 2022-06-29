person_list = [{'name': 'Jack', 'age': 37, 'hobbies': ['golf', 'jog']}, 
               {'name': 'George', 'age': 50, 'hobbies': ['hiking', 'swimming']},
               {'name': 'Dora', 'age': 18, 'hobbies': ['gaming', 'reading']},
               {'name': 'Mandy', 'age': 28, 'hobbies': ['baking', 'knitting']},  
]
# print(person_list)


name_list = [person['name'] for person in person_list]
print(name_list)


are_older = all([person['age'] > 20 for person in person_list])
print(are_older)

# import copy
# dup_person_list = copy.deepcopy(person_list)
dup_person_list = [person.copy() for person in person_list]
dup_person_list[0]['name'] = 'Marion'
print(dup_person_list)
print('-' * 50)
print(person_list)

print('-' * 50)

person_1, person_2, person_3, person_4 = person_list
print(person_1['age'])
print(person_2['name'])
print(person_3)
print(person_4['hobbies'])