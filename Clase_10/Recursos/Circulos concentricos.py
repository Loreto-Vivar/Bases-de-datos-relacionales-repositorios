size = 7
for i in range(size):
    line = " "
    for j in range(size):
        if i==0 or size -1 or j== size -1:
            line+= "*"
        elif i==1 or i== size -2 or  j== size-2:
            line+= "+"
        else: 
            line += " "
    print(line)