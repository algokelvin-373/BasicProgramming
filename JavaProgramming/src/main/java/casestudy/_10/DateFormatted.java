package com.linkedin._10;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateFormatted {
    public static void main(String[] args) {
        System.out.println(dateFormatted("dd MMMM yyyy G hh:mm:SS zzz"));
        System.out.println(dateFormatted("dd/MM/yy"));
    }

    private static String dateFormatted(String format) {
        Date now = new Date();
        DateFormat dateFormat = new SimpleDateFormat(format);
        return dateFormat.format(now);
    }

}
