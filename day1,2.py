Name = input("Please enter your name:")
print("Hello there!",Name)
Balance  = input(f"{Name},  please  enter your account balance:")
if  float(Balance) >= 5000:
    print("Access Granted welcome! to Premium Founder Dashboard",Name)
else:
    print("Access denied please deposit more fund in your account and try again",Name)
