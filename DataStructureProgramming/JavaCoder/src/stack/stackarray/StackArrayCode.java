package stack.stackarray;

public class StackArrayCode implements StackArrayImpl {
    private static final int capacity = 10;
    int arr[] = new int[capacity];
    int top1 = -1;

    @Override
    public boolean isEmpty() {
        boolean empty = false;
        if(top1 == -1){
            empty = true;
        }
        return empty;
    }

    @Override
    public void push(int data) {
        if(top1 >= capacity-1){
            System.out.println("Stack overflow!");
        }
        else {
            top1++;
            arr[top1] = data;
        }
    }

    @Override
    public void pop() {
        if(isEmpty()) {
            System.out.println("Stack underflow!");
        }
        else {
            arr[top1--] = 0;
        }
    }

    @Override
    public void makeEmpty() {

    }

    @Override
    public void print() {
        int i;
        if(isEmpty()){
            System.out.println("Stack is empty!");
        }
        else {
            for(i = 0; i <= top1; i++) {
                System.out.println("{ " + arr[i] + " }");
            }
        }
    }

    @Override
    public void top() {

    }
}
