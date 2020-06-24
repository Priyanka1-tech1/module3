n=int(input('enter range'))
i=0
fv=0
sv=1
while(i<n):
	      if(i<=1):
	      	ne=i
	      else:
	      	ne=fv+sv
	      	fv=sv
	      	sv=ne
	      print(ne)
	      i=i+1
	      

