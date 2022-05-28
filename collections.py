# LIST
# TUPLE
# pranav = ("name", 24, 'M')  # inside paranthesis

a = 10
b = 24
# print(a, b)
# SWAPPING 2 numbers
a = a + b # a -> 34, b -> 24
b = a - b # a -> 34, b -> 10
a = a - b

# TUPLE UNPACKING
# (n1, n2) = (n2, n1)

# print(a, b)

# use  case

# (name, age, gender) = ("pranav", 21, 'M')
# (a, b) = (100, 200)
# a = 100
# b = 200

# print(name)
# print(age)
# print(gender)

# for x in tup:
#   print(x)
 
# li = [1, 2, 3, 3, 3, 3]

# st = set(li)

# thirich_list = list(st)

# print(thirich_list)

# list or array
# DICTIONARY or hashmap

# pranav = ("name", 24, 'M')

# key value pairs
person = {
  "name": "pranav",
  "age": 24,
  "gender": "M",
  "skills": ["Java", "C", "Python"],
}

# getting one value using key
person_name = person['name']

person["favourite food"] = "Chappathi"

person.pop("name")

# get all keys as a list
keys_list = person.keys() # ['name', 'age', 'gender', 'skills', 'favourite food']

# looping through each key in the list of keys
for key in keys_list:
  value = person[key] # getting each value using the key we got from the list
  print(value) 


people = [ 
  { "name": "pranav", "age": 23 },
  { "name": "thanush", "age": 24}
]

list_of_lists = [ [1, 2], [ [3, 5], 4] ]

# assign
s = people[1]['name']

# print the name of the 2nd person in the people list

# put a dictionary inside another dictionary and access the inner dictionary's values

# print value of 'd'
a = {
  'b': {
    'c': {
      'd': "this is the 3rd nested dictionary's value"
    }
  }
}

b = a['b']
c = b['c']
d = c['d']

print(a)
print(a['b'])
print(a['b']['c'])
print(a['b']['c']['d'])

a['b']['c']['d']
