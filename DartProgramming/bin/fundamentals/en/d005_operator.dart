void main() {
  print('');

  int a = 10, b = 20, c = 10, d = 30, e = 30, f = 5;

  print('Operator Relational');

  print('Equal to (=)');
  print('* $a == $b -> ${a == b}');
  print('* $a == $c -> ${a == c}');

  print('Not Equal to (!=)');
  print('* $a != $b -> ${a != b}');
  print('* $a != $c -> ${a != c}');

  print('Bigger than (>)');
  print('* $d > $a -> ${d > a}');
  print('* $d > $e -> ${d > e}');
  print('* $a > $d -> ${a > d}');

  print('Bigger or Equal to (>=)');
  print('* $d >= $a -> ${d >= a}');
  print('* $d >= $e -> ${d >= e}');
  print('* $a >= $d -> ${a >= d}');

  print('Smaller than (<)');
  print('* $a < $e -> ${a < e}');
  print('* $a < $c -> ${a < c}');
  print('* $a < $f -> ${a < f}');

  print('Smaller or Equal to (<=)');
  print('* $a <= $e -> ${a <= e}');
  print('* $a <= $c -> ${a <= c}');
  print('* $a <= $f -> ${a <= f}');

  print('');

  bool b1 = true, b2 = false;

  print('Operator Logical');

  print('AND (&&) :');
  print('* $b1 && $b1 = ${b1 && b1}');
  print('* $b1 && $b2 = ${b1 && b2}');
  print('* $b2 && $b1 = ${b2 && b1}');
  print('* $b2 && $b2 = ${b2 && b2}');

  print('OR (||) :');
  print('* $b1 || $b1 = ${b1 || b1}');
  print('* $b1 || $b2 = ${b1 || b2}');
  print('* $b2 || $b1 = ${b2 || b1}');
  print('* $b2 || $b2 = ${b2 || b2}');

  print('NOT (!) :');
  print('* !$b1 = ${!b1}');
  print('* !$b2 = ${!b2}');

  print('');
}
