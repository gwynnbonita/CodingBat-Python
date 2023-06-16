# Warmup-1 > sum_double

# Given two int values, return their sum. Unless the two values are the same, then return
# double their sum.

def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b
  
"""
Solution:
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum
"""
