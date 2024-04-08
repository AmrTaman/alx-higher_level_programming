#!/usr/bin/node
const args = process.argv;
const argLen = process.argv.length;
if (argLen <= 2) {
  console.log('No argument');
}
for (let x = 2; x < argLen; x++) {
  console.log(args[x]);
}
