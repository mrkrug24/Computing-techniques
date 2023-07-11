import random

a = int(input())
N = int(input())

n = 0
pi = 0
delta = 0

for j in range(10):
    n = 0
    
    for i in range(N):
        x = random.randint(0,a)
        y = random.randint(0,a)
        if x**2 + y**2 <= a**2:
            n += 1
            
    pii = 4 * n / N
    deltai = abs(pii - 3.141592653589793238462643383279)
    pi += pii
    delta += deltai
    
print(pi/10)
print(delta/10)
print(delta/pi)