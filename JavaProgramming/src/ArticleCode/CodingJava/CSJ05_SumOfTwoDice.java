import java.util.Scanner;

public class CSJ05_SumOfTwoDice {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input n: ");
        int n = input.nextInt();
        int[][] dice = new int[n][n];
        SumOfTwoDice(dice);
    }

    private static void SumOfTwoDice(int[][] dice) {
        // Show header
        System.out.print("+ |");
        for (int i = 1; i <= dice.length; i++) {
            System.out.printf(" %2d", i);
        }
        System.out.println();
        // Set Array Two Dice
        for (int x = 1; x <= dice.length; x++) {
            for (int y = 1; y <= dice[x-1].length; y++) {
                dice[x-1][y-1] = x + y;
            }
        }
        // Show Sum Of Two Dice
        for (int x = 0; x < dice.length; x++) {
            System.out.print((x+1) + " |");
            for (int y = 0; y < dice[x].length; y++) {
                System.out.printf(" %2d", dice[x][y]);
            }
            System.out.println();
        }
    }
}
