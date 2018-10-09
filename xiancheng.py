import time
import threading
# def demo():
#     print("你好")
#     time.sleep(1)
# if __name__=='__main__':
#
#     for item in range(5):
#         threading.Thread(target=demo).start()
#
num = 0
mutex=threading.Lock()
class mythread(threading.Thread):
    def run(self):
        mutexflag  = mutex.acquire()
        global num
        if mutexflag:
            num += 1
            print(self.name+str(num))
            mutex.release()

def demo():
    for i in range(5):
        mythread().start()
        mythread().start()
if __name__=="__main__":
    demo()

# 一定要重写run方法
# 每个线程一定有一个名字
# run方法结束时该线程介绍
#　无法控制线程的调度，操作系统说了算的；但是可以通过别的方式影响线程调度，互斥，死锁，条件变量
# 线程状态

