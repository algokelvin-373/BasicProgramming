package special.solid_principle.abstraction;

public class CircleTwo extends ShapeTwo {
    private final double radius;

    public CircleTwo(double radius) {
        this.radius = radius;
    }

    public double calculateArea() {
        return super.area(radius);
    }
}
