package material.m04;

public class MaximumProgram {
    public static void main(String[] args) {
        // 3, 7, 2, 5, 4 --> max = 7
        int[] dataNum1 = {234, 543, 122, 897, 435, 324};

        // fundamentals.others.Looping
        int max1 = 0;
        for (int index = 0; index < dataNum1.length; index++) {
            if (index == 0) max1 = dataNum1[index];
            else {
                // Set maximum value
                if (max1 < dataNum1[index]) {
                    max1 = dataNum1[index];
                }
            }
        }
        System.out.println("234, 543, 122, 897, 435, 324");
        System.out.println("Max 1: "+ max1);
    }
}
