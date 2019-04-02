#!/usr/local/bin/python

fruit_list = ['Apple', 'Cherry', 'Lime', 'Lemon']
price_list = [0.10, 0.986, 0.5, 0.4]
stock_list = [10, 15, 1, 25]

for i in zip(fruit_list, price_list, stock_list):
    print(i)
  

# for fruit, price, qty in zip(fruit_list, price_list, stock_list):
    # print("{:20s} {:6.2f} {:4d}".format(fruit, price, qty))
    
    # print(f"{fruit:20s} {price:6.2f} {qty:4d}")
    
    # print("{0[0]:20s} {0[1]:6.2f} {0[2]:4d}".format(i))
    
    # print("%-20s %6.2f %4d" % (fruit, price, qty))


# NOTE FROM THE DOCs:
# ==================
# Format strings contain "replacement fields" surrounded by curly braces {}.
# ...If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.
# ...There is a section on the "Format Specification Mini-Language"
