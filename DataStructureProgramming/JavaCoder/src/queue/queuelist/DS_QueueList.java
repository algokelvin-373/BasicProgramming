package queue.queuelist;

import java.util.Scanner;

public class DS_QueueList {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        QueueList IQ = new QueueList();
        boolean j=true;
        while(j){
            Menu();
            int p = scn.nextInt();
            switch (p) {
                case 1 -> {
                    System.out.print("Masukkan data angka : ");
                    p = scn.nextInt();
                    IQ.enqueue(p);
                    break;
                }
                case 2 -> {
                    p = IQ.dequeue();
                    if (p != -1) {
                        System.out.print("Data dengan nilai ");
                        System.out.print(p);
                        System.out.println(" telah berhasil dihapus");
                    } else
                        System.out.println("Tidak ada data dalam Queue");
                    break;
                }
                case 3 -> {
                    IQ.makeEmpty();
                    break;
                }
                case 5 -> {
                    j = false;
                    break;
                }
                case 4 -> {
                    IQ.print();
                }
                default -> {
                    System.out.print("Masukan anda salah. ");
                    System.out.println("Masukkan angka antara 1-4");
                }
            }
        }
    }
    public static void Menu(){
        System.out.println("Menu (Implementasi 1)");
        System.out.println("1. Masukkan data (Enqueue)");
        System.out.println("2. Hapus data (Dequeue)");
        System.out.println("3. Kosongkan Queue (makeEmpty)");
        System.out.println("4. Tampilkan data");
        System.out.println("5. Keluar");
        System.out.print("Masukkan menu pilihan anda : ");
    }
}
