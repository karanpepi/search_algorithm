item = [1,45,25,78,56,32,14,22]

item.sort()

print(item)



def search(list,n):

	l = 0

	u = len(list) - 1

	while l <= u:

		mid = l + u // 2

		if list[mid] == n:
			return True
		else:
			if list[mid] < n:
				l = mid + 1
			else:
				u = mid - 1
	return False
