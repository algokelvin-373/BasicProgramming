
// Set size layer -> width = 200, height = 100
void setup() {
  size(200, 100);
}

// Set draw object
void draw() {
  // Draw Point
  point(50, 25);
  point(100, 25);
  point(150, 25);
  
  // Draw Line
  drawLine(0, 50, 50, 50);
  drawLineStroke(50, 75, 100, 75, 255, 0, 0);
  drawLineWeight(100, 50, 150, 100, 2);
  drawLineStrokeWeight(150, 75, 200, 50, 0, 0, 255, 2);
}

void drawLine(int x1, int y1, int x2, int y2) {
  line(x1, y1, x2, y2);
  stroke(0);
  strokeWeight(0);
}
void drawLineStroke(int x1, int y1, int x2, int y2, int r, int g, int b) {
  stroke(r, g, b);
  drawLine(x1, y1, x2, y2);
}
void drawLineWeight(int x1, int y1, int x2, int y2, int w) {
  strokeWeight(w);
  drawLine(x1, y1, x2, y2);
}
void drawLineStrokeWeight(int x1, int y1, int x2, int y2, int r, int g, int b, int w) {
  stroke(r, g, b);
  strokeWeight(w);
  drawLine(x1, y1, x2, y2);
}
