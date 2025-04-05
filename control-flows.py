def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

#  final price
final_price = calculate_discount(original_price, discount)

#  result
if final_price == original_price:
    print(f"No discount applied. The original price is: {final_price}")
else:
    print(f"Final price after discount: {final_price}")
