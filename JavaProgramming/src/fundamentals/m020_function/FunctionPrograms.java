package fundamentals.m020_function;
import java.util.Scanner;

public class FunctionPrograms {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Write your message: ");
        String message = scanner.nextLine();

        functionMethod01();
        functionMethod02(message);
        System.out.println(functionMethod03());
        System.out.println(functionMethod04(message));
    }

    // function: Not Result No Parameter
    private static void functionMethod01() {
        System.out.println("Function No Result No Parameter");
        System.out.println("Show Data Message");
    }

    // function: Not Result, With Parameter
    private static void functionMethod02(String message) {
        System.out.println("Function No Result, With Parameter");
        System.out.println("Data: "+ message);
    }

    // function: With Result, No Parameter
    private static String functionMethod03() {
        return "Function with Result, No Parameter";
    }

    // function: With Result and Parameter()
    private static String functionMethod04(String message) {
        return "With Return and Parameter, Message: "+ message;
    }
}
