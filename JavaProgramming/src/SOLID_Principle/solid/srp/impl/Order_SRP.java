package SOLID_Principle.solid.srp.impl;

import java.util.ArrayList;

public class Order_SRP {
    private int total;
    private ArrayList<Item_SRP> dataItem = new ArrayList<>();

    void calculateTotalSum() {
        for (Item_SRP item_srp : dataItem) {
            total += (item_srp.getAmount() * item_srp.getPrice());
        }
    }

    void getItems() {
        System.out.println("Item Food \t Amount \t Price");
        for (Item_SRP item_srp : dataItem) {
            System.out.println(item_srp.getName() + "\t\t" +
                    item_srp.getAmount() + "\t\t" +
                    item_srp.getAmount() * item_srp.getPrice());
        }
    }

    void getItemCount() {
        System.out.println("Total: " + total);
    }

    void addItem(Item_SRP item) {
        dataItem.add(item);
    }

    void deleteItem(Item_SRP item) {
        dataItem.remove(item);
    }
}
