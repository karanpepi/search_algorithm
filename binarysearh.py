item = [1,45,25,78,56,32,14,22]

item.sort()

print(item)



def search(data,n):

	l = 0

	u = len(data) - 1

	while l <= u:

		mid = (l + u) // 2

		if data[mid] == n:
			return True
		else:

			if data[mid] < n:
				l = mid + 1
			else:
				u = mid - 1
	return False


a = search(item,56)
print(a)