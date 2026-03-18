def my_min(a, b, c, d):
    m = a
    
    if b < m:
        m = b
    if c < m:
        m = c
    if d < m:
        m = d
    
    return m

nums = []
for _ in range(4):
    nums.append(int(input()))
print(my_min(nums[0], nums[1], nums[2], nums[3]))