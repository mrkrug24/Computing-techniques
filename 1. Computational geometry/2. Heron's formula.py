a = input().split()
a[0] = float(a[0])
a[1] = float(a[1])

b = input().split()
b[0] = float(b[0])
b[1] = float(b[1])

c = input().split()
c[0] = float(c[0])
c[1] = float(c[1])

d = input().split()
d[0] = float(d[0])
d[1] = float(d[1])

def pram(x, y, z, f):
    k = (y[1] - x[1]) / (y[0] - x[0]) 
    q = x[1] - k * x[0]
    
    if ((k * f[0] + q) <= f[1] and (k * z[0] + q) <= z[1]) or ((k * f[0] + q) >= f[1] and (k * z[0] + q) >= z[1]):
        return 1
    else:
        return 0

r = pram(a, b, c, d)  
r = r + pram(a, c, b, d)
r = r + pram(b, c, a, d)

if r == 3:
    print("Yes")
else:
    print("No")