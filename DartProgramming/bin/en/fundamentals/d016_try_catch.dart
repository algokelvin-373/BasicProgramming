import 'dart:io';

void main() {
  print('');

  try {
    int number;
    stdout.write('Input number : ');
    number = int.parse(stdin.readLineSync()!);
    print('You input number $number');
  } catch (e) {
    print('Get Error: ' + e.toString());
  }

  print('Can be run although get error.');

  print('');
}
