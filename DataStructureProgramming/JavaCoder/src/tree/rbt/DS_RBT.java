package tree.rbt;

import java.util.Scanner;

public class DS_RBT {

    public static void main(String[] args) {
        @SuppressWarnings("empty-statement")
        Scanner scan = new Scanner(System.in);
        RBT rbt = new RBT(Integer.MIN_VALUE);
        char ch; int in;
        for (;;) {
            System.out.println("\nRed Black Tree Operations\n");
            System.out.println("1. Ascending ");
            System.out.println("2. Descending ");
            System.out.println("3. search");
            System.out.println("4. count nodes");
            System.out.println("5. check empty");
            System.out.println("6. clear tree");
            System.out.println("7. exit");
            System.out.println("Pilihan : ");
            int choice = scan.nextInt();
            switch (choice) {
                case 1:

                    break;
                case 2:
                    
                    break;
                case 3:
                    
                    break;
                case 4:
                    
                    break;
                case 5:
                    
                    break;
                case 6:
                    
                    break;
                case 7:
                    
                default:
                    break;
            }
            /*  Display tree  */
            if (choice == 7) {
                break;
            }
        } 
    }
}