
package linklist;
import java.util.Scanner;
public class DS_LinkList {

    public static void main(String[] args) {
        System.out.println("WELCOME!");
        System.out.println("Pilih menu yang ingin anda gunakan : ");
        System.out.println("1. Cek kosong ");
        System.out.println("2. Menambah data di awal ");
        System.out.println("3. Menambah data di akhir ");
        System.out.println("4. Menghapus data di awal");
        System.out.println("5. Menghapus data di akhir ");
        System.out.println("6. Temukan data ");
        System.out.println("7. Cetak semua data ");
        System.out.println("8. Hapus semua data ");
        System.out.println("9. Menghitung banyaknya data");
//        System.out.println("10. Hapus data "); --> menghaous data tertentu
//        System.out.println("11. Mengganti data"); --> mengedit data
//        System.out.println("12. Menambah data di indeks ke- "); --> abaikan saja, dapat merusak linklist
        System.out.println("13. Keluar ");
        LinkListCode method = new LinkListCode();
        int again;
        do 
        {
            System.out.println("What do you want to do?");
            Scanner masukan = new Scanner (System.in);
            int number = masukan.nextInt();
            switch (number)
            {
                case 1 : 
                {
                    method.isEmpty();
                    System.out.println("Keluar sekarang?");
                } break;
                case 2 : 
                {
                    Scanner inputan = new Scanner (System.in);
                    System.out.println("Masukkan data yang ingin anda tambahkan!");
                    int masuk = inputan.nextInt();
                    method.addFirst(masuk);
                    System.out.println("Keluar sekarang?");
                } break;
                case 3 :
                {
                    Scanner inputan = new Scanner (System.in);
                    System.out.println("Masukkan data yang ingin anda tambahkan!");
                    int masuk = inputan.nextInt();
                    method.addLast(masuk);
                    System.out.println("Keluar sekarang?");
                } break;
                case 4 :
                {
                    method.removeFirst();
                    System.out.println("Keluar sekarang?");
                } break;
                case 5 :
                {
                    method.removeLast();
                    System.out.println("Keluar sekarang?");
                } break;
                case 6 :
                {
                    Scanner inputan = new Scanner (System.in);
                    System.out.println("Masukkan data yang ingin anda cari!");
                    int masuk = inputan.nextInt();
                    method.find(masuk);
                    System.out.println("Keluar sekarang?");
                } break;
                case 7 :
                {
                    System.out.println("Your data : ");
                    method.printNode();
                    System.out.println("Keluar sekarang?");
                } break;
                case 8 : 
                {
                    method.clear();
                    System.out.println("Keluar sekarang?");
                } break;
                case 9 :
                {
                    method.length();
                    System.out.println("Keluar sekarang?");
                } break;
//                case 10 :
//                {
//                    Scanner inputan = new Scanner (System.in);
//                    System.out.println("Masukkan data yang ingin dihapus : ");
//                    int masuk = inputan.nextInt();
//                    method.remove(masuk);
//                    System.out.println("Keluar sekarang?");
//                } break;
//                case 11 :
//                {
//                    System.out.println("Masukkan data apa yang ingin anda hapus?");
//                    Scanner inputan = new Scanner (System.in);
//                    int masuk = inputan.nextInt();
//                    System.out.println("Masukkan data baru : ");
//                    Scanner inputan2 = new Scanner (System.in);
//                    int masuk2 = inputan2.nextInt();
//                    method.replace(masuk, masuk2);
//                    System.out.println("Keluar sekarang?");
//                } break;
//                case 12 : 
//                {
//                    System.out.println("Masukkan data apa yang ingin anda tambahkan!");
//                    Scanner inputan = new Scanner (System.in);
//                    int masuk = inputan.nextInt();
//                    System.out.println("Data tadi ingin dimasukkan ke indeks ke berapa? ");
//                    Node n=new Node();
//                    Scanner inputan2 = new Scanner (System.in);
//                    int masuk2 = inputan2.nextInt();
//                    n.data=masuk;
//                    method.insert (n, masuk2);
//                    System.out.println("Keluar sekarang?");
//                } break;
                case 13 :
                {
                    System.out.println("Anda yakin ingin keluar?");
                }
            }
            System.out.println("(1 = Yes, 0 = No)");
            Scanner lagi = new Scanner (System.in);
            again = lagi.nextInt();
        } while (again==0);

        System.out.println("Anda telah keluar!");
        System.out.println("Terima kasih.");
    }
    
}
