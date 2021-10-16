# TODO: Printing numbers:

# def printf(n):

#     if n==0:
#         return
    
#     else:
#         print(n)
#         printf(n-1)


# printf(5)


# TODO: Fact


# def fact(n):
#     if n == 0 or n == 1:
#         return 1
    
#     else:
#         return n*fact(n-1)

# print(fact(5))



# TODO: power of x**y

# def powf(m,n):
#     if n == 1:
#         return m
    
#     else:
#         return m*powf(m,n-1)

# print(powf(4, 5))
# print(4**5)


# TODO: Digit Sum

# def digitSum(n):
#     if n == 0:
#         return 0
    
#     return (n%10 + digitSum(n//10))

# print(digitSum(1234))
# print(digitSum(7263))


# TODO: digit Product

# def digitProduct(n):
#     if n == 0: 
#         return 1
    
#     return (n%10 * digitProduct(n//10))

# print(digitProduct(123))
# print(digitProduct(623))
# print(digitProduct(6423))


# TODO: reverse the Number

# FIXME: Iterative
# def rev(n):
#     num = 0
#     while n != 0:
#         num = num*10 + n%10
#         n //= 10
#     return num

# print(rev(1234))



# TODO: Fibonacci

# def fib(n):

#     if n == 1 or n == 2:
#         return n-1
    
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(35))



# TODO: fibonacci with diary

# def fib(n, diary={1:0, 2: 1}):
    
#     if n in diary.keys():
#         return diary[n]
    
#     else:
#         diary[n] = fib(n-1, diary) + fib(n-2, diary)
#         return diary[n]

# print(fib(100))



# TODO: Subsets

# def subset(s, index, holder, my_list = []):

#     if index == len(s):
#         my_list.append(holder) # String or Array
#         return        

#     subset(s, index+1, holder+s[index], my_list)
#     subset(s, index+1, holder, my_list)

#     return my_list

# my_list = subset('abc',0,"", my_list = [])
# print(my_list)



# TODO: Decimal to Binary

# FIXME: Approach 1
# def decToBin(n):
    
#     if n == 1 or n == 0:
#         print(n, end="")
#         return     

#     decToBin(n//2)
#     print(n%2, end="")


# FIXME: Approach 2

# def decToBin(n):
#     if n == 1 or n == 0:
#         return str(n)
    
#     return (decToBin(n//2)+str(n%2))

# # decToBin(12)
# print(decToBin(12))
# # decToBin(0)
# print(decToBin(0))
# # decToBin(100)
# print(decToBin(100))
# # decToBin(2)
# print(decToBin(2))


# TODO: Nearby Duplicates 
# mydduuppllicatee -> myduplicate

# def dup(s):
#     if len(s) == 1:
#         return s
    
#     elif(s[0]==s[1]):
#         return dup(s[1:])

#     else:
#         return s[0] + dup(s[1:])
    
# print(dup("mydduupplicatee"))


# TODO: Pascal Triangle

# def pasc(n):
#     if n == 1:
#         return [1]

#     else:
#         line = [1]

#         last_line = pasc(n-1)

#         for i in range(n-2):
#             line += [last_line[i]+last_line[i+1]]

#         line += [1]

#         return line


# print(pasc(1))
# print(pasc(2))
# print(pasc(3))
# print(pasc(4))
# print(pasc(5))
# print(pasc(6))
# print(pasc(7))







