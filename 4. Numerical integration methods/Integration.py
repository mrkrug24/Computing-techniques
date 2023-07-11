import math

def f(x):
    return math.sin(x) * x

sum = 0
left = float(input())
right = float(input())
step = float(input())

x = left

for i in range(math.ceil((right - left) / step)):
    sum = sum + step * f(x)
    x = x + step
    
print('Left', sum)

sum = 0
x = left + step

for i in range(math.floor((right - left) / step)):
    sum = sum + step * f(x)
    x = x + step

print('Right', sum)

sum = 0
x = left + step / 2

for i in range(math.ceil((right - left) / step)):
    sum = sum + step * f(x)
    x = x + step

print('Middle', sum)

sum = 0
x = left

for i in range(math.ceil((right - left) / step)):
    sum = sum + step * (f(x) + f(x + step)) / 2
    x = x + step

print('Trapeze', sum) 