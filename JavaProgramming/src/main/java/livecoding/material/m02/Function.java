package material.m02;

public class Function {
    public static void main(String[] args) {
        // fundamentals.others.Function - f(x) = x + 1
        setFunction(2);
        setFunction(4);
        setMessage("I learn coding Java");
        setNoParameter();
        setFunction(30);
    }
    public static void setFunction(int x) {
        int result = x + 1;
        System.out.println("f("+ x +") = "+ result);
    }
    public static void setMessage(String message) {
        System.out.println("Your message: "+ message);
    }
    public static void setNoParameter() {
        System.out.println("This is function no parameter");
    }
}
