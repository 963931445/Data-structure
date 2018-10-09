class Node():
    def __init__(self, item = None):
        self.elem = item
        self.next = None

class LinkList():
    def __init__(self, node=None):
        self._HeadNode = node


    def length(self):
        count = 0
        cur = self._HeadNode
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traval(self):
        # 遍历
        cur = self._HeadNode
        while cur is not None:
            print(str(cur.elem)+("->"),end="")
            cur = cur.next

    def add(self, item):
        # 头部插入
        node = Node(item)
        node.next = self._HeadNode
        self._HeadNode = node

    def append(self, item):
        # 　尾部插入
        node = Node(item)
        cur = self._HeadNode

        while cur.next is not None:
            cur = cur.next
        cur.next = node

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
    def find(self, pos):
        # 查找第几个元素
        cur = self._HeadNode
        count = 0
        if pos <= 0:
            pos = 0
        elif pos >= self.length()-1:
            pos = self.length()-1
        while count < pos:
            count += 1
            cur = cur.next
        return cur.elem

    def search(self, item):
        # 查找元素

        cur = self._HeadNode
        count = 0
        while cur.elem != item:
            if count > self.length():
                return "没有找到"
            cur = cur.next
            count += 1
        return count

    def remove(self, pos):
        # 删除位置
        cur = self._HeadNode
        count = 0
        while count < pos-1:
            count += 1
            cur = cur.next
        cur.next = cur.next.next

    def delete(self, item):
        # 删除元素
        cur = self._HeadNode
        # pre = self._HeadNode
        pre = Node
        count = 0
        while cur is not None:
            if count > self.length()-1:
                return False
            if cur.elem == item:
                # 判断头结点
                if cur == self._HeadNode:
                    self._HeadNode = cur.next
                else:
                    pre.next = cur.next
                return count

            else:
                pre = cur
                cur = cur.next
                count += 1







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