a=input("enter the name : ")
b=int(input("enter the Monthly income : ₹"))
c=int(input("enter your monthly Room rent : ₹"))
d=int(input("Enter your food expense : ₹"))
e=int(input("enter your monthly Travel Expense : ₹"))
f=int(input("enter your monthly Entertainment Expense : ₹"))
g=int(input("enter your other Expense : ₹"))
print("======MONTHLY EXPENSE REPORT=====")
h=(c+d+e+f+g)
print(f"the total monthly Expense : ₹ {h}")
i=b-h # b= monthly income and h= total expense
print(f"The total remaining Money : ₹{i}")
j=(i/b)*100
print(f"the total saving percentage : {j:.2f}%")
k=h/30
print(f"the daily average : {k:.2f}")

