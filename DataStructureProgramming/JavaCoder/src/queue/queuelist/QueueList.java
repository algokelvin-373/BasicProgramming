package queue.queuelist;

public class QueueList implements QueueListImpl {
    Node front, back;

    public QueueList() {
        front=back=null;
    }

    @Override
    public boolean isEmpty() {
        return(front==null);
    }

    @Override
    public void makeEmpty() {
        if(isEmpty())
            System.out.println("Queue kosong");
        else{
            Node temp = front;
            while(temp!=null){
                front = front.next;
                temp = null;
                temp = front;
            }
            System.out.println("Queue telah dikosongkan");
        }
    }

    @Override
    public void enqueue(int data) {
        Node temp = new Node();
        temp.data = data;
        if(isEmpty()){
            front = back = temp;
        }
        else{
            back.next = temp;
            back = temp;
        }
        System.out.println("Data berhasil dimasukkan");
    }

    @Override
    public int dequeue() {
        if(isEmpty())
            return -1;
        else{
            int d = front.data;
            if(front==back){
                front=back=null;
            }
            else{
                Node temp = front;
                front=temp.next;
                temp = null;
            }
            return d;
        }
    }

    public void print(){
        Node temp = front;
        if(!isEmpty()){
            while(temp!=null){
                System.out.println(temp.data);
                temp = temp.next;
            }
        }
        else {
            System.out.println("Data kosong!");
        }
    }
}
