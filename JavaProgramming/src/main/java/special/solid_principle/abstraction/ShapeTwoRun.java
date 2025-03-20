package special.solid_principle.abstraction;

public class ShapeTwoRun {
    public static void main(String[] args) {
        CircleTwo circle = new CircleTwo(7.0);
        RectangleTwo rectangle = new RectangleTwo(10, 20);
        System.out.println("Area Circle    : "+ circle.calculateArea());
        System.out.println("Area Rectangle : "+ rectangle.calculateArea());
    }
}
