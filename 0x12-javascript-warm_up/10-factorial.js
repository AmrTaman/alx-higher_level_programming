#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return (n);
  }
  return (n * factorial(n - 1));
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('1');
} else {
  const x = factorial(num);
  console.log(x);
}
