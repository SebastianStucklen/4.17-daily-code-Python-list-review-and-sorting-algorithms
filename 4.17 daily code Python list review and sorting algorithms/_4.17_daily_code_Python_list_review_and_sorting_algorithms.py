import random
list = []
for i in range(11):
	r = random.randint(0,200)
	list.append(r)
print(f"List: {list}")
list.sort()
print(f"Sorted: {list}")
print(f"Smallest: {list[0]}")
print(f"Median: {list[5]}")
print(f"Largest: {list[10]}")
def average():
	total = 0
	for i in range(11):
		total += list[i]
	size = len(list)
	print(f"Total: {total}")
	print(f"Size: {size}")
	return total/size
print(f"Average: {average()}")
