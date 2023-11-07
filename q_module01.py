def make_pizza(size, *toppings):
  msg = "\n" + f"Making a {size} inch pizza with the following toppings: "
  print(msg)
  for topping in toppings:
    print(f"- {topping}")



def print_models(unprinted_designs, completed_models):
  """
  模拟打印每个设计，直到没有未打印的设计为止
  打印每个设计后，都将其移到列表completed_models中
  """
  original_unprinted_designs = f"The Original Unprinted Designs = {unprinted_designs}"
  original_unprinted_designs += "\n" + "Printing..."
  print(original_unprinted_designs)

  while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print(f"Printing model: {current_design}")

    # 打印每个设计后，都将其移到列表completed_models中
    completed_models.append(current_design)



def show_completed_models(completed_models):
  msg = "\n" + f"The following models have been printed: "
  print(msg)
  for completed_model in completed_models:
    print(completed_model.title())


class Dog():

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce_dog(self):
    msg_name = f"My dog's name is {self.name}." 
    msg_age = f"My dog is {self.age} years old." + "\n"
    print(msg_name)
    print(msg_age)

  def sit(self):
    msg_sit = self.name.title() + f" is now sitting."
    print(msg_sit)

  def roll_over(self):
    msg_roll = self.name.title() + f" rolled over!"
    print(msg_roll)
