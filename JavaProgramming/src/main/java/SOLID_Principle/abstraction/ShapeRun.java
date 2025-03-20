package SOLID_Principle.abstraction;

public class ShapeRun {
    public static void main(String[] args) {
        Circle circle = new Circle(7.0);
        Rectangle rectangle = new Rectangle(10, 20);
        System.out.println("Area Circle    : "+ circle.area());
        System.out.println("Area Rectangle : "+ rectangle.area());
    }
}
