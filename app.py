# this is a comment
# TODO build this function

'''
    this is supposed to be multi line comment
'''

def add(num, num2):
    '''
    this is supposed to add 2 numbers
    '''
name = "Johnny"
print(name)

nothing = None
print(nothing)
    
is_working = True
car_off = False

print(is_working)

if nothing:
    print('This is true') # [x]
    num = 7
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')
else:
    print('This is not true...')

# this is another conditional
if is_working:
    print('This is working also')

print(15 / 6)
print(15 // 6)
# conditional -> this first item that represents
# True, it runs that indented block

print("ace of spades".split(" "))

print("qqxzz".index("x"))

print(len("Hawaii"))

# get the last letter
print("my code rulez"[-1])
# "z"

print("my code rulez"[3:7])
# "code"

print("my code rulez"[:2])
# "my"

print("my code rulez"[3:])
# "code rulez"

print("my code rulez"[::-1])
# "zelur edoc ym"

# take every other letter
print("peiege eleaeteiene"[::2])
# 'pig latin'

if 7 == 7:
    print('This is seven')
else:
    print("This is the second condition")

if 7 != 6:
    print('This is seven')
else:
    print("This is the second condition")

if not 7:
    print('This is seven')
else:
    print("This is the second condition")

arr = [1, 'two', 3, 'four', True, False, 'hello']
print(len(arr))
print (arr[1])
print (arr[-1])

one_through_ten = list(range(10))
print(one_through_ten)

a = [1, 23, 12, 99, 82]
a.sort()
print(a)

a.append(88)
print(a, 'after adding 88')

a.insert(2, 77)
print(a)

# help(str)
# help(dict)

cat = {
    "name": 'Hamlet',
    "breed": 'American Shorthair',
    "fav_food": 'Prosciutto'
}

cat["name"]

cat["fav_food"]

print('this is my cat breed', cat.get("breed"))
print(cat.get("name"))
cat["age"] = 3
print(cat.get('age'))

print('ITEMS', cat.items())
print('KEYS', cat.keys())

state = "washington state"
year = 1889
n = 42
my_message = f"{state} was the {n}nd state to join the union in {year}"
print(my_message)

location = "California"
number = 6
my_second_message = f"{location} is the {number}th largest economy in the world"
print(my_second_message)

topic = 'Inflation'
num = 7
y = 1982
my_third_message = "{} is at {} percent. Highest since {}".format(topic, num, y)
print(my_third_message)

myname = "patrick"
myhighcsr = 1402
currentrank = "Diamond 4"
my_ranked_message = f"My name is {myname}, my highest csr so far was {myhighcsr}, but currently i'm ranked {currentrank}"
print(my_ranked_message)

weapon = "battle rifle"
ttk = 42.3
reload_time = 3
my_br_message = "The {} is efficient, it's time to kill is {} seconds, and only takes {} seconds to reload".format(weapon, ttk, reload_time)
print(my_br_message)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

template = "My name is {} and I like {}"
template.format("Steve", "Cheese")
'My name is Steve and I like Cheese'

# templatedeuce = "My name is {name} and I like {food}"
# template.format(food="Cheese", name="Steve")
# 'My name is Steve and I like Cheese'

# loops

# n = 0
# while n < 1000:
#     n += 1
#     if n % 2 == 0:
#         print(f'{n} is even')

n = True
num = 1
while n:
    if num % 2 == 0:
        print(f'{num} is even...')
        if num == 750:
            n = False
            print('End program')
    num += 1
    print(num)

# for loop

for i in range (1, 751):
    if i % 2 ==0:
        print (f'{i} is even...', '**')
        if i == 750:
            print('end program')

nums = [1,2,3,55,66,44,33,22,11,33,750,44,66,33,33,22]
for i in range(len(nums)):
    element = nums[i]
    if element % 2 == 0:
        print(f'{element} is even...', 'NUMS')

        if element == 750:
            print('Hi I am 750')

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]

for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == "Los Angeles":
        print(f'{student.get("name")}: this student wins! For {student.get("city")}')

for i in range(len(students)):
    student = students[i]
    print(student.get("city"))

# Iterating through list of students
for student in students:
    print(student)

# Iterating through dict(ionary)
for key in students[0]: # key to key
    print(key)
    print('value', students[0].get(key))

# Iterating through dict(ionary) part 2
for key in students[1]: # key to key
    print(key, 'Part 2')
    print('value', students[1][key])

# Iterating through dict(ionary) part 3
for anything in students[2]: # key to key
    print(key, 'Part 3')
    print('value', students[1][anything])
    
# Iterating through dict PART 4
for key, value in students[0].items(): # key to key
    print(key, '->', value)

def say_hello(friend="Tim"):
    print("Hello, {}!".format(friend))

say_hello("Tom")

def move(name, city="Seattle", state="Washington"):
    msg = "{} is moving to {}, {}"
    msg = msg.format(name, city ,state)
    print(msg)

move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")
move("John", state="New York", city="New York")

def move(reply1, reply2):
    print(f'{reply1} my friend {reply2}')

move("All good in the hood", "Benjamin")

def get_cities(students):
    '''Return a [list] of all cities from the students list'''
    # TODO Make a empty list
    # TODO Iterate through the list of student
    # TODO Append each city in the dict to the empty list
    # TODO return the list

    result = []

    for s in students:
        if s.get('city'):
            result.append(s.get('city'))

    return result

print('Cities list: ', get_cities(students))


def get_names(students):
    '''return list of cities from the students list'''
    result = []
    
    for student in students:
        if student.get("name"):
            result.append(student.get("name"))
        else:  
            return ('error')
    
    return(result)


print('name_list', get_names(students))

def parse_by_cities(students):
    # return a dict that has a key for each city and a list of students for each city
    #  TODO make an empty dict
    #  TODO iterate through the list of students and perform logic
        #  logic -> if city is not in dict
            #  add the city and set that to an empty list
        #  logic -> if the city is in the dict
            #  append student name to list
    # TODO return the dict

    result = {}

    for student in students:
        print('Print INSIDE', student)
        if student.get('city'):
            if not result.get(student.get('city')):
                print('Does not exist')
                result[student.get('city')] = []
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))
            else:
                print('Does exist')
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))

    print('-------space---------')

    return result

print('Printing OUTSIDE', parse_by_cities(students))
