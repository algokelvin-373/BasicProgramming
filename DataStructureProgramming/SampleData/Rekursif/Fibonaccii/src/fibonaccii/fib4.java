package fibonaccii;

public class fib4 {

    public static void main(String[] args) {
        long N = 4;
        for (int i = 1; i <= N; i++) {
            System.out.println(i + " : " + fib4(i));
        }
    }
    
    public static long fib4(int n){
        return fiboHelp(0,1,n);
    }
    
    public static long fiboHelp(long x, long y, int n) {
        if(n==0) return x;
        else if(n==1) return y;
        else return fiboHelp(y,x+y,n-1);
    }
}
