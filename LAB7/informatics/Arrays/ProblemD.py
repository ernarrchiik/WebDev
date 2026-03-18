n = int(input())

prev = int(input())
count = 0

for _ in range(n - 1):
    x = int(input())
    if x > prev:
        count += 1
    prev = x

print(count)