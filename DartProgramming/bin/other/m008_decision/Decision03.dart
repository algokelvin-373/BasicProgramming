//Multiple Decision If - Else If - Else

import 'dart:io';
void main() {
  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  if (number > 0) {
    print('The number that you input is positive');
  } else if (number == 0) {
    print('The number that you input is null');
  } else {
    print('The number that you input is negative');
  }
}
