import java.util.Scanner;

public class JavaInputOutput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input Your Name: ");
        String name = input.nextLine();

        System.out.println("Name : "+ name);

    }
}
