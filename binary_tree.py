class Node():
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None
class Tree():
    def __init__(self):
        self.root = None
    def add(self,item):
        node  = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.lchild is None:
                current_node.lchild = node
                return
            else:
                queue.append(current_node.lchild)

            if current_node.rchild is None:
                current_node.rchild = node
                return
            else:
                queue.append(current_node.rchild)
    def bread_travel(self):
        "广度遍历"
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.elem)
            if current_node.lchild is  not None:
                queue.append(current_node.lchild)
            if current_node.rchild is not None:
                queue.append(current_node.rchild)
    def pre_order(self,node):
        if node is None:
            return
        print(node.elem)
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        if node is None:
            return

        self.in_order(node.lchild)
        print(node.elem)
        self.in_order(node.rchild)

    def post_order(self, node):
        if node is None:
            return

        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem)
if __name__=="__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.bread_travel()
    tree.pre_order(tree.root)