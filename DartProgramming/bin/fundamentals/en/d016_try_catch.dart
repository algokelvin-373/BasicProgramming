import 'dart:io';

void main() {
  print('');

  try {
    int number;
    stdout.write('Input number : ');
    number = int.parse(stdin.readLineSync()!);
  } catch (e) {
    print('Get Error: ' + e.toString());
    print('You must input number');
  }

  print('Can be run although get error.');

  print('');
}
