price = float(input("Enter price: "))

if price > 1000:
    discount = 20
elif price > 500:
    discount = 10
else:
    discount = 5

final = price - (price * discount / 100)

print("Discount Applied =", discount, "%")
print("Final Bill =", final)