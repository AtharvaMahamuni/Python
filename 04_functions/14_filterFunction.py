# filter function:

'''
filter function accept 2 argumants
'''

# def even_no(a):
#     return a % 2 == 0

# even_no = lambda a: a%2==0

num = [12, 13, 4, 6, 3, 6, 7, 8, 9, 5, 3, 2, 14]
even = list(filter(lambda a: a % 2 == 0, num))
# even = list(filter(even_no, num))
print(even)


