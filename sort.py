def bubble_sort(list):
    for j in range(len(list)-1):
        count = 0
        for index in range(len(list)-1-j):
            if list[index] > list[index+1]:
                list[index],list[index+1] = list[index+1],list[index]
                count += 1
        if 0 == count:
            return list,count,j
    return list,count,j

l =[1,2,9,10,4,7,6]
# print(bubble_sort(l))

# def select_sort(list):
#     for i in range(len(list)-1):
#         min_index = i
#         for j in range(i+1,len(list)):
#             if list[min_index] > list[j]:
#                 min_index = j
#         list[min_index],list[i] = list[i], list[min_index]
#     return list
#
# # print(select_sort(l))
#
# def insert_sort(list):
#     for i in range(1,len(list)):
#         for j in range(i,0,-1):
#             if list[j-1] > list[j]:
#                 list[j],list[j-1] = list[j-1],list[j]
#             else:
#                 break
#
#     return list
#
# print(insert_sort(l))


def shell_sort(list):
    n = len(list)
    gap = n // 2


    while gap > 0:
        for j in range(gap,n):
            i = j
            while i >0:
                if list[i] < list[i-gap]:
                    list[i],list[i-gap] = list[i-gap],list[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return list

print(shell_sort(l))