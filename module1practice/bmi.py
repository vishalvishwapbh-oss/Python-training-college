w=float(input("enter the weight in kg"))
feet=float(input("enter the height in feet"))
inches=float(input("enter the height in feet"))
h=(feet*12+inches)*0.0254
bmi=w/h**2
print("the body mass index is " ,bmi)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")
