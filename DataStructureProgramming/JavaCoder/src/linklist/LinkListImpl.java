
package linklist;

public interface LinkListImpl {
    boolean isEmpty();
    void addFirst(int input);
    void addLast(int input);
    void removeFirst();
    void removeLast();
    void find(int data);
    void printNode();
    void clear();
    void length();
    void remove(int data);
    void replace(int addData, int newData);
    void insert(Node data, int indeks);
    
}
