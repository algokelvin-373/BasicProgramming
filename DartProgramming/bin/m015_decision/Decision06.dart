// Ternary Operator ( ?: )

import 'dart:io';

void main() {
  int number;
  stdout.write('Input number : ');
  number = int.parse(stdin.readLineSync()!);

  // Ternary Operator '?:'
  String dt = number > 0 ? "positive" : "negative";
  print("Your number input is $dt");
}