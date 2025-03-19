package SOLID_Principle.abstraction;

abstract class ShapeTwo {
    public double area(double radius) { // Area of Circle
        return Math.PI * radius * radius;
    }
    public int area(int width, int height) { // Area of Rectangle
        return width * height;
    }
}
