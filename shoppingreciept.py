notebooks = 3
notebook_price = 2.50
pens = 5
pen_price = 1.20
total = (notebooks * notebook_price) + (pens * pen_price)
tax = total * 1.08
print(f'Your total today is ${round(tax,2)}')