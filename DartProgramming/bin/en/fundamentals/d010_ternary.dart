import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  // Ternary Operator
  String result = (number > 0) ? "Positive" : "Negative";
  print(result);

  print('');
}
