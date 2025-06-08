void main() {
  print('');

  int a = 3;
  int b = 4;
  double c = 25;

  print('Operator Arithmatic');
  print('$a + $b = ${a + b}'); // plus
  print('$a - $b = ${a - b}'); // minus
  print('$a * $b = ${a * b}'); // times
  print('$b / $a = ${b / a}'); // divided by
  print('$b % $a = ${b % a}'); // modulo
  print('$c ~/ $a = ${c ~/ a}');

  print('');

  print('Operator pre-increment');
  print('Value a before : $a');
  print('Pre-increment  : ${++a}');
  print('Value a now    : $a');

  print('');

  print('Operator post-increment');
  print('Value b before : $b');
  print('Pre-increment  : ${++b}');
  print('Value b now    : $b');

  print('');
}
