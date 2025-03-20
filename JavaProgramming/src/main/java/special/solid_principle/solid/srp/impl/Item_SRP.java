package special.solid_principle.solid.srp.impl;

public class Item_SRP {
    private String name;
    private int price;
    private int amount;

    public Item_SRP(String name, int price, int amount) {
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
