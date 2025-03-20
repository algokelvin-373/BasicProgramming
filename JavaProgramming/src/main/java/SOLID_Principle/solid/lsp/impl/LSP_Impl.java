package SOLID_Principle.solid.lsp.impl;

public class LSP_Impl {
    public static void main(String[] args) {
        Vegetables_LSP vegetablesLsp = new Vegetables_LSP();
        vegetablesLsp.setName("Broccoli");
        vegetablesLsp.setExpiredDate("21 January 2022");
        vegetablesLsp.getFoodProductInfo();

        Smartphone_LSP smartphoneLsp = new Smartphone_LSP();
        smartphoneLsp.setName("Samsung S21");
        smartphoneLsp.getProductInfo();
    }
}
