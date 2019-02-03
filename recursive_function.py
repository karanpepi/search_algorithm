def recurs(c):
	if c<=0:
		return 1
	else:
		return c*recurs(c-1)


print(recurs(5))