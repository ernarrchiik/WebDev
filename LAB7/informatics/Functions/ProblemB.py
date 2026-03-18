def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

inputs = []
for _ in range(2):
    inputs.append(input())

a = float(inputs[0])
n = int(inputs[1])

print(power(a, n))