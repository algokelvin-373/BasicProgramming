package stack.stacklinklist;

import java.util.Scanner;

public class DS_StackLinkList {
    private static StackLinkListCode llist = new StackLinkListCode();
    private static Scanner input = new Scanner(System.in);
    private static int data;

    public static void main(String[] args) {
        int again;
        do {
            System.out.println("What do you want to do?");
            System.out.println("1. Push data.");
            System.out.println("2. Pop data.");
            System.out.println("3. Display data.");
            data = input.nextInt();
            switch (data) {
                case 1 : {
                    push();
                    break;
                }
                case 2 : {
                    pop();
                    break;
                }
                case 3 : {
                    printData();
                    break;
                }
            }
            System.out.println("Again?");
            System.out.println("1.Again || 2. Quit");
            Scanner inputAgain = new Scanner (System.in);
            again = inputAgain.nextInt();
        } while (again == 1);
    }

    private static void push() {
        System.out.println("Enter the data!");
        data = input.nextInt();
        llist.push(data);
        System.out.println("Data has been pushed");
    }

    private static void pop() {
        System.out.println("Data has been popped!");
        llist.pop();
    }

    private static void printData() {
        System.out.println("The data : ");
        llist.print();
    }

}
