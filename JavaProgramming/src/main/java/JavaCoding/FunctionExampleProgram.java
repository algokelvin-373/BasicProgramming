import java.util.Scanner;

public class FunctionExampleProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input message: ");
        String message = input.nextLine();
        showMessage(message);
    }
    private static void showMessage(String message) {
        System.out.println("Your message: "+ message);
    }
}
