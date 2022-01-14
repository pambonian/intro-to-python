numbers = [1, 2, 3, 4]
def triple_num(num):
    return num * 3

# result = map(double_num, numbers)
# print('before', result)
# print('after making it a list', list(result))

result = map(triple_num, numbers)
print('before', result)
print('after making it a list', list(result))

result2 = map(lambda x: x + x, numbers)
print('result 2 -> list', list(result2))

result3 = map(lambda y: y * y, numbers)
print('result 3 -> list', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('result 4 -> list', list(result4))


# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]

print('---- filter ----')

ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = list(filter(lambda person_age: person_age < 21, ages))
print('Young Folks', young_folks)

grown_folks = list(filter(lambda person_age: person_age >= 21, ages))
print('Grown Folks', grown_folks)

def is_not_21(person_age):
    if person_age < 21:
        return True
    else:
        return False

def is_21(person_age):
    if person_age >= 21:
        return True
    else:
        return False

young_people = list(filter(is_not_21, ages))
print('Young People', young_people)

grown_people = list(filter(is_21, ages))
print('Grown People', grown_people)