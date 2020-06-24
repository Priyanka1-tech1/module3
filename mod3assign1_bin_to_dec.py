n= list(input(" binary num"))
v=0
for i in range(len(n)):
	d =n.pop()
	if d== '1':
		v= v+ pow(2, i)
print('decimal num',v)