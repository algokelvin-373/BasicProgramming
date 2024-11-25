package tree.rbt;

public class Node {

    Node left, right;
    int element;
    int color;

    /* Constructor */
    public Node(int theElement) {
        this(theElement, null, null);
    }

    /* Constructor */
    public Node(int theElement, Node lt, Node rt) {
        left = lt;
        right = rt;
        element = theElement;
        color = 1;
    }
}
