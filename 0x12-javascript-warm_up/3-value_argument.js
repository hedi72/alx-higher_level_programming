#!/usr/bin/node

if (process.argv[2] === undefined) {
  let index = 2;
  while (process.argv[index]) {
    console.log(process.argv[index]);
    index++;
  }
} else {
  console.log('No argument');
}
