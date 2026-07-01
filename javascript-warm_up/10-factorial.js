#!/usr/bin/node
/*
Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
*/

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const arg1 = parseInt(process.argv[2]);
const factNaN = 1;

if (isNaN(arg1)) {
  console.log(factNaN);
} else {
  console.log(factorial(arg1));
}
