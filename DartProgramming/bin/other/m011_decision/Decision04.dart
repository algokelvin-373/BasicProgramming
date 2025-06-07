//'If' with If in Inner

import 'dart:io';
void main() {
  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  if (number > 0) {
    print('The number that you input is positive');
    if (number % 2 == 0) {
      print('The number that you input is can be divided by 2');
    } else {
      print('The number that you input is cannot be divided by 2');
    }
  } else {
    print('The number that you input is negative');
    if (number % 2 == 0) {
      print('The number that you input is can be divided by 2');
    } else {
      print('The number that you input is cannot be divided by 2');
    }
  }
}
