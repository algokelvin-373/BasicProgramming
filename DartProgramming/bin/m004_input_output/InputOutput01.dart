//Input Output Number

// Using this to get implement input output
import 'dart:io';

void main() {
  int? number;
  double? decimal;

  stdout.write('Input number = '); // Display in terminal or console
  number = int.parse(stdin.readLineSync()!); // Input from Keyboard
  print('You input number $number');

  stdout.write('Input variable b = ');
  decimal = double.parse(stdin.readLineSync()!);
  print('You input decimal $decimal');
}
