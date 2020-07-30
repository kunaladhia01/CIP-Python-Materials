# The nth term will be p**4, where p is the nth prime number.
# The factors will be 1, p, p**2, p**3, and p**4.

count = 1 # We'll ignore 2, the first prime number, and start at 3.
current_value = 3
while count < 100001: # we will exit this while loop after the 100001th prime is found.
    is_prime = True
    # this is an efficient way to check if a number is prime, but any checker would work here.
    # the + 1 term will account for any rounding issues
    for i in range(2, int((current_value)**0.5) + 1):
        if current_value % i == 0:
            is_prime = False
            break # if we found another factor other than 1 and i, we don't need to check the rest of the terms
    if is_prime: # we found no factors for current_value except 1 and itself.
        count += 1
        if count == 100001:
            print(1, current_value, current_value**2, current_value**3, current_value**4)
            break
    # We know even numbers aren't prime, so we can skip them. current_value will go from 3, 5, 7, etc.
    current_value += 2
