package special.solid_principle.solid.lsp.no_impl;

abstract class Product_No_LSP {
    abstract void setName(String name);
    abstract void setExpiredDate(String expDate);

    String name;
    String expDate;

    void getProductInfo() {
        System.out.println(name+" - "+expDate);
    }
}
