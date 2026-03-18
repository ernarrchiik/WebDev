def xor(x, y):
    return (x and not y) or (not x and y)
inputs = []
for _ in range(2):
    inputs.append(int(input()))

x = bool(inputs[0])
y = bool(inputs[1])


result = xor(x, y)
print(int(result))