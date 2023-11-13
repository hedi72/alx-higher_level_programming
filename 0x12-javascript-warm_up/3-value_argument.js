#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  for (let index = 2; index < process.argv.length; index++) {
    console.log(process.argv[index]);
  }
}
