import 'dart:io';

void main() {
  print('');

  int number;
  stdout.write('输入数字 : ');
  number = int.parse(stdin.readLineSync()!);

  switch (number) {
    case 1:
      print('一月');
      break;
    case 2:
      print('二月');
      break;
    case 3:
      print('三月');
      break;
    case 4:
      print('四月');
      break;
    case 5:
      print('五月');
      break;
    case 6:
      print('六月');
      break;
    case 7:
      print('七月');
      break;
    case 8:
      print('八月');
      break;
    case 9:
      print('九月');
      break;
    case 10:
      print('十月');
      break;
    case 11:
      print('十一月');
      break;
    case 12:
      print('十二月');
      break;
    default:
      print('Error');
      break;
  }

  print('');
}
