n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

for x in arr:
    if x % 2 == 0:
        print(x, end=" ")