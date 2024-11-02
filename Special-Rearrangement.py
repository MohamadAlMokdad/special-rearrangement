def special_rearrangement(nums):
  #lists to hold even and odd numbers
  even_nums=[]
  odd_nums=[]

  # Loop through each number in the input list
  # Check whether each number is even or odd
  for i in range(len(nums)):
    if nums[i]%2==0:
      even_nums.append(nums[i])
    else:
      odd_nums.append(nums[i])
      
  #Combine the list of even numbers and the list of odd numbers
  return even_nums + odd_nums





  
    
  
    


