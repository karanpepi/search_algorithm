
numbers = [1,223,33,44,214,3,53]


def sorting(numbers):
	# print(numbers)
	for i in range(len(numbers)-1,0,-1):
		for j in range(i):
			# print(j)
			if numbers[j] > numbers [j+1]:
				# temp = numbers[j]
				# numbers[j] = numbers[j+1]
				# numbers[j+1] = temp
				numbers[j+1],numbers[j] = numbers[j],numbers[j+1]

sorting(numbers)

print(numbers)