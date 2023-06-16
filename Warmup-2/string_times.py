# Warmup-2 > string_times

# Given a string and a non-negative int n, return a larger string that is n copies of the
# original string.

def string_times(str, n):
  return str * n

"""
Solution:
def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result
"""
