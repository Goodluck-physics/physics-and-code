Name = input("Hello there please enter your name:")
print("hi",Name)
Funding_offer = input(f"{Name},please enter your Funding Offer")
if float(Funding_offer) >= 100000:
    print(f"Excellent choice welcome to the world  of premium buisness {Name},you deposited an amount of ${Funding_offer}.")

elif float(Funding_offer) >=10000 and float(Funding_offer) <=99999:
    print("Good choice", Name)

else:
    print("Insufficient  funding please deposit more  funds", Name)    