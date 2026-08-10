# Selection sort
# list = [64, 25, 12, 22, 11, 90,7, 3, 5, 6, 8, 9, 10]
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_ind = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_ind]:
#                 min_ind = j
#         arr[i], arr[min_ind] = arr[min_ind], arr[i]
#     return arr

# print(selection_sort(list))





# Bubble sort

List = [4,7,2,44,23,6,9,18,56,37,12,85,49,14,66]

def bub_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
    return list   

print(bub_sort(List))