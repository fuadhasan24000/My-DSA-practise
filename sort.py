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

# List = [4,7,2,44,23,6,9,18,56,37,12,85,49,14,66]

# def bubble_sort(list):
#     n = len(list)
    
#     for i in range(n):
#         is_swap = False                    #best case optimization
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1], list[j]
#                 is_swap = True 
#         if is_swap == False:
#             return list
#     return list   

# print(bubble_sort(List))




# Inserton sort

# List = [4,7,2,44,23,6,9,18,56,37,12,85,49,14,66]

# def ins_sort(arr):
#     n= len(arr)
#     for i in range(1,n):
#         key = arr[i]
#         j= i-1
#         while j>=0 and arr[j] > key:
#             arr[j+1]= arr[j]
#             j-=1
#         arr[j+1]= key
#     return arr
# print(ins_sort(List))




#  Merge sort

List = [4,7,2,44,23,6,9,18,56,37,12,85,49,14,66]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle=len(arr)//2
    left = merge_sort(arr[:middle])
    right= merge_sort(arr[middle:])
    i=0
    j=0
    result =[]
    while i<len(left) and j<len(right):
        
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
            
        elif left[i] > right[j]:
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result           

print(merge_sort(List))