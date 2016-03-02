import random
import datetime

lst = [] 

for count in range(0,100):
	item = random.randint(0, 10000)
	lst.append(item)
print lst

# lst = [8, 3, 4, 2, 5]
for count1 in range (0, len(lst)):
	for count2 in range(0, len(lst)-1):
		if lst[count2] > lst[count2+1]:
			temp = lst[count2]          
			lst[count2] = lst[count2+1]      
			lst[count2+1] = temp
print lst	
print "seconds: ", datetime.timedelta(seconds=1)  

# count1 = 0, <5

# count1 = 0
# 	count2 = 0:
# 	temp = 8
# 	lst[0] = 3
# 	lst[1] = 8, lst=[3, 8, 4, 2, 5]

# 	count2 = 1:
# 	temp = 8
# 	lst[1] = 4
# 	lst[2] = 8, lst=[3, 4, 8, 2, 5]

# 	count2 = 2:
# 	temp = 8
# 	lst[2] = 2
# 	lst[3] = 8, lst=[3, 4, 2, 8, 5]

# 	count2 = 3:
# 	temp = 8
# 	lst[3] = 5
# 	lst[4] = 8, lst=[3, 4, 2, 5, 8]