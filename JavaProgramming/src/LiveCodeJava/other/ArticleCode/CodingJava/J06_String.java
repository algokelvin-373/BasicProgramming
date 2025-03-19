public class J06_String {
    public static void main(String[] args) {
        String word = "AlgoKelvin - Class Online Private Coding";

        System.out.println("Index String [5] = "+ word.charAt(5));
        System.out.println("Index String [last] = "+ word.charAt(word.length()-1));
        System.out.println("Substring [0] - [9] = "+ word.substring(0, 10));
        System.out.println("Substring [13] - last = "+ word.substring(13));
        System.out.println("Lowercase = "+ word.toLowerCase());
        System.out.println("Uppercase = "+ word.toUpperCase());
        System.out.println("Replace 'a' to 'e' = "+ word.replace("a", "e"));
        System.out.println("Replace 'Kelvin' to 'kvn' = "+ word.replace("Kelvin", "kvn"));
    }
}
