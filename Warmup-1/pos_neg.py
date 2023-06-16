# Warmup-1 > pos_neg

# Given 2 int values, return True if one is negative and one is positive. Except if the
# parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  if ((a < 0 and b > 0) or (a > 0 and b < 0)) and not negative:
    return True
  elif negative and (a < 0 and b < 0):
    return True
  else:
    return False

"""
Solution:
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
"""
