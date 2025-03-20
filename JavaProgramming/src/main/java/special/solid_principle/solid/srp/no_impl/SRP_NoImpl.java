package special.solid_principle.solid.srp.no_impl;

public class SRP_NoImpl {
    public static void main(String[] args) {
        Item_No_SRP itemNoSrp1 = new Item_No_SRP("Meatball", 15000, 2);
        Item_No_SRP itemNoSrp2 = new Item_No_SRP("Noodles", 20000, 1);
        Item_No_SRP itemNoSrp3 = new Item_No_SRP("Fried Chicken", 12500, 3);

        Order_No_SRP orderNoSrp = new Order_No_SRP();

        //Add Item
        orderNoSrp.addItem(itemNoSrp1);
        orderNoSrp.addItem(itemNoSrp2);
        orderNoSrp.addItem(itemNoSrp3);

        //Delete Item
        orderNoSrp.deleteItem(itemNoSrp2);

        //Calculate Total
        orderNoSrp.calculateTotalSum();

        orderNoSrp.getItems();
        orderNoSrp.getItemCount();

        orderNoSrp.showOrder();
        orderNoSrp.printOrder();

        orderNoSrp.getDailyHistory();
        orderNoSrp.getMonthlyHistory();

    }
}
