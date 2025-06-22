import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  // Double Conditional
  if (number % 2 == 0) {
    print('Even Number');
  } else {
    print('Odd Number');
  }

  print('');
}
