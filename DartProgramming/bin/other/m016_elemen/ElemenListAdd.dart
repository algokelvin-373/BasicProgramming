// Element 'list'

void main() {
  List<int> listInt = [1, 2, 3];

  print(listInt.elementAt(0));
  print(listInt.elementAt(1));
  print(listInt.elementAt(2));

  // Add element
  listInt.add(4);
  print(listInt.elementAt(3));

  // Add another list
  List<int> listInt2 = [5, 6];
  listInt.addAll(listInt2);
  print(listInt.elementAt(4));
  print(listInt.elementAt(5));

}