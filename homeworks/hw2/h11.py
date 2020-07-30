sum_so_far = 0
# remember that range() does not include the last element!
# that's why we need to use 123457 instead of 123456
for i in range(123457):
    sum_so_far += 2*i
print(sum_so_far)
