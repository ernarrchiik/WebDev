x = input()

rev = ""

for digit in x:
    rev = digit + rev

print(int(rev))