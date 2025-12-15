import 'dart:io';

void printStartWithHole(int x, int line, int finish) {
  for (var y = 1; y <= finish; y++) {
    if (x == line) {
      stdout.write('*');
      continue;
    }
    makeHole(y, finish);
  }
}

void makeHole(int start, int finish) {
  if (start == 1 || start == finish) {
    stdout.write('*');
  } else {
    stdout.write(' ');
  }
}

void printSpace(int n, int line) {
  for (var y = 1; y <= n - line; y++) {
    stdout.write(' ');
  }
}

void triangle6(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStartWithHole(x, n, 2 * (x - 1) + 1);
    print('');
  }
}

void main() {
  print('');

  int n;
  stdout.write('输入 n : ');
  n = int.parse(stdin.readLineSync()!);
  triangle6(n);

  print('');
}
