import java.util.Scanner;

public class J03_Repeat {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Input n: ");
        int n = scanner.nextInt();

        // Repeat Program
        for (int x = 1; x <= n; x++) {
            System.out.print(x + " ");
        }
        System.out.println();

    }
}
