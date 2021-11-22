//Function using '=>'
void main() {
  print(welcome());
  print(areaRectangle(3));
  func("AlgoKelvin", 3);
}
String welcome() => 'Welcome, AlgoKelvin';
int areaRectangle(int s) => s * s;

// '=>' isn't work for 2 lines
void func(String msg, int s) {
  print('Welcome, $msg');
  print(s * s);
}