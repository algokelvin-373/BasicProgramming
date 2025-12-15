import 'dart:io';

void printStar(int x) {
  for (var y2 = 1; y2 <= x; y2++) {
    stdout.write('*');
  }
}

void triangle2(int n) {
  for (var x = 1; x <= n; x++) {
    printStar(x);
    print('');
  }
}

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);
  triangle2(n);

  print('');
}
