# Discount Calculator

amt = float(input("Enter purchase amount: "))

if amt >= 1000:
    disc = amt * 0.10   # 10% discount
else:
    disc = amt * 0.05   # 5% discount

payable = amt - disc

print("Purchase Amount =", amt)
print("Discount =", disc)
print("Final Payable =", payable)
