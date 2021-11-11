package SOLID_Principle.solid.lsp.impl;

abstract class FoodProduct_LSP extends Product_LSP {
    abstract void setExpiredDate(String expDate);
    String expDate;

    void getFoodProductInfo() {
        System.out.println(name+" - "+expDate);
    }
}
