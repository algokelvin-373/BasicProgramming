import 'dart:io';
import '../casestudy/dcs002_triangle_1.dart';
import '../casestudy/dcs003_triangle_2.dart';
import '../casestudy/dcs004_triangle_3.dart';
import '../casestudy/dcs005_triangle_4.dart';
import '../casestudy/dcs006_triangle_5.dart';
import '../casestudy/dcs007_triangle_6.dart';

void main() {
  print('');

  int n;
  stdout.write('输入 n : ');
  n = int.parse(stdin.readLineSync()!);

  int choose;
  stdout.write('Type Triangle : ');
  choose = int.parse(stdin.readLineSync()!);

  switch (choose) {
    case 1:
      triangle1(n);
      break;
    case 2:
      triangle2(n);
      break;
    case 3:
      triangle3(n);
      break;
    case 4:
      triangle4(n);
      break;
    case 5:
      triangle5(n);
      break;
    case 6:
      triangle6(n);
      break;
    default:
      print('Not have item');
  }

  print('');
}
