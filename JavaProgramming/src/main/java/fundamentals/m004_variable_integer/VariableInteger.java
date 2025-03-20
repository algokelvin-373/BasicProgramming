package fundamentals.m004_variable_integer;

public class VariableInteger {
    public static void main(String[] args) {
        byte byteNum = 100;
        // byte byteNum = 128; -> Error, byte numbers from -128 to 127

        short shortNum = 10000;
        // short shortNum = 32768; -> Error, short numbers from -32768 to 32767

        System.out.println(byteNum);
        System.out.println(shortNum);
    }
}
