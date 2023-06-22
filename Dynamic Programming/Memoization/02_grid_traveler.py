

# Classical implementation
'''
def gridTraveler(m, n):
    if(m == 1 and n == 1):
        return 1
    elif(m == 0 or n == 0):
        return 0
    else:
        return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
'''

# -------------------------------------------------------------
# DP implementation
# Memoization


def gridTraveler(m, n, memo={}):

    key = str(m)+','+str(n)

    if key in memo.keys():
        return memo[key]
    elif (m == 1 and n == 1):
        return 1
    elif (m == 0 or n == 0):
        return 0
    else:
        memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n - 1, memo)
        return memo[key]


print(gridTraveler(5, 5, {}))
print(gridTraveler(2, 2, {}))
print(gridTraveler(2, 3, {}))
print(gridTraveler(3, 2, {}))
print(gridTraveler(10, 10, {}))

# This will take a lot of time due to to many recursive call
print(gridTraveler(20, 20, {}))
