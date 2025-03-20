package fundamentals.others;

import java.util.Scanner;

public class Looping {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input n: ");
        int n = input.nextInt();

        // fundamentals.others.Looping for
        for (int x = 0; x < n; x++) {
            System.out.print((x+1) + " ");
        }
        System.out.println("Done");

    }
}
