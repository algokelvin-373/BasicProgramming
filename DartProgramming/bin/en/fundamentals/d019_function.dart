// Without Parameter
String showTitle() {
  return "Add Two Number";
}

// With Parameter
String showMyName(int num1, int num2) {
  int result = num1 + num2;
  return "$num1 + $num2 = $result";
}

void main() {
  print('');

  // Function with return data
  print(showTitle());
  print(showMyName(5, 3));

  print('');
}
