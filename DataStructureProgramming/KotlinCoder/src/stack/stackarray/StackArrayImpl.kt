package stack.stackarray

import stack.stackarray.StackArray

class StackArrayImpl: StackArray {
    private var capacity = 10
    private var arr = IntArray(capacity)
    private var top1 = -1

    override fun isEmpty(): Boolean {
        var empty = false
        if (top1 == -1) {
            empty = true
        }
        return empty
    }

    override fun push(data: Int) {
        if (top1 >= capacity - 1) {
            println("Stack overflow!")
        } else {
            top1++
            arr[top1] = data
        }
    }

    override fun pop() {
        if (isEmpty()) {
            println("Stack underflow!")
        } else {
            arr[top1--] = 0
        }
    }

    override fun makeEmpty() {

    }

    override fun print() {
        var i: Int
        if (isEmpty()) {
            println("Stack is empty!")
        } else {
            i = 0
            while (i <= top1) {
                println("{ " + arr[i] + " }")
                i++
            }
        }
    }

    override fun top() {

    }

}