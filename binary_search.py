def sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
# 递归
def binary(list1,x):
    n = len(list1)
    if n > 0:
        mid = n // 2
        if x == list1[mid]:
            return True
        elif x < list1[mid]:
            return binary(list1[:mid], x)
        else:
            return binary(list1[mid+1:],x)
    else:
         return False
# 非递归
def binary2(list,x):
    pre = 0
    back = len(list)
    while pre < back:
        mid = (pre + back)//2
        if x == list[mid]:
            return mid
        elif x>list[mid]:
            pre = mid +1
        else:
            back = mid-1
    return False
if __name__=="__main__":
    list=[1,5,6,4,48,423,4,0]
    list1 = sort(list)
    print(list1)
    print(binary2(list1,48))