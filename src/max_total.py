import math

def max_total(T, carton_sizes):
  '''
  A cool drinks' company wants to try out using different carton sizes
  to see what works best for the deliveries. Deliveries can contain 
  cool drinks packed in different carton sizes. 
  Write a program containing a function that returns the number of
  cool drinks to pack given a list of available sizes of the cartons 
  and the order from the store. 
  Find the value as close to - but not more than - the order from the
  store.

  EXAMPLE:  
  Input: 
  max_total(20,[2,4])
  max_total(25,[2,3])
  max_total(91,[6])
  max_total(43,[2, 5])
  max_total(100,[6,3,2])
  max_total(100,[6,3])
  
  Output:
  20
  25
  90
  43
  100
  99
  '''
  
  # This is a dynamic programming challenge
  # For each subproblem/state i, i <= T (order from the store):
  #  - Initialise solution for i > 0 as Infinity.
  #    Solution for i = 0 is set to 0.
  #  - Identify carton sizes j, where size_j <= i
  #      - Let solution(i - size_j) be m
  #      - If (m + 1) < current solution for i, update it to (m + 1)
  # Loop through the table from the order T downwards to find the max total possible
  # Similar to
  # https://github.com/Bluette1/Miscellaneous/blob/master/src/miscellaneous/dynamicprogramming/MinimumCoins.java
  # https://www.topcoder.com/thrive/articles/Dynamic%20Programming:%20From%20Novice%20to%20Advanced
  infinity = math.inf
  total = [0] + [infinity] * (T)
  
  for i in range(T + 1):
    for j in range(len(carton_sizes)):
      size_j = carton_sizes[j]
      if size_j <= i:
        m = total[i - size_j]
        total[i] = min(total[i], m + 1)
        
  for i in range(T, 0, -1):
    if total[i] < infinity:
      return i
print(max_total(20,[2,4]))
print(max_total(25,[2,3]))
print(max_total(91,[6]))
print(max_total(43,[2, 5]))
print(max_total(100,[6,3,2]))
print(max_total(100,[6,3]))

