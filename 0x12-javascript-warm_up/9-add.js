#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (!isNaN(num1) && !isNaN(num2)) {
  const x = add(num1, num2);
  console.log(x);
} else {
  console.log('NaN');
}
