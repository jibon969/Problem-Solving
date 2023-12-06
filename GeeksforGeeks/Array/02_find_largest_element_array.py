# Find largest element in an array

def large_element(arr, n):
        max = arr[0]
        for i in range(1, n):
                if arr[i] > max:
                        max = arr[i]
        return max

arr = [10, 20, 30]
n = len(arr)
output = large_element(arr, n)
print(output)