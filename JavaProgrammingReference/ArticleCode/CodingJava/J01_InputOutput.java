import java.util.Scanner;

public class J01_InputOutput {
    public static void main(String[] args) {
        
        // Scanner for create input data
        Scanner scanner = new Scanner(System.in);
        
        // Step for input data
        System.out.print("Input Your Name: ");
        String name = scanner.nextLine();

        // Step for output data
        System.out.println("Your name: " + name);


    }
}
