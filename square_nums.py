"""
Convert the following function into a generator so you won't need a list anymore:

def square_numbers(nums):
  result = []
  for i in nums:
    result.append(i*i)
  return result
 

print(my_nums) # [1, 4, 9, 16, 25]

"""

def square_numbers(nums):
  for i in nums:
    # generators don't hold the entire result in memory, it yields one result at a time
    yield(i*i)

# create generator object
my_nums = square_numbers([1,2,3,4,5])

# list comprehension does the same as the square_numbers function above
my_nums = [x*x for x in [1,2,3,4,5]]
# convert list comprehension to generator:
my_nums = (x*x for x in [1,2,3,4,5])
# to print all values, convert generator to list:
print(list(my_nums)) # [1, 4, 9, 16, 25]

print(next(my_nums)) # 1
print(next(my_nums)) # 4
print(next(my_nums)) # 9
print(next(my_nums)) # 16
print(next(my_nums)) # 25

# you can use a for loop with a generator
# it stops when necessary
for num in my_nums:
  print(num)