let input = require('fs').readFileSync("/dev/stdin").toString().split(' ');
let num1 = +input[0];
let num2 = +input[1];
console.log(num1+num2);