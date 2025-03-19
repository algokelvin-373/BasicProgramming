import java.util.Scanner;

public class Function {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input message: ");
        String msg = input.nextLine();

        // Call function 'showMessage'
        showMessage(msg);
    }
    // Create function
    private static void showMessage(String msg) {
        System.out.println("Message: "+ msg);
    }
}
