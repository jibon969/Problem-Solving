# Prime numbers in an Interval

start_num = int(input("Enter start number : "))
end_num = int(input("Enter end number : "))

for num in range(start_num, end_num+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("Prime number : ", num)
            