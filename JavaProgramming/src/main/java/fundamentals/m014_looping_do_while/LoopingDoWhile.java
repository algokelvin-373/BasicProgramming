package fundamentals.m014_looping_do_while;

public class LoopingDoWhile {
    public static void main(String[] args) {
        int n = 10, x = 0;
        do {
            System.out.print((x + 1) + " ");
            x++;
        }
        while (x < n);
    }
}
