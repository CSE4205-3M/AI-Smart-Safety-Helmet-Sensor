from collections import deque

d = deque()

i = 0
while True:
	i+=1
	if len(d) != 10:
		d.append(i)
	else:
		print(d[0])
		d.popleft()
		d.append(i)
		break
    
    
