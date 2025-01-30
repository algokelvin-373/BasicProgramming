
package fibonaccii;

public class Fib3 {

    public static void main(String[] args) {
        long N = 4;
        for (int i = 1; i <= N; i++) {
            System.out.println(i + " : " + fib3(i));
        }
    }
    
    public static long fib3(int n) {
        if(n<=1) return n;
        long a = 0;
        long b = 1;
        long result = 0;
        for(int x = 2; x<=n; x++) {
            result = a + b;
            a = b;
            b = result;
        } return result;
    }
}
