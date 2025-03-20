package material.m06;

public class MethodsProgram {
    public static void main(String[] args) {
        showMessage(); // function type 1
        inputYourName("Kelvin"); // function type 2
        String message = getMessage(); // function type 3
        int result = add(10, 20); // function type 4

        System.out.println(message);
        System.out.println(result);
    }

    /*
    parameter = input untuk proses program di fungsi tertentu
    pengembalian data = output dari hasil proses program fungsi itu.
     */

    // 1. Tanpa parameter dan pengembalian data
    public static void showMessage() {
        System.out.println("Good Morning");
    }

    // 2. Pakai parameter, tidak pakai pengembalian data
    public static void inputYourName(String name) {
        System.out.println("Your name: "+ name);
    }

    // 3. Pakai pengembalian data, tidak pakai parameter
    public static String getMessage() {
        return "Selamat Pagi dan Selamat Datang di Channel AlgoKelvin";
    }

    // 4. Pakai parameter dan pengembalian data
    public static int add(int angka1, int angka2) {
        return angka1 + angka2;
    }

}
