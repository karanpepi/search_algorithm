
numbers = [999,223,33,44,214,3,53]


def sorting(numbers):
	# print(numbers)
	for i in range(len(numbers)): 
      

	    min_idx = i 
	    for j in range(i+1, len(numbers)):
	        if numbers[min_idx] > numbers[j]: 
	            min_idx = j 
     
	    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i] 

sorting(numbers)

print(numbers)