import 'dart:io';

void main() {
  print('');

  int? number;
  stdout.write('输入涉资 = ');
  number = int.parse(stdin.readLineSync()!);
  print('您输入的数字是 $number');

  String? strName;
  stdout.write('你叫什么名字? ');
  strName = stdin.readLineSync();
  print('你的名字是$strName');

  print('');
}
