//Function in function
void main() {
  func("AlgoKelvin", 3);
}

void func(String msg, int s) {
  welcome(msg);
  areaRectangle(s);
}

String welcome(String msg) => 'Welcome, $msg';
int areaRectangle(int s) => s * s;