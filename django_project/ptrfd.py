inp = "She likes to sing"
inp = inp.split(" ")
for i in inp:
	if i.lower().startswith("s"):
		print(i,end = " ")


dic_t = {
	"A" : 3,
	"B" : 7,
	"C" : 2
}

for j in dic_t.values():
	if j%2 != 0 and j < 6:
		print(j)

list_w = [1,2,3,4,5,4,3,2,1]
sum_1 = 6

count = 0

for i in range(0, len(list_w)):
	for j in range((i+1), len(list_w)):
		if list_w[i] + list_w[j] == sum_1:
			count += 1
print(count)







