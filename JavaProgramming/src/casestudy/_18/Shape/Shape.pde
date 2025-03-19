void setup() {
  size(250, 250);
}

void draw() {
  // Shape 1
  int[][] shapes1 = { {10, 10}, {125, 10}, {125, 215}, {10, 215} };
  int[] colors1 = {255, 100, 100};
  drawShape(shapes1, colors1);
  
  // Shape 2
  int[][] shapes2 = { {135, 25}, {235, 45}, {225, 200}, {145, 215} };
  int[] colors2 = {100, 50, 255};
  drawShape(shapes2, colors2);
}

void drawShape(int[][] shapes, int[] colors) {
  beginShape();
  for (int x = 0; x < shapes.length; x++) {
    vertex(shapes[x][0], shapes[x][1]);
  }
  fill(colors[0], colors[1], colors[2]);
  endShape(CLOSE);
}
