// Element 'list'

void main() {
  List<int> listInt = [1, 2, 3, 4, 5];

  // Remove element
  listInt.removeAt(2);
  listInt.removeLast();
  print(listInt.elementAt(0));
  print(listInt.elementAt(1));
  print(listInt.elementAt(2));
  // print(listInt.elementAt(3)); --> Error: length now = 3, no 5 again
  // print(listInt.elementAt(4)); --> Error: length now = 3, no 5 again

}