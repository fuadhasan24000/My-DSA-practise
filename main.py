# CHECK IF A NUMBER IS PALINDROME OR NOT
#TC O(logN) or O(d)

# def is_palindrome(number1):
#     num=0
#     number = number1
#     while number != 0:
#         num = (number % 10)  + num * 10
#         number = number // 10
#     return num == number1




# ARMSTRONG NUMBER
# TC O(logN) or O(d)

# def armstrong(num):
#     num1 =num
#     result=0
#     n = len(str(num))
#     for i in range(n):
#         result = (num1 % 10) ** n + result
#         num1 = num1 // 10
#     return result == num

# print(armstrong(153))





#Print Factors 

# solve 1 
#TC O(d)  SC O(k) where k is the number of factors

# def print_factors(num):
#     result = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             result.append(i)
#     return result
# print(print_factors(12))

#Solve 2 
#TC O(√n) + O(nlogn)  SC O(k) where k is the number of factors

# def print_factors(num):
#     result = []
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             result.append(i)
#             if i != num // i:
#                 result.append(num // i)
#     return sorted(result)
# print(print_factors(36))



# Hashing:

# problem: 2 lists are given, find how many times an element of list 2 appeared in list 1.
# list 1 can only have elements from 1 to 10 
# both lists can have upto 10^8 numbers of elements

# list1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 123,6,634,565,344,23,6,4,2,8,45,97,2,1,7,9,5]

# hash_list= [0]*11
# for i in list1:
#     hash_list[i] += 1
# for j in list2:
#     if j<0 or j>10:
#         print(0,end=" ")
#     else:
#         print(hash_list[j], end=" ")

#TC O(n+m)


#solve using dictionary
# hash1 = {}
# for i in list1:
#     if i not in hash1:
#         hash1[i] = 1
#     else:
#         hash1[i] = hash1[i]+ 1
# for j in list2:
#     if j not in hash1:
#         print(0)
#     else:
#         print(hash1[j])






#Recursion:
# calling a function inside that function

#Q: print Fuad 5 times using recursion

# count = 0
# def pepe():
#     global count
#     if count == 5:
#         return
#     print("Fuad")
#     count += 1
#     pepe()
# pepe()

#TC o(N) SC O(N)

#types:i) head ii) tail
#recursion tree

# recursion using parameters

# def pepe(x,N):
#     if N == 0:
#         return
#     print(x)
#     pepe(x,N-1)
# pepe(4,3)

#functional recursion

# def pepe(n):
#     if n==1:
#         return 1
#     return n+pepe(n-1)
# print(pepe(10))

# factorial
# def fac(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fac(n-1)
# print(fac(0))



# Reverse an array using recursion

# arr = [5,6,7,2,6,1,9,0,34,6,78,4,62,1,9,36,8]
# i= len(arr)
# def rev(arr):
#     global i
#     if i == 0:
#         return
#     i-=1
#     print(arr[i])
#     rev(arr)
#
# rev(arr)


# Reverse an array using recursion (4 to 8th index only)

# arr = [5,6,7,2,6,1,9,0,34,6,78,4,62,1,9,36,8]
# def rev(arr, l, r):
#     if l>=r:
#         return
#     arr[l], arr[r] = arr[r], arr[l]
#     rev(arr, l+1, r-1)
#
# rev(arr, 4, 8)
# print(arr)

# TC O(N/2) SC O(N/2) stack space




# Check palindrome using recursion

# word = "ajerhthrutr"
# print(len(word))
# def rev(arr, l, r):
#
#     if l>=r:
#         return True
#     if arr[l] != arr[r]:
#         return False
#     return rev(arr, l+1, r-1)
# print(rev(word, 0, len(word)-1))




# Fabonacci number

n = 6
a =0
b=1
for i in range(int(n/2)):
    b += a
    a += b

if n%2 == 0:
    print(b)
else:
    print(a)