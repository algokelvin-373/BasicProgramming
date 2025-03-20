package special.solid_principle.solid.lsp.no_impl;

public class LSP_No_Impl {
    public static void main(String[] args) {
        Vegetables_No_LSP vegetablesNoLsp = new Vegetables_No_LSP();
        vegetablesNoLsp.setName("Broccoli");
        vegetablesNoLsp.setExpiredDate("9 January 2022");
        vegetablesNoLsp.getProductInfo();

        Smartphone_No_LSP smartphoneNoLsp = new Smartphone_No_LSP();
        smartphoneNoLsp.setName("Samsung S21 Pro");
        smartphoneNoLsp.setExpiredDate("21 December 2022"); // Not Compatible
        smartphoneNoLsp.getProductInfo();
    }
}
