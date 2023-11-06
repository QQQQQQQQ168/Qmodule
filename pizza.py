def make_pizza(size, *toppings):
  msg = "\n" + f"Making a {size} inch pizza with the following toppings: "
  print(msg)
  for topping in toppings:
    print(f"- {topping}")
