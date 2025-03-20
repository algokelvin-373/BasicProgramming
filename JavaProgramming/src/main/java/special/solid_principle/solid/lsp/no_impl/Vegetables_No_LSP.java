package special.solid_principle.solid.lsp.no_impl;

class Vegetables_No_LSP extends Product_No_LSP {

    @Override
    void setName(String name) {
        this.name = name;
    }

    @Override
    void setExpiredDate(String expDate) {
        this.expDate = expDate;
    }

}
