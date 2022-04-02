// Element "map"

void main() {
  Map<int, String> map = {
    1: 'Dart',
    2: 'Kotlin',
    3: 'Java'
  };

  // Set Map Key and Map Value
  var keys = map.keys;
  var values = map.values;
  map.remove(keys.elementAt(1));
  print('${keys.elementAt(0)} => ${values.elementAt(0)}');
  print('${keys.elementAt(1)} => ${values.elementAt(1)}');

}