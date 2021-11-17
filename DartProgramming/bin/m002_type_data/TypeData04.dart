// Type Data 'var'
void main() {
  int a = 373;
  String b = "AlgoKelvin";

  // Set var x to initialize a
  var x = a;
  print('var x: '+ x.toString());

  // x = b; -> Error (should be different variable)
  // Set var y to initialize b
  var y = b;
  print('var y: '+ y); // Because y is 'String'
}