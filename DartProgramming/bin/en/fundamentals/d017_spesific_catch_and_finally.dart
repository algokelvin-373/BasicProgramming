import 'dart:io';

void main() {
  print('');

  double number1, number2;
  int countError = 0;

  try {
    stdout.write('Input number 1 : ');
    number1 = double.parse(stdin.readLineSync()!);
    stdout.write('Input number 2 : ');
    number2 = double.parse(stdin.readLineSync()!);

    double result = number1 / number2;
    print("$number1 / $number2 = $result");
  } on FormatException catch (e) {
    countError++;
    print('Get Error: ${e.message}');
  } finally {
    print('Done');
    if (countError == 0) {
      print('No Error');
    } else {
      print('Get $countError Error');
    }
  }

  print('');
}
