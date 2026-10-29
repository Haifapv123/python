def simple_interest(p, t, senior):
    if senior == "yes":
        r = 12
    else:
        r = 10

    si = (p * r * t) / 100
    return si


p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
senior = input("Is the customer a senior citizen (yes/no): ")

interest = simple_interest(p, t, senior.lower())
print("Simple interest =", interest)
