#  TASK ONE

# 4 + 4 / 2
print(4 + 4 / 2)
# (2 + -7) * 3
print((2 + -7) * 3)
# 101 % 10
print(101 % 10)
# 12 - 4 % 3
print(12 - 4 % 3)
# true && false
print(True and False)
# true && !(false || false)
print(True and not (False or False))
# !true && !(false || false)
print(not True and not (False or False))
# 'cat' + 'dog'
print('cat' + 'dog')
# 2 + 'pizza'
print(str(2) + 'pizza')
# 2.5 * 'fish'
print(2.5 * len('fish'))
# 5 >= 11
print(5 >= 11)
# 5 === 5.0
print(5 == 5.0)
# 7 !== 7.1
print(7 != 7.1)
# 5 + 5 > 8
print(5 + 5 > 8)
# 6 + 6 !== 12
print(6 + 6 != 12)
# 2 > 1 || false
print(2 > 1)
# 'true' === true
print('true' == True)
# 10 % 2 === 0
print(10 % 2 == 0)
# 21 % 2 === 0
print(21 % 2 == 0)
# 21 % 2 !== 0
print(21 % 2 != 0)
# 21 % 2 === 1
print(21 % 2 == 1)
# 12 % 3 === 0
print(12 % 3 == 0)
# 9 % 3 === 0
print(9 % 3 == 0)
# 14 % 3 === 0
print(14 % 3 == 0)
# 'new york'[0]
print('new york'[0])
# 'new york'[1]
print('new york'[1])
# 'san francisco'[2 * 3]
print('san francisco'[2 * 3])
# 'engineering'[3].toUpperCase()
print(('engineering'[3]).upper())
# 'engineering'.indexOf('G')
print("engineering".index("g"))
# 'engineering'.indexOf('neer')
print("engineering".index("neer"))
# 'engineering'.indexOf('r') > -1
print(("engineering".index("r")) > 1)
# 'science'.indexOf('x') === -1
print("science".index("x") == 1)

#  TASK TWO

# // 1
# let idx = 'abcde'.indexOf('D');
# idx = idx + 11;
# console.log(idx); // ?
# idx * 2;
# console.log(idx); // ?

# // 2
# let num = 33;
# let isEven = num % 2 === 0;
# console.log(isEven); // ?
# console.log(!isEven); // ?

# // 3
# let str1 = 'marker';
# let num = 'whiteboard'.length - str1.length;
# console.log(num); // ?
# let str2 = 'bootcamp';
# console.log(str2[num].toUpperCase()); // ?
# let char = str2[num].toLowerCase(); // ?
# console.log(char + '!'); // ?

# // 4
# let sentence = 'welcome to bootcamp prep';
# let lastChar = sentence[sentence.length - 1];
# console.log(lastChar); // ?
# console.log(sentence.indexOf(lastChar)); // ?