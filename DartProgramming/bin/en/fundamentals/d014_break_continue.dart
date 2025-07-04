void main() {
  print('');

  // Show Number 1 - 10
  int j1 = 3;
  int j2 = 6;
  for (var i = 1; i <= 10; i++) {
    if (i == j1) {
      continue; // Next Loop
    } else if (i == j2) {
      break; // Stop Loop
    } else {
      print("$i ");
    }
  }

  print('');
}
