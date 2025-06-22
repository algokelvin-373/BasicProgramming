import 'dart:io';

void main() {
  print('');

  // 双重循环
  for (var i = 1; i < 10; i++) {
    int number = i;
    for (var j = 1; j <= i; j++) {
      stdout.write(number);
    }
    print('');
  }

  print('');
}
