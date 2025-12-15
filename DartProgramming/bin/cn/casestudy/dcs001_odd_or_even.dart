import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('输入数字 : ');
  number = int.parse(stdin.readLineSync()!);

  // Double Conditional
  if (number % 2 == 0) {
    print('偶数');
  } else {
    print('奇数');
  }

  print('');
}
