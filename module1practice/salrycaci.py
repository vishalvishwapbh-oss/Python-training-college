basic = float(input("Enter basic salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100

gross_salary = basic + hra + da

print("Basic Salary =", basic)
print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross_salary)