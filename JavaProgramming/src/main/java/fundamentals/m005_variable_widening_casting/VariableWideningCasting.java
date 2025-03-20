package fundamentals.m005_variable_widening_casting;

public class VariableWideningCasting {
    public static void main(String[] args) {
        // Widening Casting (automatically)
        // converting a smaller type to a larger type size
        int intA = 373;
        float floatA = intA;
        double doubleA = floatA;
        System.out.println(intA);
        System.out.println(floatA);
        System.out.println(doubleA);
    }
}
