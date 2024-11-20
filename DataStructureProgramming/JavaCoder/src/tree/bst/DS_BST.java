package tree.bst;

/*
BST = Binary Search Tree
 */

import java.util.Scanner;

public class DS_BST {
    public static void main(String[] args) {
        int a;
        Scanner masukan = new Scanner (System.in);
        BST bst = new BST ();
        MenuPilihan();
        do {
            System.out.print ("Silahkan Pilih :");
            int pilih = masukan.nextInt();
            switch (pilih) {
                case 1  : System.out.print ("Masukan Angka : ");
                    a = masukan.nextInt();
                    bst.insert(a);
                    break;
                case 2  : System.out.print ("Masukan Angka Yang "+
                        "Ingin Dihapus : ");
                    a = masukan.nextInt();
                    bst.delete(a);
                    break;
                case 3  : System.out.print ("Masukan Angka : ");
                    a = masukan.nextInt();
                    bst.find(a);
                    break;
                case 4  : bst.deleteAll();
                    break;
                case 5  : System.out.println ("Hasil Tampilan Pre-order :");
                    bst.preorder();
                    break;
                case 6  : System.out.println ("Hasil Tampilan In-order :");
                    bst.inorder();
                    break;
                case 7  : System.out.println ("Hasil Tampilan Post-order : ");
                    bst.postorder();
                    break;
                case 8  : System.out.println ("\nBanyak Daun = "+bst.leaf());
                    break;
                case 9  : System.out.println ("\nBanyak node = "+bst.getUkuran());
                    break;
                case 10 : System.out.print ("Masukan Angka : ");
                    a = masukan.nextInt();
                    bst.CariTerdekat(a);
                    break;
                case 11 : System.out.println ("See You Next Time\n");
                    System.exit(0);
                    break;
                default : System.out.println ("Maaf, pilihan anda salah\n");
            }
        }
        while (true);
    }

    public static void MenuPilihan () {
        System.out.println ("Menu :");
        System.out.println ("1  = Masukan Data");
        System.out.println ("2  = Hapus Data");
        System.out.println ("3  = Mencari Data Yang Diinput");
        System.out.println ("4  = Menghapus Semua Data");
        System.out.println ("5  = Menampilkan Pohon secara Pre-order");
        System.out.println ("6  = Menampilkan Pohon secara In-order");
        System.out.println ("7  = Menampilkan Pohon secara Post-order");
        System.out.println ("8  = Jumlah daun pada pohon");
        System.out.println ("9  = Jumlah node pada pohon");
        System.out.println ("10 = Mencari data terdekat dari inputan");
        System.out.println ("11 = Keluar");
    }
}
