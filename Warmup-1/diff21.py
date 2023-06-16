# Warmup-1 > diff21

# Given an int n, return the absolute difference between n and 21, except return double the
# absolute difference if n is over 21.

def diff21(n):
  diff = abs(n - 21)
  
  if n > 21:
    diff *= 2
    return diff
  return diff

"""
Solution:
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
"""
