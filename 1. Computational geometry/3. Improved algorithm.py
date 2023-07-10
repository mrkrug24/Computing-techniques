def diff(x, y):
    d = [0, 0]
    d[0] = x[0] - y[0]
    d[1] = x[1] - y[1]
    return d

def cmp(x, y, z):
    if (x[0] * y[1] - x[1] * y[0]) * (x[0] * z[1] - x[1] * z[0]) >= 0:
        return 1
    return 0

def cmp_2(cnt, x, y):
    if cnt == 2 and x[0] * y[1] - x[1] * y[0] == 0:
        return 1
    return 0

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

ad = diff(a, d)
bd = diff(b, d)
cd = diff(c, d)
ab = diff(a, b)
ba = diff(b, a)
ac = diff(a, c)
bc = diff(b, c)

cnt = 0
cnt += cmp(ab, ad, ac)
cnt += cmp (bc, bd, ba)
cnt += cmp (ac, ad, ab)

cnt_2 = 0
cnt_2 += cmp_2(cnt, ab, ad)
cnt_2 += cmp_2(cnt, bc, bd)
cnt_2 += cmp_2(cnt, ac, ad)

if cnt == 3:
    print("Yes")
if cnt != 3 and cnt_2 != 1:
    print("No")
if cnt == 2 and cnt_2 == 1:
    print("The point D lies on the side of the triangle ABC")