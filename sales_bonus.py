"""
Practical 1
exercise create sales bonus structure
"""

sales = float(input("Enter the sales :"))
if sales < 1000:
    sales = sales * 0.1
else:
    sales <= 1000
    sales = sales * 0.15
print(sales)