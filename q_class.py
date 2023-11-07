class Dog():

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce_dog(self):
    msg_name = f"My dog's name is {self.name.title()}."
    msg_age = f"My dog is {self.age} years old."
    print(msg_name)
    print(msg_age)

  def sit(self):
    msg_sit = f"{self.name.title()} is now sitting."
    print(msg_sit)

  def roll_over(self):
    msg_roll = f"{self.name.title()} rolled over!"
    print(msg_roll)

##########

class Car():

  # 初始化描述汽车的属性
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  # 返回整洁的描述性信息
  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
