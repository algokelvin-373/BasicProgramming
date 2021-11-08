package SOLID_Principle.solid.srp.no_impl;

import java.util.ArrayList;

class Order_No_SRP {
    private int total;
    private ArrayList<Item_No_SRP> dataItem = new ArrayList<>();

    void calculateTotalSum() {
        for (Item_No_SRP item_no_srp : dataItem) {
            total += (item_no_srp.getAmount() * item_no_srp.getPrice());
        }
    }

    void getItems() {
        System.out.println("Item Food \t Amount \t Price");
        for (Item_No_SRP item_no_srp : dataItem) {
            System.out.println(item_no_srp.getName() + "\t\t" +
                    item_no_srp.getAmount() + "\t\t" +
                    item_no_srp.getAmount() * item_no_srp.getPrice());
        }
    }

    void getItemCount() {
        System.out.println("Total: " + total);
    }

    void addItem(Item_No_SRP itemNoSRP) {
        dataItem.add(itemNoSRP);
    }

    void deleteItem(Item_No_SRP itemNoSRP) {
        dataItem.remove(itemNoSRP);
    }

    void printOrder() {
        System.out.println("Print Order");
    }

    void showOrder() {
        System.out.println("Show Order");
    }

    void getDailyHistory() {
        System.out.println("Daily History");
    }
    void getMonthlyHistory() {
        System.out.println("Month History");
    }
}
