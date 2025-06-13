void main() {
  print('');

  int a = 3;
  int b = 4;
  double c = 25;

  print('算术运算符');
  print('$a + $b = ${a + b}'); // 加
  print('$a - $b = ${a - b}'); // 减
  print('$a * $b = ${a * b}'); // 乘
  print('$b / $a = ${b / a}'); // 除
  print('$b % $a = ${b % a}'); // 取模
  print('$c ~/ $a = ${c ~/ a}');

  print('');

  print('前递增运算符');
  print('之前 a 的值 : $a');
  print('前递增运算  : ${++a}');
  print('现在 a 的值 : $a');

  print('');

  print('后递增运算符');
  print('之前 b 的值 : $b');
  print('后递增运算  : ${b++}');
  print('现在 b 的值 : $b');

  print('');
}
