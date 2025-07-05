import 'dart:io';

void triangleTypeOne(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStar(x);
    print('');
  }
}

void triangleTypeTwo(int n) {
  for (var x = 1; x <= n; x++) {
    printStar(x);
    print('');
  }
}

void triangleTypeThree(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStar(2 * (x - 1) + 1);
    print('');
  }
}

void triangleTypeFour(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStartWithHole(x, n, x);
    print('');
  }
}

void triangleTypeFive(int n) {
  for (var x = 1; x <= n; x++) {
    printStartWithHole(x, n, x);
    print('');
  }
}

void triangleTypeSix(int n) {
  for (var x = 1; x <= n; x++) {
    printSpace(n, x);
    printStartWithHole(x, n, 2 * (x - 1) + 1);
    print('');
  }
}

void printSpace(int n, int line) {
  for (var y = 1; y <= n - line; y++) {
    stdout.write(' ');
  }
}

void printStar(int x) {
  for (var y = 1; y <= x; y++) {
    stdout.write('*');
  }
}

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

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);

  int choose;
  stdout.write('Type Triangle : ');
  choose = int.parse(stdin.readLineSync()!);

  switch (choose) {
    case 1:
      triangleTypeOne(n);
      break;
    case 2:
      triangleTypeTwo(n);
      break;
    case 3:
      triangleTypeThree(n);
      break;
    case 4:
      triangleTypeFour(n);
      break;
    case 5:
      triangleTypeFive(n);
      break;
    case 6:
      triangleTypeSix(n);
      break;
    default:
      print('Not have item');
  }

  print('');
}
