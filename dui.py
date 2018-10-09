import threading
# 单向队列
# class queue():
#     def __init__(self):
#         self.list = []
#     def enqueue(self,item):
#         # self.list.append(item)
#         self.list.insert(0,item)
#     def dequeue(self):
#         return self.list.pop(-1)
#     def length(self):
#         return len(self.list)
#
#
# if __name__=="__main__":
#     q = queue()
#     for item in range(5):
#         q.enqueue(item)
#     for i in range(len(q.list)):
#         print(q.dequeue())


# 双端队列
class doublequeue():
    def __init__(self):
        self.list = []
    def HeadEnQueue(self,item):
        self.list.insert(0,item)
    def HailEnQueue(self,item):
        self.list.append(item)
    def HeadDnQueue(self):
        return self.list.pop(0)
    def HailDnQueue(self):
        return self.list.pop(-1)
    def length(self):
        return len(self.list)
    def is_empry(self):
        return self.list == []

if __name__=="__main__":
    q = doublequeue()
    q.HeadEnQueue(1)
    q.HeadEnQueue(2)
    q.HailEnQueue(-1)
    q.HailEnQueue(-2)
    print(q.is_empry())
    for item in range(q.length()):
        print(q.HailDnQueue())
    print(q.is_empry())
    # print(q.HailDnQueue())
    # print(q.HeadDnQueue())