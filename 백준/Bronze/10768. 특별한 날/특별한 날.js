const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "example.txt";
let [a,b] = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);
if((a === 2 && b < 18) || a === 1) console.log("Before");
if(a === 2 && b === 18) console.log("Special");
if ((a === 2 && b > 18) || a > 2) console.log("After");