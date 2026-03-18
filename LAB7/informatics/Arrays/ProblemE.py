n = int(input())

prev = int(input())
answer = "NO"

for i in range(n - 1):
    x = int(input())
    if (prev > 0 and x > 0) or (prev < 0 and x < 0):
        answer = "YES"
    prev = x

print(answer)