import java.util.Scanner;

public class J05_Function {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Write your message: ");
        String message = scanner.nextLine();

        // Call function 'showMessage'
        showMessage(message);
    }
    private static void showMessage(String msg) {
        System.out.println("Message: "+ msg);
    }
}
