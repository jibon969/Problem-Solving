# Python Program for simple interest
"""
Formula : SI = (P × R ×T) / 100
P	=	initial principal balance
r	=	annual interest rate
t	=	time (in years)
"""

""" 
Input : P = 10000
        R = 5
        T = 5
Output :2500.0
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 units of time.
"""

principal_balance = 10000
interest_rate = 5
time = 5

simple_interest = principal_balance*interest_rate*time/100
print(simple_interest)
