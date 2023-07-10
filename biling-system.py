#1. wap to create a biling system (product,price,aulity,total,all_total)
def clc_billing_system():
    name = input("Enter your name: ")
    print(f"Welcome Mr/Mrs {name}")

    all_total = 0
    try:
        product_num = int(input("Enter the number of products: "))
        for i in range(product_num):
            product = input("Enter the product name: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            total = price * quantity
            print(f"You bought {quantity} {product}(s) at {price} each. Total: {total}")
            all_total += total

        print(f"Your total bill is: {all_total}")
    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")

clc_billing_system()
