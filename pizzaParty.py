friends = 8
cost = 12
slices_per_pizza = 6
slices_per_person = 3

pizza_slices = friends * slices_per_person
total_pizza = int(pizza_slices / slices_per_pizza)
total_cost = total_pizza * cost

print(f'You need to buy {total_pizza} pizzas for ${total_cost}')