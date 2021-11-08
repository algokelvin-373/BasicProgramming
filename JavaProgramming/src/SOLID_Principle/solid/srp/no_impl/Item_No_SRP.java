package SOLID_Principle.solid.srp.no_impl;

public class Item_No_SRP {
    private String name;
    private int price;
    private int amount;

    public Item_No_SRP(String name, int price, int amount) {
        this.name = name;
        this.price = price;
        this.amount = amount;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public int getAmount() {
        return amount;
    }
}
