package special.solid_principle.abstraction;

public class Circle extends Shape {
    private final double radius;

    public Circle (double radius) {
        this.radius = radius;
    }
    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}
