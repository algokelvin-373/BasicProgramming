// function

void main() {
  Map<int, String> map = {
    1: 'Dart',
    2: 'Kotlin',
    3: 'Java'
  };

  // Set Map Key and Map Value using 'foreach'
  map.forEach((key, value) {
    print('$key => $value');
  });

}