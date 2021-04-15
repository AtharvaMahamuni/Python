
def gridTraveler(m, n):
    table = [[0 for x in range(n+1)] for y in range(m+1)]
    table[1][1] = 1

    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current
    return table[m][n]


print(gridTraveler(1, 1))
print(gridTraveler(2, 2))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))
print(gridTraveler(10, 10))
print(gridTraveler(20, 20))

# Outputs:
# 1
# 2
# 3
# 3
# 6
# 48620
# 35345263800
