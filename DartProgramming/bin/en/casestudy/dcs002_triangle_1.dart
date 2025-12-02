import 'dart:io';

void main() {
  print('');

  int n;
  stdout.write('Input n : ');
  n = int.parse(stdin.readLineSync()!);

  for (var x = 1; x <= n; x++) {
    for (var y1 = 1; y1 <= n - x; y1++) {
      stdout.write(' ');
    }
    for (var y2 = 1; y2 <= x; y2++) {
      stdout.write('*');
    }
    print('');
  }

  print('');
}
