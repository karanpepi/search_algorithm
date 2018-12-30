ele = [1,2,3,4,6,8,3,23]
n = 23

for index,item in enumerate(ele):
	if n == item:
		print("found at {}".format(index))
		break

