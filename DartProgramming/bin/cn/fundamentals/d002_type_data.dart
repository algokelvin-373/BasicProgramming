void main() {
  print('');

  int dataInt = 100;
  double dataDouble = 3.14;
  String dataStr = "我是Kelvin。";
  bool dataBool = true;

  // num
  num dataNum = dataInt;
  print('数据 num (Int)    : ' + dataNum.toString());
  dataNum = dataDouble;
  print('数据 num (Double) : ' + dataNum.toString());

  // var
  var dataVar = dataInt;
  print('数据 var (int1)   : ' + dataVar.toString());
  dataVar = 200;
  print('数据 var (int2)   : ' + dataVar.toString());

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
