# FUNCTIONS
# function definition
def add_2_numbers():
  a = 1 + 2
  print(a)

# add_2_numbers() # function call

# function with parameters
def add_2_nums(first_num, second_num):
  x = first_num + second_num
  print(x)

# add_2_nums(1, 2)
# add_2_nums(4, 5)
# add_2_nums(7, 5)

# functions with return types
# def multiply_2_numbers(first, second):
#   result = first * second
#   return result

# global scope
x = 3

def ret_zero():
  # scope - local scope
  # x = 0
  return x


# print(ret_zero())

def ret_nothing():
  x = 1 + 2

def give_me_name():
  return "cyan"

None # denotes Nothing

my_name = give_me_name()


def add2_and_give(first, second):
  # s = first + second
  return first + second

ans_i_asked = add2_and_give(4, 5)

# print(ans_i_asked)



# def is_prime(num):
#   flag = True

#   for x in range(2, num):
#     if num % x == 0: 
#       flag = False
#       break
    
#   return flag

# is_5_prime = is_prime(5)
# is_2_prime = is_prime(2)
# is_10_prime = is_prime(10)

# print(is_5_prime)
# print(is_2_prime)
# print(is_10_prime)

# def is_prime(n):
#   for x in range(2, n):
#     if n % x == 0:
#       return False
#   return True

def is_prime(num):
  for x in range(2, num):
    if num % x == 0: 
      return False
  return True

# def is_even(num):
#   if num % 2 == 0:
#     return True
#   return False

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False
# print(is_prime(10))

# print(is_even(5))

def find_max_in_list(my_list):
  pass # placeholder

# usage
max_val = find_max_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(max_val)