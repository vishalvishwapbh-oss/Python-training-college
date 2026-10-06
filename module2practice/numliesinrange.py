num = int(input("Enter a number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low <= num <= high:
    print("Number lies within the range")
else:
    print("Number is outside the range")
