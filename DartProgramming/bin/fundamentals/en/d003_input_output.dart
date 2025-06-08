import 'dart:io';

void main() {
  print('');

  int? number;
  stdout.write('Input number = ');
  number = int.parse(stdin.readLineSync()!);
  print('You input number $number');

  String? strName;
  stdout.write('What is your name? ');
  strName = stdin.readLineSync();
  print('Your name is $strName');

  print('');
}
