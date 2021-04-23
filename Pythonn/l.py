a= ord("A")
for i in range (4):
    for j in range(i+1):
        print(chr(a), end=" ")
    a=a+1
    print()