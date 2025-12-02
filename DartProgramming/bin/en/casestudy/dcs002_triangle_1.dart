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

void triangle1(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStar(x);
    print('');
  }
}

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);
  triangle1(n);

  print('');
}
