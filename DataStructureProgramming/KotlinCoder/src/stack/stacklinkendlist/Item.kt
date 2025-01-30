package stack.stacklinkendlist

class Item(id: Int) {
    private var num = 0
    var data = 0

    var next: Item? = null
    var previous: Item? = null

    init {
        data = id
        num = id
        next = null
    }

    fun displayLink() {
        println("{ $data }")
    }
}