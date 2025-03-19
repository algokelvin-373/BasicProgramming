void setup() {
  size(250, 250);
}

void draw() {
  int radius = 10; // Set radius
  
  // Draw Rectangle: width = 225, height = 75
  fill(255, 100, 100); // Set fill rectangle
  stroke(100, 100, 255); // Set stroke line rectangle
  strokeWeight(5);
  rect(10, 10, 225, 75, radius); // Start on (10, 10)
  
  // Draw Circle: diameter = 125
  int dCircle = 125;
  fill(50, 255, 50); // Set fill circle
  stroke(255, 50, 50); // Set stroke line circle
  strokeWeight(10);
  circle(150, 175, dCircle); // Start on (10, 100)
}
