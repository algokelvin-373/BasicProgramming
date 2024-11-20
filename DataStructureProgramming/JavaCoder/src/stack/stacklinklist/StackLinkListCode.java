package stack.stacklinklist;

public class StackLinkListCode implements StackLinkListImpl {
    private Item top;
    private Item bottom;

    @Override
    public boolean isEmpty() {
        boolean empty = false;
        if(top == null){
            empty = true;
        }
        return empty;
    }

    @Override
    public void push(int data) {
        Item newItem = new Item (data);
        if(top == null){
            top = bottom = newItem;
        }
        else {
            top.next = newItem;
            newItem.previous = top;
            top = newItem;
        }
    }

    @Override
    public void pop() {
        if(isEmpty()){
            System.out.println("Stack is empty!");
        }
        else {
            Item temp = null;
            if(top == bottom) {
                temp = top;
                top = bottom = null;
            }
            else {
                temp = top;
                top = top.previous;
                top.next = null;
            }
        }
    }

    @Override
    public void makeEmpty() {

    }

    @Override
    public void print() {
        if(isEmpty()){
            System.out.println("Stack is empty!");
        }
        else {
            Item current = bottom;
            while ( current != null){
                current.displayLink();
                current = current.next;
            }
        }
        System.out.println();
    }

    @Override
    public void top() {

    }
}
