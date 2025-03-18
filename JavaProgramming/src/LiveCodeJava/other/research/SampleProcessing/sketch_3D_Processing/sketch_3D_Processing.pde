void setup() {
  size(400, 200, P3D);
}

void draw() {
  translate(100, 100, 0);
  noFill();
  box(75); // x = 75, y = 75, z = 75
  
  translate(175, 5, 0);
  noFill();
  box(100, 125, 75); // x = 200, y = 50, z = 75
}
