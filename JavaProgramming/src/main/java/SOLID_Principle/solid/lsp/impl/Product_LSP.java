package SOLID_Principle.solid.lsp.impl;

abstract class Product_LSP {
    abstract void setName(String name);
    String name;

    void getProductInfo() {
        System.out.println(name);
    }
}
