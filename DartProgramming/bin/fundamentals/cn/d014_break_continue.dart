void main() {
  print('');

  int j1 = 3;
  int j2 = 6;
  for (var i = 1; i <= 10; i++) {
    if (i == j1) {
      continue;
    } else if (i == j2) {
      break;
    } else {
      print("$i ");
    }
  }

  print('');
}
