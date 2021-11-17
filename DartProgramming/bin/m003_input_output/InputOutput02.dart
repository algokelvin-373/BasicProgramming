//Input Output String

import 'dart:io';

void main() {
  String? text;
  stdout.write('Input text: ');
  text = stdin.readLineSync();
  print('You input text: $text');
}