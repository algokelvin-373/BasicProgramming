package binaryheap;

import java.util.Scanner;

public class HomeBinaryHeap {
    public static void main(String[] args) {
        System.out.println("---Welcome in Binary Heap SDA II 2018 with Algokelvin_373---\n");
        @SuppressWarnings("UnusedAssignment")
        int pilih = 0;

        // System Binary Heap
        Scanner input = new Scanner(System.in);
        System.out.print("Masukan besar kapasitas : ");
        BinaryHeap binaryHeap = new BinaryHeap(input.nextInt());
        System.out.println("Kapasitas anda saat ini ada "+binaryHeap.heap.length+".\nSelamat menggunakan dan selamat belajar SDA II");

        do {
            System.out.println("\nSilahkan pilih :\n1. Input Data\n2. Delete Data\n3. Keluar");
            System.out.print("Pilih : ");
            pilih = input.nextInt();
            switch(pilih) {
                case 1 :
                    break;
                case 2 :
                    break;
                case 3 : System.out.println("Anda sudah keluar. Sampai ketemu lagi");
                    break;
            }
        }
        while(pilih != 3);
    }
}
