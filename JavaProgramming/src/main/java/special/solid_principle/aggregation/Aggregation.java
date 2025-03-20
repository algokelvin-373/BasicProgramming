package special.solid_principle.aggregation;

import special.solid_principle.data.Seller;
import special.solid_principle.data.Shop;

public class Aggregation {
    public static void main(String[] args) {
        Seller seller1 = new Seller(12, "Kelvin");
        Shop shop1 = new Shop(1000, "Olshop.vin", seller1);
        Shop shop2 = new Shop(2312, "Coffee.vin", seller1);

        System.out.println(shop1.getName()+ " - "+ shop1.getSeller().getName());
        System.out.println(shop2.getName()+ " - "+ shop2.getSeller().getName());
    }
}
