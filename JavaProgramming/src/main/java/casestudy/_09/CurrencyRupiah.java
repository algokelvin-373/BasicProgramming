package com.linkedin._09;

import java.text.NumberFormat;
import java.util.Currency;
import java.util.Locale;

public class CurrencyRupiah {
    public static void main(String[] args) {
        String rupiah1 = currencyRupiah(100000.00);
        String rupiah2 = currencyRupiah(2000000.00);
        System.out.println(rupiah1);
        System.out.println(rupiah2);
    }

    private static String currencyRupiah(double price) {
        Locale locale = new Locale("in", "ID");
        Currency currency = Currency.getInstance(locale);
        NumberFormat numberFormat = NumberFormat.getCurrencyInstance(locale);
        return numberFormat.format(price);
    }

}
