n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]


for x in arr:
    print(x, end=" ")