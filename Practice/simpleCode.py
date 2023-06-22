# grid traveller tabulation

def grid(m, n):

    table = [[0 for i in range(m+1)] for i in range(n+1)]
    table[1][1] = 1

    for i in range(n+1):
        for j in range(m+1):
            if(i+1 <= n):
                table[i+1][j] += table[i][j]
            if(j+1 <= m):
                table[i][j+1] += table[i][j]


    print(table)


grid(5,6)