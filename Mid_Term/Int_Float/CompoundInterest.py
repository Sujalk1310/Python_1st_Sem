P = float(input("Enter Principle Amount : "))
R = float(input("Enter Rate of Interest : "))
T = float(input("Enter Tenure : "))
CI = P*((1+(R/100))**T)
Tot = CI+P
print ("Compund Ineterest :",CI)
print ("Total Amount :",Tot)
