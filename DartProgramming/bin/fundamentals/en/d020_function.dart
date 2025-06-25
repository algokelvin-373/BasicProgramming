// Without Parameter (One Expression)
String showTitle() => "Add Two Number";

// With Parameter (One Expression)
String showMyName(int num1, int num2) => "$num1 + $num2 = ${num1 + num2}";

void main() {
  print('');

  // Function with return data
  print(showTitle());
  print(showMyName(5, 3));

  print('');
}
