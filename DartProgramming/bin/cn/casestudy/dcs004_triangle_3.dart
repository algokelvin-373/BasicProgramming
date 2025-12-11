import 'dart:io';

void printSpace(int n, int x) {
  for (var y1 = 1; y1 <= n - x; y1++) {
    stdout.write(' ');
  }
}

void printStar(int x) {
  for (var y2 = 1; y2 <= x; y2++) {
    stdout.write('*');
  }
}

void triangle3(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStar(2 * (x - 1) + 1);
    print('');
  }
}

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);
  triangle3(n);

  print('');
}
