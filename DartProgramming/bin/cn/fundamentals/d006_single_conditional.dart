import 'dart:io';

void main() {
  int number;
  stdout.write('输入数字 : ');
  number = int.parse(stdin.readLineSync()!);

  if (number > 0) {
    print('正数。');
  }
}
