package special.solid_principle.kardinalitas;

import special.solid_principle.data.Seller;
import special.solid_principle.data.User;

import java.util.ArrayList;

public class OneToMany {
    public static void main(String[] args) {
        ArrayList<Seller> dataSeller = new ArrayList<>();
        dataSeller.add(new Seller(1234, "Ines"));
        dataSeller.add(new Seller(4555, "Fakri"));
        dataSeller.add(new Seller(9876, "Thea"));
        dataSeller.add(new Seller(1023, "Yohana"));

        ArrayList<User> dataUser = new ArrayList<>();

        ArrayList<Seller> dataSellerAngel = new ArrayList<>();
        dataSellerAngel.add(dataSeller.get(0));
        dataSellerAngel.add(dataSeller.get(2));
        dataUser.add(new User(10, "Angel", dataSellerAngel));

        ArrayList<Seller> dataSellerSiska = new ArrayList<>();
        dataSellerSiska.add(dataSeller.get(1));
        dataSellerSiska.add(dataSeller.get(2));
        dataSellerSiska.add(dataSeller.get(3));
        dataUser.add(new User(20, "Siska", dataSellerSiska));

        for (User user : dataUser) {
            System.out.println("User:");
            System.out.println("Name  : " + user.getName());
            System.out.println("Seller: " + user.getName());
            for (int x = 0; x < user.getSellers().size(); x++) {
                System.out.println((x + 1) + ". " + user.getSellers().get(x).getName());
            }
        }
    }
}
