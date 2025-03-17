package m006_variable_narrowing_casting;

public class VariableNarrowingCasting {
    public static void main(String[] args) {
        // Narrowing Casting (manually)
        // converting a larger type to a smaller size type
        double doubleA = 3.14;
        float floatA = (float) doubleA;
        int intA = (int) floatA;
        System.out.println(doubleA);
        System.out.println(floatA);
        System.out.println(intA);
    }
}
