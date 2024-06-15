# Check Prime Number

num = 2
for i in range(1, num):
    if num % i == 0:
        print("Its not Prime" )
        break
else: 
    print("Its prime")