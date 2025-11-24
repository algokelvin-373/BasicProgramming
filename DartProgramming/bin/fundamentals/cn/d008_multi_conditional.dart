import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('输入数字 : ');
  number = int.parse(stdin.readLineSync()!);

  if (number > 0) {
    print('正数。');
  } else if (number == 0) {
    print('数字零');
  } else {
    print('负数');
  }

  print('');
}
