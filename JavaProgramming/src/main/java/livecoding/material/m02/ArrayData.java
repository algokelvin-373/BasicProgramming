package material.m02;

public class ArrayData {
    public static void main(String[] args) {
        // Array Data
        int[] number = {10, 20, 30, 40, 50}; // data array number
        // size = 5, last index = 4

        String[] code = {"Java", "Kotlin", "Python"}; // data array string

        System.out.println(number[2]);

        // looping for
        for (int x = 0; x < code.length; x++) {
            System.out.println(code[x]);
        }

        number[1] = 200;
        System.out.println(number[1]);

    }
}
