//Decision: Switch Element

import 'dart:io';
void main() {
  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  switch(number) {
    case 1: print('Your input number 1');
      break;
    case 2: print('Your input number 2');
      break;
    case 3: print('Your input number 3');
      break;
    default: print('Your input another number');
      break;
  }
}