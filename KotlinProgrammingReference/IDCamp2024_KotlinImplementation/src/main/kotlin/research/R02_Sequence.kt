package research

fun main() {
    val list =(1..100000000).toList()

    // Implement List
    val start1 = System.currentTimeMillis()
    val filterList1 = list.filter {
        it % 5 == 0
    }.map {
        it * 2
    }.first()
    val end1 = System.currentTimeMillis()

    // Implement Sequence
    val start2 = System.currentTimeMillis()
    val filterList2 = list.asSequence()
        .filter {
            it % 5 == 0
        }.map {
            it * 2
        }.first()
    val end2 = System.currentTimeMillis()

    println(filterList1)
    println("Timer: ${end1 - start1}")
    println(filterList2)
    println("Timer: ${end2 - start2}")
}