package special.solid_principle.composition;

import special.solid_principle.data.Address;
import special.solid_principle.data.User;

public class Composition {
    public static void main(String[] args) {
        User user1 = new User(1234, "Algokelvin", new Address(123, "SoloJakarta"));
        User user2 = new User(5412, "Jenda", new Address(342, "Jakarta"));

        System.out.println(user1.getName()+"-"+user1.getAddress().getLocation());
        System.out.println(user2.getName()+"-"+user2.getAddress().getLocation());
    }
}
