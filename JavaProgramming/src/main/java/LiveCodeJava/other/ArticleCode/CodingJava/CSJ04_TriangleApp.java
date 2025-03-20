import java.util.Scanner;
public class CSJ04_TriangleApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input sisi: ");
        int s = input.nextInt();
        MenuTriangle(s, input);
    }

    private static void MenuTriangle(int s, Scanner input) {
        System.out.println("Menu Triangle:");
        System.out.println("1. Triangle Type 1");
        System.out.println("2. Triangle Type 2");
        System.out.println("3. Triangle Type 3");
        System.out.print("Pilih: ");
        int a = input.nextInt();

        if (a == 1) {
            TriangleType1(s);
        } else if (a == 2) {
            TriangleType2(s);
        } else if (a == 3) {
            TriangleType3(s);
        } else {
            System.out.println("This is not available");
        }
    }

    private static void TriangleType1(int s) {
        for (int x = 0; x < s; x++) {
            for (int y = 0; y <= x; y++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    private static void TriangleType2(int s) {
        for (int x = 0; x < s; x++) {
            // Set print space
            for (int y = 0; y < (s-1)-x; y++) {
                System.out.print(" ");
            }
            // Set print star
            for (int z = 0; z < 2*x + 1; z++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    private static void TriangleType3(int s) {
        for (int x = 0; x < s; x++) {
            // Set print space
            for (int y = 0; y < x; y++) {
                System.out.print(" ");
            }
            // Set print star
            for (int z = s-x; z > 0; z--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}
