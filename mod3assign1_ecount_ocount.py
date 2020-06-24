l1 = [10, 21, 4, 45, 66, 93, 1] 
ecount, ocount = 0, 0
for n in l1: 
    if n% 2 == 0: 
        ecount += 1
    else: 
        ocount += 1
print("Even count", ecount) 
print("Odd count", ocount) 
