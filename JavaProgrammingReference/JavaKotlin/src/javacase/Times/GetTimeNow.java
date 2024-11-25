package javacase.Times;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class GetTimeNow {
    public static void main(String[] args) {
        System.out.println("Get Time Now Format 1: "+ setFormatDateTime("yyyy-MM-dd HH:mm:ss"));
        System.out.println("Get Time Now Format 2: "+ setFormatDateTime("yyyyMMdd"));
        System.out.println("Get Time Now Format 3: "+ setFormatDateTime("HHmmss"));
    }

    public static String setFormatDateTime(String format) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(format);
        LocalDateTime now = LocalDateTime.now();
        return dtf.format(now);
    }

}
