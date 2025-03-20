package SOLID_Principle.solid.srp.impl;

public class SRP_Impl {
    public static void main(String[] args) {
        Item_SRP itemNoSrp1 = new Item_SRP("Meatball", 15000, 2);
        Item_SRP itemNoSrp2 = new Item_SRP("Noodles", 20000, 1);
        Item_SRP itemNoSrp3 = new Item_SRP("Fried Chicken", 12500, 3);

        Order_SRP orderSrp = new Order_SRP();

        //Add Item
        orderSrp.addItem(itemNoSrp1);
        orderSrp.addItem(itemNoSrp2);
        orderSrp.addItem(itemNoSrp3);

        //Delete Item
        orderSrp.deleteItem(itemNoSrp2);

        //Calculate Total
        orderSrp.calculateTotalSum();

        orderSrp.getItems();
        orderSrp.getItemCount();

        OrderViewer orderViewer = new OrderViewer();
        orderViewer.showOrder(orderSrp);
        orderViewer.printOrder(orderSrp);

        OrderHistory orderHistory = new OrderHistory();
        orderHistory.getDailyHistory();
        orderHistory.getMonthlyHistory();
    }
}
