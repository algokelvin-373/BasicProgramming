package fibonaccii;

public class Fib2 {
    
    public static long fib2(int n){
        if (n<=1) return n;
        else return fib2(n-1)+ fib2(n-2);
    }
    
    public static void main(String[] args) {
        long N = 4;
        for(int i=1; i <= N; i++)
            System.out.println(i+ " : " + fib2(i));
    }
    
}
