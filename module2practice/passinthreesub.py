m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4=(m1+m2+m3)*100/300
if(m4>40):
    print("pass in exam")
else:
    print("fail")