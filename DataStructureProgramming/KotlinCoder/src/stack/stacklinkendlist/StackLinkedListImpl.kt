package stack.stacklinkendlist

class StackLinkedListImpl: StackLinkedList {
    private var top: Item? = null
    private var bottom: Item? = null

    override fun isEmpty(): Boolean {
        var empty = false
        if (top == null) {
            empty = true
        }
        return empty
    }

    override fun push(data: Int) {
        val newItem = Item(data)
        if (top == null) {
            bottom = newItem
            top = bottom
        } else {
            top?.next = newItem
            newItem.previous = top
            top = newItem
        }
    }

    override fun pop() {
        if (isEmpty()) {
            println("Stack is empty!")
        } else {
            var temp: Item? = null
            if (top === bottom) {
                temp = top
                bottom = null
                top = bottom
            } else {
                temp = top
                top = top?.previous
                top?.next = null
            }
        }
    }

    override fun makeEmpty() {

    }

    override fun print() {
        if (isEmpty()) {
            println("Stack is empty!")
        } else {
            var current = bottom
            while (current != null) {
                current.displayLink()
                current = current.next
            }
        }
        println()
    }

    override fun top() {

    }

}