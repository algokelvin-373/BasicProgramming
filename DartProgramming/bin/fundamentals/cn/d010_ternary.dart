import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('输入数字 : ');
  number = int.parse(stdin.readLineSync()!);

  // Ternary Operator
  String result = (number > 0) ? "正数" : "负数";
  print(result);

  print('');
}
