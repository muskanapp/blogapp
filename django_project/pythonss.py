#.list_ = [0,1]
for i in range(5):
	list_.append(list_[-1] + list_[-2])
print(list_)

#list_m = [15,85,35,89,125]
max_num = list_m[0] 
for i in list_m:
	if max_num > i:
		max_num = i
print(max_num)

#list_s = [2,5,2,7,8]
a = len(list_s)
print(list_s[int(a/2)])

list_1 = [1,2,3]
list_2 = [4,5,6]
result = []
for i in range(0, len(list_1)):
	result.append(list_1[i] + list_2[i])
print(result)

str_1 = "kayak".lower()
str_2 = "Kayak".lower()
if str_1 == str_2[::-1]:
inp = "helloSJIDS"
count_u = 0
count_l = 0
for i in inp:
	if  i.isupper():
		count_u += 1
	else:
		count_l += 1


	







	