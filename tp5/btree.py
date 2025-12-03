from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from collections import deque

@dataclass
class BinaryTree:
    """
    A binary tree is a tree data structure in which each node has at most two children,
    which are referred to as the left child and the right child.

    The BinaryTree class is a dataclass with a single field, root, which is a reference to the root node of the tree.

    The Node class is a nested dataclass with three fields: key, left, and right.
    The key field is an integer that stores the value of the node.
    The left and right fields are references to the left and right children of the node, respectively.

    Example:
        >>> bt = BinaryTree(Node(2, Node(1, Node(0)), Node(4, Node(3), Node(5))))
    """
    root: Node | None = None


@dataclass
class Node:
    key: int
    left: Node | None = None       # "Or None" for terminal nodes
    right: Node | None = None



def bt_is_empty(bt: BinaryTree) -> bool:
    return bt.root is None

def bt_root(bt: BinaryTree) -> Node:
    if bt_is_empty(bt):
        raise ValueError
    return bt.root

def bt_iter_dfs(n: Node) -> Iterator[Node]:
    if n is None:
        pass
    else:
        for g in bt_iter_dfs(n.left):
            yield g
        yield n
        for g in bt_iter_dfs(n.right):
            yield g


def bt_iter_bfs(n: Node) -> Iterator[Node]:
    if n is not None:
        file= deque([])
        file.append(n)
        while len(file) > 0:
            tete= file.popleft()
            yield tete
            if tete.left:
                file.append(tete.left)
            if tete.right:
                file.append(tete.right)



def bt_height(bt: BinaryTree) -> int:
    def bt_height_aux(n:Node)->int:
        if n is None:
            return -1
        else:
            return  max(bt_height_aux(n.left),bt_height_aux(n.right)) +1
    return bt_height_aux(bt.root)


def bt_size(bt: BinaryTree) -> int:
    def bt_size_aux(n:Node)->int:
        if n is None:
            return 0
        else:
            return  bt_size_aux(n.left) + bt_size_aux(n.right) +1
    return bt_size_aux(bt.root)

def bt_str(bt: BinaryTree) -> str:
    def bt_str_aux(n:Node):
        if n is None:
            return ''
        if n.right is None and n.left is None:
            return f"{n.key}"
        else:
            return f"{n.key} " + f"({bt_str_aux(n.left)}) " + f"({bt_str_aux(n.right)})"
    return bt_str_aux(bt.root)

def bt_new(nodes: list[int | None] | None = None) -> BinaryTree:
    if nodes is None or nodes ==[] or nodes[0] is None:
        return BinaryTree(None)
    else:
        def bt_new_aux(l,i):
            if i>=len(l) or l[i] is None:
                return None
            else:
                return Node(nodes[i],bt_new_aux(l,(2*i)+1),bt_new_aux(l,(2*i)+2))
        return BinaryTree(bt_new_aux(nodes,0))

def bt_is_bst(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_bst function not implemented yet")


def bt_is_heap(bt: BinaryTree) -> bool:
    raise NotImplementedError("bt_is_heap function not implemented yet")


def bt_lca(bt: BinaryTree, a: int, b: int) -> int:
    raise NotImplementedError("bt_lca function not implemented yet")


def bt_prettystr(bt: BinaryTree) -> str:
    raise NotImplementedError("bt_prettystr function not implemented yet")


if __name__ == '__main__':
    a = BinaryTree(Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))