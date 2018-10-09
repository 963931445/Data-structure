class Node():
    def __init__(self, item = None):
        self.elem = item
        self.next = None

class LinkList():
    def __init__(self, node=None):
        self._HeadNode = node
        node.next = self._HeadNode
    def is_empty(self):
        return self._HeadNode == None
    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._HeadNode
        while cur.next != self._HeadNode:
            count += 1
            cur = cur.next
        return count

    def traval(self):
        # 遍历
        cur = self._HeadNode
        if self.is_empty():
            return
        while cur.next != self._HeadNode:
            print(str(cur.elem)+("->"),end="")
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        # 头部插入
        node = Node(item)
        if self.is_empty():
            self._HeadNode = node
            node.next = node
        node.next = self._HeadNode
        while cur.next != self._HeadNode:
            cur = cur.next
        node.next = self._HeadNode
        self._HeadNode = node
        cur.next = node

    def append(self, item):
        # 　尾部插入
        node = Node(item)
        cur = self._HeadNode
        if self.is_empty():
            self._HeadNode = node
            node.next = node
        else:
            while cur.next != self._HeadNode:
                cur = cur.next
            cur.next = node
            node.next = self._HeadNode

    def insert(self, pos, item):
        # 指定位置插入
        node  = Node(item)
        cur = self._HeadNode
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            while count< (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
    # def find(self, pos):
    #     # 查找第几个元素
    #     cur = self._HeadNode
    #     count = 0
    #     if pos <= 0:
    #         pos = 0
    #     elif pos >= self.length()-1:
    #         pos = self.length()-1
    #     while count < pos:
    #         count += 1
    #         cur = cur.next
    #     return cur.elem

    def search(self, item):
        # 查找元素
        cur = self._HeadNode
        count = 0
        if self.is_empty():
            return False
        while cur != self._HeadNode:
            if cur.elem == item:
                return count
            cur = cur.next
            count += 1
        # 判断尾节点
        if cur.elem == item:
            return count
        return False

    # def remove(self, pos):
    #     # 删除位置
    #     cur = self._HeadNode
    #     count = 0
    #     while count < pos-1:
    #         count += 1
    #         cur = cur.next
    #     cur.next = cur.next.next

    def delete(self, item):
        # 删除元素
        cur = self._HeadNode
        pre = None
        count = 0
        if self.is_empty():
            return
        while cur.next != self._HeadNode:
            if cur.elem == item:
                # 判断头结点
                if cur == self._HeadNode:
                    # 找尾节点
                    rear  = self._HeadNode
                    while rear.next != self._HeadNode:
                        rear = rear.next
                    self._HeadNode = cur.next
                    rear.next = self._HeadNode
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
            count += 1
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self._HeadNode:
                # 链表只有一个节点
                self._HeadNode = None
            else:
                pre.next = cur.next







if __name__ == "__main__":
    l = LinkList(Node(100))
    # print(l.length())
    l.add(200)
    l.add(500)
    l.append(600)
    l.append(900)
    l.insert(2,20)
    # print(l.find(2))
    # l.remove(3)
    # print(l.search(500))
    print(l.delete(5000))
    l.traval()