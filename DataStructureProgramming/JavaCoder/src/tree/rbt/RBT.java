package tree.rbt;

public class RBT {

    private Node current;
    private Node parent;
    private Node grand;
    private Node great;
    private Node header;
    private static Node nullNode;

    /* static initializer for nullNode */
    static {
        nullNode = new Node(0);
        nullNode.left = nullNode;
        nullNode.right = nullNode;
    }

    /* Black - 1  RED - 0 */
    static final int BLACK = 1;
    static final int RED = 0;

    /* Constructor */
    public RBT(int negInf) {
        header = new Node(negInf);
        header.left = nullNode;
        header.right = nullNode;
    }

    /* Function to check if tree is empty */
    public boolean isEmpty() {
        return header.right == nullNode;
    }

    /* Make the tree logically empty */
    public void makeEmpty() {
        header.right = nullNode;
    }

    /* Function to insert item */
    public void insert(int item) {
        current = parent = grand = header;
        nullNode.element = item;
        while (current.element != item) {
            great = grand;
            grand = parent;
            parent = current;
            current = item < current.element ? current.left : current.right;
            // Check if two red children and fix if so            
            if (current.left.color == RED && current.right.color == RED) {
                handleReorient(item);
            }
        }

        // Insertion fails if already present
        if (current != nullNode) {
            System.out.println("Element bernilai sama");
            return;
        }
        current = new Node(item, nullNode, nullNode);
        // Attach to parent
        if (item < parent.element) {
            parent.left = current;
        } else {
            parent.right = current;
        }
        handleReorient(item);
    }

    private void handleReorient(int item) {
        // Do the color flip
        current.color = RED;
        current.left.color = BLACK;
        current.right.color = BLACK;
        if (parent.color == RED) {
            // Have to rotate
            grand.color = RED;
            if (item < grand.element != item < parent.element) {
                parent = rotate(item, grand);  // Start dbl rotate
            }
            current = rotate(item, great);
            current.color = BLACK;
        }
        // Make root black
        header.right.color = BLACK;
    }

    private Node rotate(int item, Node parent) {
        if (item < parent.element) {
            return parent.left = item < parent.left.element ? rotateWithLeftChild(parent.left) : rotateWithRightChild(parent.left);
        } else {
            return parent.right = item < parent.right.element ? rotateWithLeftChild(parent.right) : rotateWithRightChild(parent.right);
        }
    }

    /* Rotate binary tree node with left child */
    private Node rotateWithLeftChild(Node k2) {
        Node k1 = k2.left;
        k2.left = k1.right;
        k1.right = k2;
        return k1;
    }

    /* Rotate binary tree node with right child */
    private Node rotateWithRightChild(Node k1) {
        Node k2 = k1.right;
        k1.right = k2.left;
        k2.left = k1;
        return k2;
    }

    /* Functions to count number of nodes */
    public int countNodes() {
        return countNodes(header.right);
    }

    private int countNodes(Node r) {
        //isi sendiri ya :3
    }

    /* Functions to search for an element */
    public boolean search(int val) {
        return search(header.right, val);
    }

    private boolean search(Node r, int val) {
        //isi sendiri ya :3
    }

    /* Function for inorder traversal */
    public void inorder() {
        inorder(header.right);
    }

    private void inorder(Node r) {
        //isi sendiri ya :3
    }
    /* Function for preorder traversal */

    public void preorder() {
        preorder(header.right);
    }

    private void preorder(Node r) {
        if (r != nullNode) {
            char c = 'B';
            if (r.color == 0) {
                c = 'R';
            }
            System.out.print(r.element + "" + c + " ");
            preorder(r.left);
            preorder(r.right);
        }
    }
    /* Function for postorder traversal */

    public void postorder() {
        postorder(header.right);
    }

    private void postorder(Node r) {
        //isi sendiri ya :3
    }
}