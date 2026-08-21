# FIXED: range(1, 10) stopes before 10, used range(1, 11) to print 1 to 10.
for i in range(1, 11):
    print(i)

# FIXED: n was never decreased, causing an infinite loop. Decrease n by 1 each time
n = 3
while n > 0:
    print(n)
    n = n -1

# FIXED: total was been reset to 0 in side the loop, initialize it before the loop
total = 0
for i in range(1, 6):
    total = total + i
print(total)