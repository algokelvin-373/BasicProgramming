import java.util.Scanner;

public class CSJ02_DeretHitung {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        MenuDeretHitung();
        int in = input.nextInt();
        Calculate(in, input);
    }

    private static void MenuDeretHitung() {
        System.out.println("Deret Hitung:");
        System.out.println("1. Arithmetic");
        System.out.println("2. Geometry");
        System.out.print("Pilih: ");
    }

    private static void Calculate(int in, Scanner input) {
        System.out.print("Input a: ");
        int a = input.nextInt();
        System.out.print("Input n: ");
        int n = input.nextInt();

        if (in == 1) {
            DeretAritmatika(a, n, input);
        } else if (in == 2) {
            DeretGeometri(a, n, input);
        } else {
            System.out.println("This is not available");
        }

    }

    private static void DeretAritmatika(int a, int n, Scanner input) {
        System.out.print("Input b: ");
        int b = input.nextInt();

        for (int x = 1; x <= n; x++) {
            System.out.print(a + " ");
            a += b;
        }
        System.out.println();
    }

    private static void DeretGeometri(int a, int n, Scanner input) {
        System.out.print("Input r: ");
        int r = input.nextInt();

        for (int x = 1; x <= n; x++) {
            System.out.print(a + " ");
            a *= r;
        }
        System.out.println();
    }

}
