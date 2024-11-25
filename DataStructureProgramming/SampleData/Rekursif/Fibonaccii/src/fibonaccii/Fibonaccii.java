package fibonaccii;

public class Fibonaccii {
    
    public static long fib1(int n){
        if (n == 0) return n;
        else if (n == 1) return n;
        else {
            long x = 0;
            long y = 1;
            for (long k = 2 ; k <= n; k++){
                y = x + y;
                x = y - x;
        }
            return y;
        }
    }

    public static void main(String[] args) {
        long N = 10;
        for(int i=1; i <= N; i++)
            System.out.println(i+ " : " + fib1(i));
    }
    
}
