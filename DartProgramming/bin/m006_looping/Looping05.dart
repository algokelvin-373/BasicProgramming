//Break
import 'dart:io';

void main() {
  //Arithmetic: 1, 2, 3, 4, ...
  print('Deret Arithmetic : ');
  stdout.write('Input n : ');
  int n = int.parse(stdin.readLineSync()!);

  for (int x = 1; x <= n; x++) {
    if (x % 2 == 0 && x % 7 == 0) {
      break;
    }
    stdout.write('$x, ');
  }
}