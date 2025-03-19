package kotlincase

import java.text.DecimalFormat
import java.text.NumberFormat
import java.text.SimpleDateFormat
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.util.*

object CaseStudy01 {
    //Case 1: Convert Format Date
    fun getDateConvert(oldFormat: String, oldDate: String, newFormat: String): String {
        val sdf = SimpleDateFormat(oldFormat, Locale.getDefault())
        val sdf2 = SimpleDateFormat(newFormat, Locale("id","ID"))
        val date = sdf.parse(oldDate)
        return sdf2.format(date)
    }

    //Case 2: Get Time Now
    fun getTimeNow(format: String): String {
        val current = LocalDateTime.now()
        val formatter = DateTimeFormatter.ofPattern(format)
        return current.format(formatter)
    }

    //Case 3: Convert Currency (Rupiah - IDR)
    fun convertCurrency(data: Double): String {
        val formatter: NumberFormat = DecimalFormat("#,###")
        return formatter.format(data).replace(",", ".")
    }
}