import 'dart:io';

void main() {
  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  if (number > 0) {
    print('Positive');
  } else {
    print('Negative');
  }
}
