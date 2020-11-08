# Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# instantiate the total as 0
total = 0

for x in range (1,1000):
    # check if x is either a multiple of 3 or 5
    if((x%3 == 0) or (x%5 == 0)):
        # if so, then we add x to the total
        total = total + x

print(total)
