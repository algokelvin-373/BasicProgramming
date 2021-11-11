package SOLID_Principle.solid.lsp.no_impl;

class Smartphone_No_LSP extends Product_No_LSP {

    @Override
    void setName(String name) {
        this.name = name;
    }

    @Override
    void setExpiredDate(String expDate) {
        this.expDate = expDate; // ?? Not Compatible
    }
}
