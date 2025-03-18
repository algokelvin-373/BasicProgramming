import java.util.Scanner;

public class CSJ03_RectangleApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Input s: ");
        int s = input.nextInt();
        CreateRectangle(s);
    }

    private static void CreateRectangle(int s) {
        System.out.println("Rectangle (n = "+ s + ")");
        for (int x = 0; x < s; x++) {
            for (int y = 0; y < s; y++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}
