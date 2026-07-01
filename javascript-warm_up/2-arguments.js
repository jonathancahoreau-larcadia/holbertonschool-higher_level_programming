#!/usr/bin/node
/*
If no arguments are passed to the script, print "No argument"
If only one argument is passed to the script, print "Argument found"
Otherwise, print "Arguments found"
You must use console.log(...) to print all output
You are not allowed to use var
*/

const nombreArgument = process.argv.length;

if (nombreArgument < 3) {
  console.log('No argument');
} else if (nombreArgument === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
