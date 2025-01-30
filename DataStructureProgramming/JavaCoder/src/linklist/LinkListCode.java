
package linklist;

public class LinkListCode implements LinkListImpl {
    
    Node head;
    Node tail;
    @Override
    public boolean isEmpty()
    {
        return (head==null);
    }

    @Override
    public void addFirst(int input) {
        Node baru = new Node (input);
        if(isEmpty())
        {
            head = baru;
            tail = baru;
        }
        else
        {
            baru.next = (Node) head;
            head = baru;
        }
        System.out.println("Data : " + baru.data + " ditambahkan di awal!");
    }

    @Override
    public void addLast(int input) {
        Node baru = new Node (input);
        if(isEmpty())
        {
            head = baru;
            tail = baru;
        }
        else
        {
            tail.next = baru;
            tail = baru;
        }
        System.out.println("Data : " + baru.data + " ditambahkan di akhir!");
    }

    @Override
    public void removeFirst() {
        Node temp = (Node) head;
        if(!isEmpty())
        {
            if(head == tail)
            {
                head = tail = null;
            }
            else
            {
                head = temp.next;
                temp.next = null;
                //temp = null;
            }
            System.out.println("Data di awal sudah dihapus!");
        }
        else
            System.out.println("Data kosong!");
    }

    @Override
    public void removeLast() {
        Node temp = (Node) head;
        if(!isEmpty())
        {
            if (tail == head)
            {
                head = tail = null;
            }
            else
            {
                while (temp.next != tail)
                {
                    temp = temp.next;
                }
                temp.next = null;
                tail = temp;
                //temp = null;
            }
            System.out.println("Data di akhir berhasil dihapus!");
        }
        else
            System.out.println("Data kosong!");
        
    }

    @Override
    public void find(int data) {
        int i = 0;
        boolean found = false;
        Node temp = (Node) head;
        while (temp != null)
        {
            if(temp.data == data)
            {
                found = true;
                break;
            }i++; temp = temp.next;
            
        }
        if (found) 
                {
                    System.out.println(data+" ditemukan di indeks ke-" + i);
                }
        else
            System.out.println("Data tidak ditemukan!");
    }

    @Override
    public void printNode() {
        Node temp;
        temp = (Node) head;
        while (temp != null)
        {
            System.out.println("Data : " + temp.data);
            temp = temp.next;
        }
        System.out.println("END");
    }
    
    @Override 
    public void clear () {
        
            head = null;
           
        System.out.println("SUDAH KOSONG!");
    }
    
    @Override 
    public void length () {
        int i = 0;
        Node temp;
        temp = (Node) head;
        while (temp!= null)
        {
            i++;
            temp = temp.next;
        }
        System.out.println("Jumlah datanya : " + i);
    }
    
    @Override 
    public void remove (int data)
            
    {
        
        Node hm = (Node) head;
        Node temp;
        temp = (Node) head;
        //boolean found = false;
        while( temp.data!= data & temp != null ) {
                    hm = temp;
                    temp = temp.next;
            } 
            if( temp.data == data ) {
                hm.next = temp.next ;
                System.out.println( "Data berhasil dihapus\n" );
            }
            else
                System.out.println("Data tidak ditemukan!");
               
            
        }

    
    
    
    @Override
    public void replace (int addData,int newData)
    {
        
        boolean found = false;
        Node temp = (Node) head;
        while (temp != null)
        {
            if(temp.data == addData)
            {
                found = true;
                temp.data = newData;
                break;
            } temp = temp.next;
            //System.out.println(head.next.data);
        }
        if(found)
            System.out.println("Data sudah diganti!");
        else
            System.out.println("Data tidak ditemukan! Operasi tidak dapat dilanjutkan!");
    }
    
    @Override 
    public void insert (Node data,int indeks){
        Node temp = (Node) head;
        //Node hm = (Node) head;
        //boolean found=false;
        
        int i=0;
        int indek = indeks-1;
        if (indeks == 0){
             data.next = head;
             head = data;
        }
        else{
            do{
                if (i == indek){
                    //found=true;
                    data.next=temp.next;
                    temp.next=data;
                    System.out.println("Data berhasil dimasukkan!");
                    break;
                }
                else{
                    i++;
                    temp = temp.next;
                }
            }
            while (temp != null);
        }
        
    }
}

