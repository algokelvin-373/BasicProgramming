//Operator Logic 'AND'
void main() {
  bool p = true, q = false;
  print('* Operator AND :');
  print('* $p && $p = ${p && p}');
  print('* $p && $q = ${p && q}');
  print('* $q && $p = ${q && p}');
  print('* $q && $q = ${q && q}');
}