//Type Data 'dynamic'
void main() {
  int a = 273; // integer
  double b = 3.14; // double
  int hex = 0xff; // integer in hexa
  String c = "AlgoKelvin"; // string
  bool d = true; // boolean

  //'dynamic' can be defined all type data
  dynamic dy = a; print('dynamic - a : '+ dy.toString());
  dy = b; print('dynamic - b : '+ dy.toString());
  dy = c; print('dynamic - c : '+ dy.toString());
  dy = d; print('dynamic - d : '+ dy.toString());
  dy = hex; print('dynamic - hex : '+ dy.toString());
}