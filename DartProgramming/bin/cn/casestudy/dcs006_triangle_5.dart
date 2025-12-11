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

void triangle5(int n) {
  for (var x = 1; x <= n; x++) {
    printStartWithHole(x, n, x);
    print('');
  }
}

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);
  triangle5(n);

  print('');
}
