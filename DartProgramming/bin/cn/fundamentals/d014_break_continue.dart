void main() {
  print('');

  int j1 = 6;
  int j2 = 4;
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
