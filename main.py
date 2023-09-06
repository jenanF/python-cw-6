# write your code here
# PART 1
person = {'name':'jenan', 'age': 17, 'hobbies':['coding', 'baking', 'editing']}
print(person['name'])
print(person['age'])

# PART 2
person['age'] = 18
person['country'] = 'kuwait'
print(person)
print(person.__len__())

# PART 3
person['hobbies'] += ['video games']

def check_hobbies(person):
    if person['hobbies'].__len__() > 3:
        print("WOW YOU ARE AMAZING")
    else:
        print("nice")

check_hobbies(person)

