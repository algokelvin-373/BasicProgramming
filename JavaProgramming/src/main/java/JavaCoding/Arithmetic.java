public class Arithmetic {
    public static void main(String[] args) {
        // 1, 3, 5, 7, 9 => 1001 algoritma
        // Cara 1:
        for (int x = 1; x <= 10; x += 1) {
            System.out.println("Nilai x skrg: "+ x);
            if (x % 2 == 1) {
                System.out.println(x);
            }
            System.out.println("Selesai Eksekusi untuk x = "+ x);
        }
        // Cara 2: (just basic to show data)
        System.out.println("1 3 5 7 9");
        // Cara 3: 
        //|( x += 1 => x = x + 1 | x = 1 | x' = 1 + 1 = 2 )
        for (int x = 1; x <= 10; x += 2) {
            System.out.println(x);
        }
    }
}
