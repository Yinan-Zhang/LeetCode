


class Node:
    def __init__(self):
        self.val;
        self.left;
        self.right;


def tree_to_list( root ):
    if root is None: return None;

    prev_visit_node = None;
    def in_order_traversal(node):
        if node.left is None and node.right is None:
            prev_visit_node = node;

        if node.left:
            in_order_traversal(node.left);
        prev_visit_node.next = node;
        prev_visit_node = node;
        
        if node.right:
            in_order_traversal(node.right);
