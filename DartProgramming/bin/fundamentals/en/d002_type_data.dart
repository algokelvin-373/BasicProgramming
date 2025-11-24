void main() {
  print('');

  int dataInt = 100;
  double dataDouble = 3.14;
  String dataStr = "My Name is Kelvin";
  bool dataBool = true;

  // num
  num dataNum = dataInt;
  print('Data Num (Int)    : ' + dataNum.toString());
  dataNum = dataDouble;
  print('Data Num (Double) : ' + dataNum.toString());

  // var
  var dataVar = dataInt;
  print('Data var (int1)   : ' + dataVar.toString());
  dataVar = 200;
  print('Data var (int2)   : ' + dataVar.toString());

  // dynamic
  dynamic dataDynamic = dataInt;
  print('dynamic - int     : ' + dataDynamic.toString());
  dataDynamic = dataDouble;
  print('dynamic - double  : ' + dataDynamic.toString());
  dataDynamic = dataStr;
  print('dynamic - String  : ' + dataDynamic.toString());
  dataDynamic = dataBool;
  print('dynamic - boolean : ' + dataDynamic.toString());

  print('');
}
