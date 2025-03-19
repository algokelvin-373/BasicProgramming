package material.m05;

public class StringObject {
    public static void main(String[] args) {
        // Sample
        String stringNumber = "14590";
        String stringWord = "coding";

        String stringSample1 = "I Love Coding Java";

        // Change to UpperCase
        String str1 = stringSample1.toUpperCase();

        // Change to LowerCase
        String str2 = stringSample1.toLowerCase();

        System.out.println("str1: "+str1);
        System.out.println("str2: "+str2);

        // Get 'Love'
        String str3 = stringSample1.substring(2, 6);
        System.out.println("str3: "+str3);
        // Get 'Java'
        String str4 = stringSample1.substring(14, 18);
        System.out.println("str4: "+str4);
        // Get 'Love Coding Java'
        String str5 = stringSample1.substring(2);
        System.out.println("str5: "+str5);

        // Replace 'Java' to 'Kotlin'
        String str6 = stringSample1.replace("Java", "Kotlin");
        System.out.println("str6: "+str6);

        // charAt - charAt(0) = I
        char char1 = stringSample1.charAt(0);
        System.out.println("char1: "+char1);

        // Convert to String
        int number = 2300;
        String str7 = String.valueOf(number);
        System.out.println("str 7: "+str7);
        System.out.println(str7 instanceof String);
    }
}
