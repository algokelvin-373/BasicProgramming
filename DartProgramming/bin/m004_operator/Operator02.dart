//Operator Increment
void main() {
  int x = 0;

  //Pre-Increment "++x"
  //Plus 1, then, print data
  print('Value x before: $x');
  print('Pre-increment : ${++x}');
  print('Value x after : $x');

  //Post-Increment ""
  //Print data, then, plus 1
  print('Value x before: $x');
  print('Post-increment : ${x++}');
  print('Value x after : $x');
}