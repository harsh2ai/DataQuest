# This program will demonstrate the
# Insertion sorting.

a = [54, 32, 32, 5, 82, 34, 5, 9]

for i in range(1, len(a), 1):
	key = a[i]
	j = i-1
	while(j>-1 and a[j]>key):
		a[j+1] = a[j]
		j = j-1
	a[j+1] = key

print(a)