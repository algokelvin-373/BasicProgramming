package tree.avl;

public class AVL {
    protected AVLNode root;

    public void insert(int k) {

        AVLNode n = new AVLNode(k);

        insertAVL(this.root, n);
    }

    public void insertAVL(AVLNode p, AVLNode q) {
        if (p == null) {
            this.root = q;
        } else {
            if (q.key < p.key) {
                if (p.left == null) {
                    p.left = q;
                    q.parent = p;

                    recursiveBalance(p);
                    System.out.println("Data telah dimasukkan");
                } else {
                    insertAVL(p.left, q);
                }

            } else if (q.key > p.key) {
                if (p.right == null) {
                    p.right = q;
                    q.parent = p;

                    recursiveBalance(p);
                    System.out.println("Data telah dimasukkan");
                } else {
                    insertAVL(p.right, q);
                }
            } else {
                System.out.println("Data telah ada, silahkan masukkan yang lain");
            }
        }
    }

    public void recursiveBalance(AVLNode cur) {

        setBalance(cur);
        int balance = cur.balance;

        if (balance == -2) {

            if (height(cur.left.left) >= height(cur.left.right)) {
                cur = rotateRight(cur);
            } else {
                cur = doubleRotateLeftRight(cur);
            }
        } else if (balance == 2) {
            if (height(cur.right.right) >= height(cur.right.left)) {
                cur = rotateLeft(cur);
            } else {
                cur = doubleRotateRightLeft(cur);
            }
        }

        if (cur.parent != null) {
            recursiveBalance(cur.parent);
        } else {
            this.root = cur;
            System.out.println("------------ Balancing finished -------------");
        }
    }

    public void remove(int k) {
        removeAVL(this.root, k);
    }

    public void removeAVL(AVLNode p, int q) {
        if (p == null) {
            System.out.println("Pohon dalam keadaan kosong");
            return;
        } else {
            if (p.key > q) {
                removeAVL(p.left, q);
            } else if (p.key < q) {
                removeAVL(p.right, q);
            } else if (p.key == q) {
                removeFoundNode(p);
            }
        }
    }

    public void removeFoundNode(AVLNode q) {
        AVLNode r;
        if (q.left == null || q.right == null) {

            if (q.parent == null) {
                this.root = null;
                q = null;
                return;
            }
            r = q;
        } else {

            r = successor(q);
            q.key = r.key;
        }
        AVLNode p;
        if (r.left != null) {
            p = r.left;
        } else {
            p = r.right;
        }
        if (p != null) {
            p.parent = r.parent;
        }

        if (r.parent == null) {
            this.root = p;
        } else {
            if (r == r.parent.left) {
                r.parent.left = p;
            } else {
                r.parent.right = p;
            }
            recursiveBalance(r.parent);
        }
        r = null;
    }

    public AVLNode rotateLeft(AVLNode n) {

        AVLNode v = n.right;
        v.parent = n.parent;

        n.right = v.left;

        if (n.right != null) {
            n.right.parent = n;
        }

        v.left = n;
        n.parent = v;

        if (v.parent != null) {
            if (v.parent.right == n) {
                v.parent.right = v;
            } else if (v.parent.left == n) {
                v.parent.left = v;
            }
        }

        setBalance(n);
        setBalance(v);
        System.out.println("Single rotation (kiri)");
        return v;
    }

    public AVLNode rotateRight(AVLNode n) {

        AVLNode v = n.left;
        v.parent = n.parent;

        n.left = v.right;

        if (n.left != null) {
            n.left.parent = n;
        }

        v.right = n;
        n.parent = v;

        if (v.parent != null) {
            if (v.parent.right == n) {
                v.parent.right = v;
            } else if (v.parent.left == n) {
                v.parent.left = v;
            }
        }

        setBalance(n);
        setBalance(v);
        System.out.println("Single rotation (kanan)");
        return v;
    }

    public AVLNode doubleRotateLeftRight(AVLNode u) {
        u.left = rotateLeft(u.left);
        System.out.println("Double Rotation (kiri ke kanan)");
        return rotateRight(u);
    }

    public AVLNode doubleRotateRightLeft(AVLNode u) {
        u.right = rotateRight(u.right);
        System.out.println("Double Rotation (kanan ke kiri)");
        return rotateLeft(u);
    }

    public AVLNode successor(AVLNode q) {
        if (q.left != null) {
            AVLNode r = q.left;
            while (r.right != null) {
                r = r.right;
            }
            return r;
        } else {
            AVLNode p = q.parent;
            while (p != null && q == p.right) {
                q = p;
                p = q.parent;
            }
            return p;
        }
    }

    private int height(AVLNode cur) {
        if (cur == null) {
            return -1;
        }
        if (cur.left == null && cur.right == null) {
            return 0;
        } else if (cur.left == null) {
            return 1 + height(cur.right);
        } else if (cur.right == null) {
            return 1 + height(cur.left);
        } else {
            return 1 + maximum(height(cur.left), height(cur.right));
        }
    }

    private int maximum(int a, int b) {
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }

    private void setBalance(AVLNode cur) {
        cur.balance = height(cur.right) - height(cur.left);
    }

    public void showPreOrder() {
        preOrder(root);
    }

    private void preOrder(AVLNode parent) {

        if (parent != null) {
            System.out.print(parent.getData() + " ");
            preOrder(parent.getLeft());
            preOrder(parent.getRight());
        }

    }

    public void showPostOrder() {
        postOrder( root );
    }

    public void showInOrder() {
        inOrder(root);
    }

    private void inOrder( AVLNode parent ) {

        if( parent != null ) {
            inOrder(parent.getLeft());
            System.out.print(parent.getData() + " ");
            inOrder(parent.getRight());
        }
    }

    private void postOrder( AVLNode parent ) {

        if( parent != null ) {
            postOrder(parent.getLeft());
            postOrder(parent.getRight());
            System.out.print(parent.getData() + " ");
        }
    }
}
