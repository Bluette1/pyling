# Given an array of integers, find the sum of the two largest numbers

def sum_max(arr):
  max = arr[0]
  next_max = arr[1]
  if arr[0] < arr[1]:
    max = arr[1]
    next_max = arr[0]
  for i in range(2, len(arr)):
    if arr[i] > max:
      next_max = max 
      max = arr[i]  
    elif arr[i] > next_max:
      next_max = arr[i]
  return max + next_max