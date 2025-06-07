// Operator 'is' '!is'

void main() {
  var a = 10, b = 3.15;

  print(a is int); // true
  print(b is int); // false

  print(a is! int); // false
  print(b is! int); // true

}