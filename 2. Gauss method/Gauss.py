n = int(input()) 
a = [[int(j) for j in input().split()] for i in range(n)]
k = a[0][0]

for i in range(n - 1):
    for j in range(n - 1):
        m = a[j + 1][i] / k
        for j in range(n + 1):
            k = a[i][i]
            a[j + 1][j] = a[j + 1][j] - a[i][j] * m

ans = []
p = 0

for i in range(n - 1):
    if a[n - 1 - i][n - 1 - i] == 0:
        print("No roots of the equation")
        exit(0)
        
    x = (a[n - 1 - i][n] - p) / a[n - 1 - i][n - 1 - i]
    ans.append(x)
    p = 0
    
    for j in range(len(ans)):
        p = p + a[n - 2 - i][n - 1 - i + j] * ans[j]

p = 0

for j in range(len(ans)):
    p = p + a[0][n - 1 - j] * ans[j]

x = (a[0][n] - p) / a[0][0]
ans.append(x)
ans.reverse()

for i in range(len(ans)):
    ans[i] = round(ans[i], 5)

print(*ans)