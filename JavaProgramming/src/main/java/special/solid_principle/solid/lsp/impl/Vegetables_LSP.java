package special.solid_principle.solid.lsp.impl;

class Vegetables_LSP extends FoodProduct_LSP {

    @Override
    void setName(String name) {
        this.name = name;
    }

    @Override
    void setExpiredDate(String expDate) {
        this.expDate = expDate;
    }

}
