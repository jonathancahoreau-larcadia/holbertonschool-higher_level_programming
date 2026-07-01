#!/usr/bin/node

/*
Write a script that prints a square

The first argument is the size of the square
If the first argument can't be converted to an integer, print "Missing size"
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
*/

const arg1 = parseInt(process.argv[2]);
let i = 0;
let j = 0;
const n = 'X';
let nbrX = '';
if (isNaN(arg1)) {
  console.log('Missing size');
}

for (i = 0; i < arg1; i++) {
  nbrX = '';
  for (j = 0; j < arg1; j++) {
    nbrX += n;
  }
  console.log(nbrX);
}
