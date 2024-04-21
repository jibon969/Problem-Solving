

<img src="image/how-to-approach-a-coding-problem.png" id='header'>

<h1 align="center">Problem Solving</h1>

<div align="center">
<!-- Gmail Account -->
<a href="mailto:jayed.swe@gmail.com">
<img src='https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="tel:+8801987132107">
<img
src='https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white'
alt='Jayed Hossain Jibon'
/>
<a href="#" target="_blank">
<img
src='https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://www.facebook.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white'
alt='Jayed Hossain Jibon'
/>

<a href="https://www.linkedin.com/in/jibon969/" target="_blank">
<img
src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
<a href="https://github.com/jibon969" target="_blank">
<img
src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'
alt='Jayed Hossain Jibon'
/>
</a>
</div>

<hr/>
<div align="center">
        <a href="https://www.programiz.com/python-programming/examples" target="_blank">Programiz
        </a>
        |
        <a href="https://pynative.com/python-basic-exercise-for-beginners/" target="_blank">PYnative</a>
        |
        <a href="https://www.geeksforgeeks.org/python-programming-examples/" target="_blank">Geeksforgeeks</a>
        |
        <a href="https://www.w3resource.com/python-exercises/" target="_blank">w3resource</a>
        |
        <a href="https://www.hackerrank.com/" target="_blank">HackerRank</a>
        |
        <a href="https://leetcode.com/" target="_blank">LeetCode</a>
</div>
<hr/>

##### 01. Add Two Numbers

```
Input: num1 = 5, num2 = 10
Output: 15
Explanation: 5 + 10 = 15

Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```

<details>
<summary style="cursor:pointer">Solution</summary>

```py
num1 = 5;
num2 = 10;
sum = num1 + num2;
print(sum) // Output: 15
```
</details>

#### 02. Find Maximum of two numbers in Python

```
Input: num1 = 5, num2 = 10
Output: 10
Explanation: 5, 10 ---> Here 10 is maximum
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
num1 = 5
num2 = 10
if num1 >= num2:
    print(f"{num1} Maximum")
else:
    print(f"{num2} Maximum")
```
</details>

#### 03. Find the Factorial of a Number

```
Input  : 5
Output : 120
Explanation: 5! = 5*4*3*2*1
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
def factorial_number(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        return f
result = factorial_number(5)
print(result)
```
</details>

#### 04. Simple Interest

```
Input : P = 10000
        R = 5
        T = 5
Output :2500.0
Explanation:
P	=	initial principal balance
r	=	annual interest rate
t	=	time (in years)
Formula : SI = (P × R ×T) / 100
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
principal_balance = 10000
interest_rate = 5
time = 5
simple_interest = principal_balance*interest_rate*time/100
print(simple_interest)
```
</details>

#### 05. Compound Interest

```
Input: Principal (amount): 1200 Time: 2 Rate: 5.4
Output : 1330.9920000000002
Explanation:
Formula:
Amount= P(1 + R/100)t
Compound Interest = Amount – P
Where, 
P is principal amount 
R is the rate and 
T is the time span
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
def compound_interest(principal, rate, time):
    # Formula = P(1 + R/100)t
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    print("Compound interest is : ", ci)
compound_interest(12000, 5.4, 2)
```
</details>

#### 06. Armstrong Number

```
Input  : 
Output : 
Explanation:
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
```
</details>

#### 07. Find area of a circle

```
Input: 5
Output : 78.55
Formula: Area = pi * r2
where r is radius of circle
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
def find_area_circle(area):
        pi = 3.142
        return pi * (area*area);
result = find_area_circle(5)
print(result)
```
</details>

#### 08. Prime numbers in an Interval

```
Input: 
start_number = 1
end_number = 10
Output : 1, 2, 3, 5, 7
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
start_num = int(input("Enter start number : "))
end_num = int(input("Enter end number : "))

for num in range(start_num, end_num+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("Prime number : ", num)
```
</details>


#### 09. check whether a number is Prime or not

```
Input: 7
Output : Prime Number
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
is_prime = int(input("Enter your number : "))

if is_prime % 2 == 0:
    print("Not Prime number")
else:
    print("Prime Number ")
```
</details>

#### 10. Fibonacci Number

```
Input  : 5
Output : 0 1 1 2 3
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
def fibonacci_number(n):
        a = 0
        b = 1
        print(a)
        print(b)

        for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)

fibonacci_number(int(input("Enter your number : ")))
```
</details>

#### 11. Check Fibonacci Number

```
Input  : 10
Output : 
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
def isFibonacci(num):
        fib1 = 0
        fib2 = 1
        sum =  fib1 + fib2

        while (sum <= num):
                if num == sum:
                        return True
        return False

output = isFibonacci(10)
print(output)
```
</details>


#### 12. ASCII Value of a character

```
Input  : A
Output : 65
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
ascii_value = input("Enter your ascii : ")
output = ord(ascii_value)
print(output)
```
</details>

#### 13. Sum of squares of first n natural numbers

```
Input  : 5
Output : 55
Explanation: 5 = 1**2 + 2**2 + 3**2 + 4**2+ 5**2
               = 1 + 4 + 9 + 16 + 25
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
number = int(input("Enter your number : "))
def sum_of_square(n):
        sum = 0
        for i in range(1, n+1):
                sum = sum + i * i
        return sum
output = sum_of_square(number)
print("Sum of squares : ", output)
```
</details>

#### 14. Cube sum of first n natural numbers

```
Input :  3
Output: 784
Explanation: 
Complexity Analysis
    Time Complexity: O(1)
    Auxiliary Space: O(1)
    
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
number = int(input("Enter your number : "))
def sum_of_square(n):
        sum = 0
        for i in range(1, n+1):
                sum = sum + i * i
        return sum
output = sum_of_square(number)
print("Sum of squares : ", output)
```
</details>



## Array

#### 01. Find sum of array

```
Input  : 1, 2, 3, 4, 10
Output : 20
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
num = [1, 2, 3, 4, 10]
sum = 0
for i in num:
        sum = sum + i
print(sum)
```
</details>

#### 02. Find largest element in an array

```
Input  : [1, 2, 3, 4, 10, 5]
Output : 10
```
<details>
<summary style="cursor:pointer">Solution</summary>

```py
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
```
</details>






---
**[⬆ Back to Top](#header)**
