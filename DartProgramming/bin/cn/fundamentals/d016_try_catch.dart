import 'dart:io';

void main() {
  print('');

  try {
    int number;
    stdout.write('输入数字 : ');
    number = int.parse(stdin.readLineSync()!);
    print('您输入的数字是 $number');
  } catch (e) {
    print('发生错误: ' + e.toString());
  }

  print('即使发生错误也可以运行。');

  print('');
}
