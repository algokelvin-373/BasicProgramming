package stack.stackarray

interface StackArray {
    fun isEmpty(): Boolean
    fun push(data: Int)
    fun pop()
    fun makeEmpty()
    fun print()
    fun top()
}