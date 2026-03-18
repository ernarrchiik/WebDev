n = int(input())

if n < 3:
    for i in range(n):
        int(input())
    print(0)
else:
    first = int(input())
    second = int(input())
    count = 0

    for i in range(n - 2):
        third = int(input())
        if second > first and second > third:
            count += 1
        first = second
        second = third

    print(count)