import 'dart:io';

void main() {
  print('');

  int width, height;
  stdout.write('输入宽度  : ');
  width = int.parse(stdin.readLineSync()!);
  stdout.write('输入高度 : ');
  height = int.parse(stdin.readLineSync()!);

  for (var h = 1; h <= height; h++) {
    for (var w = 1; w <= width; w++) {
      if (h == 1 || h == height || w == 1 || w == width) {
        stdout.write('*');
      } else {
        stdout.write(' ');
      }
    }
    print('');
  }

  print('');
}
