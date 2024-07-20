# A	
# B	A
# C	B	A
# D	C	B	A


for i in range(4):
    a=65
    for j in range(i+1):
        print(chr(a-j),end='\t')
        
    print()    
    a+=1