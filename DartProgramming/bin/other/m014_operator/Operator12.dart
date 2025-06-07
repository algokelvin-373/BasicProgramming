// Operator 'as'

void main() {
  num b = 3, c = 4.567;

  // set 'as' integer to use 'isOdd'
  print((b as int).isEven);

  // set 'as' double to use 'round'
  print((c as double).round());

}