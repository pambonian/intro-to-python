// 1
let idx = 'abcde'.indexOf('D');
idx = idx + 11;
console.log(idx); // ?
idx * 2;
console.log(idx); // ?

// 2
let num = 33;
let isEven = num % 2 === 0;
console.log(isEven); // ?
console.log(!isEven); // ?

// 3
let str1 = 'marker';
let num = 'whiteboard'.length - str1.length;
console.log(num); // ?
let str2 = 'bootcamp';
console.log(str2[num].toUpperCase()); // ?
let char = str2[num].toLowerCase(); // ?
console.log(char + '!'); // ?

// 4
let sentence = 'welcome to bootcamp prep';
let lastChar = sentence[sentence.length - 1];
console.log(lastChar); // ?
console.log(sentence.indexOf(lastChar)); // ?