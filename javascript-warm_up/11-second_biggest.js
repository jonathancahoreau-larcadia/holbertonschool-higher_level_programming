#!/usr/bin/node

/*
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
*/

const nombreArgument = process.argv.length;
const list_arg = [];

if (nombreArgument < 4) {
  console.log(0);
} else {
  for (let i = 2; i < nombreArgument; i++) {
    list_arg.push(parseInt(process.argv[i]));
  }
  const maxi = Math.max(...list_arg);
  const indexMax = list_arg.indexOf(maxi);
  list_arg.splice(indexMax, 1);
  const secondBiggest = Math.max(...list_arg);

  console.log(secondBiggest);
}
