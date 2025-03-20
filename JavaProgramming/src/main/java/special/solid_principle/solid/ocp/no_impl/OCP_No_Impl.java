package special.solid_principle.solid.ocp.no_impl;

public class OCP_No_Impl {
    public static void main(String[] args) {
        StandardCinema_No_OCP standardCinemaNoOcp = new StandardCinema_No_OCP(100.0);
        PremiumCinema_No_OCP premiumCinemaNoOcp = new PremiumCinema_No_OCP(50.0);
        DeluxeCinema_No_OCP deluxeCinemaNoOcp = new DeluxeCinema_No_OCP(200.0);

        CinemaCalculations cinemaCalculations = new CinemaCalculations();
        double adminFeeStandard = cinemaCalculations.calculateAdminFee(standardCinemaNoOcp);
        double adminFeePremium = cinemaCalculations.calculateAdminFee(premiumCinemaNoOcp);
        double adminFeeDeluxe = cinemaCalculations.calculateAdminFee(deluxeCinemaNoOcp);

        System.out.println("Admin Fee Standard : "+ adminFeeStandard);
        System.out.println("Admin Fee Premium  : "+ adminFeePremium);
        System.out.println("Admin Fee Deluxe   : "+ adminFeeDeluxe);

    }
}
