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
print("science".index("s") == 1)

#  TASK TWO

# // 1
# let idx = 'abcde'.indexOf('D');
# idx = idx + 11;
# console.log(idx); // ?
# idx * 2;
# console.log(idx); // ?

idx = 'abcde'.index('d')
idx = idx + 11
print('hello', idx)
print(idx * 2)

# // 2
# let num = 33;
# let isEven = num % 2 === 0;
# console.log(isEven); // ?
# console.log(!isEven); // ?

num = 33
isEven = num % 2 == 0
print(isEven)
print(not isEven)

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

# TASK THREE

# // 5
# let age = 30; // try different numbers here
# if (age > 30) {
#   console.log('older than 30');
# } else {
#   console.log('younger than 30');
# }

# // 6
# let str = 'pizza'; // try different strings here
# if (str.length > 10) {
#   console.log('long string');
# } else {
#   console.log('short string');
# }
# if (str[0] === 'p') {
#   console.log('starts with p');
# }

# // 7
# let num = 15; // try different numbers here
# if (num % 3 === 0) {
#   console.log('divisible by 3');
# } else if (num % 5 === 0) {
#   console.log('divisible by 5');
# }

# // 8
# let num = 15; // try different numbers here
# if (num % 3 === 0) {
#   console.log('divisible by 3');
# }
# if (num % 5 === 0) {
#   console.log('divisible by 5');
# }

# // 9
# let str = 'General Assembly'; // try different strings here
# if (str[0] === str[0].toUpperCase()) {
#   console.log('starts with a capital!');
# }
# if (str[str.length - 1] === str[str.length - 1].toUpperCase()) {
#   console.log('ends with a capital!');
# }

# // 10
# let num = -44; // try different numbers here
# if (num > 0) {
#   console.log('positive');
# } else if (num < 0) {
#   console.log('negative');
# } else {
#   console.log(0);
# }
# if (num % 2 === 0) {
#   console.log('even');
# } else {
#   console.log('odd');
# }

# TASK FOUR

# let num = 11; // feel free to change the value of this variable
# if (num > 5) {
#   console.log('if');
# }

# let num = 5; // feel free to change the value of this variable
# if (num > 5) {
#   console.log('if');
# } else {
#   console.log('else');
# }

# let num = 0; // feel free to change the value of this variable
# if (num < 0) {
#   console.log('if');
# } else if (num > 0) {
#   console.log('else if');
# } else {
#   console.log('else');
# }

# TASK FIVE

# function sayHello(name) {
#     let msg = 'Hello, ' + name + '. How are you?';
#     return msg;
#   }
#   console.log(sayHello('bootcamp prep')); // feel free to change the string being passed


# function checkNumber(num) {
#     if (num > 0) {
#       return 'positive';
#     } else if (num < 0) {
#       return 'negative';
#     } else {
#       return 'zero';
#     }
#   }
#   console.log(checkNumber(5)); // feel free to change the number being passed

#   function fizzBuzz1(max) {
#     for (let i = 0; i < max; i += 1) {
  
#       if (i % 3 === 0 && i % 5 !== 0) {
#         console.log(i);
#       } else if (i % 5 === 0 && i % 3 !== 0) {
#         console.log(i);
#       }
#     }
#   }

#   function evenCaps(sentence) {
#     let newSentence = "";
  
#     for (let i = 0; i < sentence.length; i++) {
#       let char = sentence[i];
  
#       if (i % 2 === 0) {
#         let capitalChar = char.toUpperCase();
#         newSentence += capitalChar;
#       } else {
#         newSentence += char;
#       }
#     }
  
#     return newSentence;
#   }