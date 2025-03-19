package SOLID_Principle.solid.ocp.impl;

public class OCP_Impl {
    public static void main(String[] args) {
        StandardCinema_OCP standardCinemaOcp = new StandardCinema_OCP(100);
        PremiumCinema_OCP premiumCinemaOcp = new PremiumCinema_OCP(50.0);
        DeluxeCinema_OCP deluxeCinemaOcp = new DeluxeCinema_OCP(200.0);

        System.out.println("Admin Fee Standard : "+ standardCinemaOcp.calculateAdminFee());
        System.out.println("Admin Fee Premium  : "+ premiumCinemaOcp.calculateAdminFee());
        System.out.println("Admin Fee Deluxe   : "+ deluxeCinemaOcp.calculateAdminFee());
    }
}
