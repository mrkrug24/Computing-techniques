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

def line(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)
  
def area(x, y, z):
    half_sum = (x + y + z) / 2
    return (half_sum * (half_sum - x) * (half_sum - y) * (half_sum - z)) ** 0.5

ab = line(a, b)
bc = line(b, c)
ac = line(a, c)

ad = line(a, d)
bd = line(b, d)
cd = line(c, d)

S0 = area(ab, bc, ac)
S1 = area(ab, bd, ad)
S2 = area(bd, bc, cd)
S3 = area(ad, cd, ac)

flag = 0

if abs(S0 - S1 - S2 - S3) < 0.001:
    flag = 1
    print("Yes")

if abs(S0 - S1 - S2 - S3) > 0.001:
    print("No")

if S1 == 0 or S2 == 0 or S3 == 0 and flag == 1:
    print("The point D lies on the side of the triangle ABC")