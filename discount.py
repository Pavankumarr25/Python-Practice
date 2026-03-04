price = float(input("Enter price: "))
discount_percent = float(input("Enter percentage: "))

discount = (price * discount_percent) / 100
final_price = (price-discount)
print("Final price after discount: ", final_price)