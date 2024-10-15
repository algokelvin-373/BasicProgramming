package m018_string_methods;

public class StringMethods {
    public static void main(String[] args) {
        // String 1: length, uppercase, lowercase, indexOf
        String data = "Algo Kelvin";
        System.out.println("String : "+ data);
        System.out.println("Length : "+ data.length());
        System.out.println("Uppercase : "+ data.toUpperCase());
        System.out.println("Lowercase : "+ data.toLowerCase());
        System.out.println("Index of (Algo) : "+ data.indexOf("Algo"));
        System.out.println("Index of (Kelvin) : "+ data.indexOf("Kelvin"));
    }
}
