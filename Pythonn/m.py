a=ord("A")
for i in range(6,1,-1):
    for j in range (1,i-1):
        print(chr(a),end=" ")
        a=a+1
print()