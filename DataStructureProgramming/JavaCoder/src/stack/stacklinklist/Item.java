package stack.stacklinklist;

public class Item {
    private int num;
    public int data;

    public Item next;
    public Item previous;

    public Item (int id){
        data = id;
        num = id;
        next = null;
    }

    public void displayLink() {
        System.out.println("{ " + data + " }");
    }
}
