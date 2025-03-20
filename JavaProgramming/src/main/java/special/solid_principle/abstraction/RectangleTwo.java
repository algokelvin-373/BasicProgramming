package special.solid_principle.abstraction;

public class RectangleTwo extends ShapeTwo {
    private final int width;
    private final int height;

    public RectangleTwo(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int calculateArea() {
        return super.area(width, height);
    }
}
