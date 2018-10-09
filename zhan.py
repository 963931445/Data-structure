class Stack():
    def __init__(self):
        self.list=[]
    def push(self,item):
        # self.list=item
        self.list.append(item)
    def pop(self):
        return self.list[-1]
    def peek(self):
        return self.list[0]
    def is_empty(self):
        num = 0;
        for item in self.list:
            num += 1;
        if not num:
            return True
        else:
            return False
    def length(self):
        num = 0;
        for item in self.list:
            num+=1;
        return num


s = Stack()
s.push(1)
# s.push(2)
print(s.pop())
print(s.is_empty())
print(s.length())
