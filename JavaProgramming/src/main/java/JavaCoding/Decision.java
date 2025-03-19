import java.util.Scanner;

public class Decision {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input your score Math: ");
        int score = input.nextInt();

        if (score >= 90) {
            System.out.println("Congratulations. You get a bicycle");
        } else {
            System.out.println("Sorry, you are not lucky today");
        }

    }
}
