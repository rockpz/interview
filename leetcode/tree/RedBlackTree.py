”“”
二叉查找树 binary search tree
若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值
若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值
任意节点的左、右子树也分别为二叉查找树
没有键值相等的节点

红黑树 red black tree
每个节点都带有颜色属性的二叉查找树，颜色为红色或黑色
节点是红色或黑色
根是黑色
所有的叶子都是黑色
每个红色节点必须有两个黑色的子节点
从任意节点到其每个叶子的所有简单路径都包含相通数目的黑色节点

插入5种情况
1: 插入的新节点N是红黑树的根节点
2: N的父节点是黑色
3: N的父节点是红色，叔叔节点也是红色
4: N的父节点为红色，叔叔节点为黑色
5: N的父节点为红色，叔叔节点为黑色
“”“
RED = 0
BLACK = 1

class BSTNode():
    def __init__(self, key, data):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.data = data


class RBTNode():
    def __init__(self, color, key=None, data=None):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.color = color
        self.data = data


class RBTree():
    def __init__(self, root=None):
        self.root = root
        self.sentinel = RBTNode(RED)

# node.color = RED
def insert_case1(node):
    if not node.parent:
        node.color = BLACK
    else:
        insert_case2(node)

def insert_case2(node):
    if node.parent.color == BLACK:
        return
    else:
        insert_case3(node)

def insert_case3(node):
    if uncle(node) && uncle(node).color == RED:
        node.parent.color = BLACK
        uncle(node).color = BLACK
        grandparent(node).color = RED
        insert_case1(grandparent(node))
    else:
        insert_case4(node)

def insert_case4(node):
    if node == node.parent.right && node.parent == grandparent(node).left:
        rorate_left(node.parent)
        node = node.left
    elif node == node.parent.left && node.parent == grandparent(node).right:
        rotate_right(node.parent)
        node = node.right
    insert_case5(node)


def insert_case5(node):
    node.parent.color = BLACK
    grandparent(node).color = RED
    if node == node.parent.left && node.parent == grandparent(node).left:
        rotate_right(grandparent(node))
    else:
        rotate_left(grandparent(node))