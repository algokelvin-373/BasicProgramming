import java.util.Scanner;

public class InputOutput {
    public static void main(String[] args) {
        // import scanner to create input program
        Scanner input = new Scanner(System.in);

        // Input Program
        System.out.print("Input Your Name: ");
        String name = input.nextLine();

        // Output Program
        System.out.println("Name: "+ name);

    }
}
