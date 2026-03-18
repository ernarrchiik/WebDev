x = int(input())
d = int(input())
count = 0
for i in range(0,x):
    if x % 10 == d:
        count += 1
    count // 10
print(count)