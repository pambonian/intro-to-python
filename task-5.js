function sayHello(name) {
    let msg = 'Hello, ' + name + '. How are you?';
    return msg;
  }
  console.log(sayHello('bootcamp prep')); // feel free to change the string being passed


function checkNumber(num) {
    if (num > 0) {
      return 'positive';
    } else if (num < 0) {
      return 'negative';
    } else {
      return 'zero';
    }
  }
  console.log(checkNumber(5)); // feel free to change the number being passed

  function fizzBuzz1(max) {
    for (let i = 0; i < max; i += 1) {
  
      if (i % 3 === 0 && i % 5 !== 0) {
        console.log(i);
      } else if (i % 5 === 0 && i % 3 !== 0) {
        console.log(i);
      }
    }
  }

  function evenCaps(sentence) {
    let newSentence = "";
  
    for (let i = 0; i < sentence.length; i++) {
      let char = sentence[i];
  
      if (i % 2 === 0) {
        let capitalChar = char.toUpperCase();
        newSentence += capitalChar;
      } else {
        newSentence += char;
      }
    }
  
    return newSentence;
  }