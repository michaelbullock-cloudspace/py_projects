'''count = 0

while count < 10:
    print (f"count: {count}")
    if count == 5:
        break # STOP HERE
    count += 1'''

n = 5

while n > 0:
    n -= 1
    if n == 2: # Skip 2 and continue while loop
        continue
    print (n)
print('Loop ended.')