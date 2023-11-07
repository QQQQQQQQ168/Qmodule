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
  
  # 初始化描述汽车的属性 make, model, year，odometer_reading的属性，其初始值总是为0。
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  # 返回整洁的描述性信息
  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def show_info(self):
    long_name = f"{self.year} {self.make.title()} {self.model.title()}"
    print(long_name)

  # 打印一条指出汽车里程的消息
  def read_odometer(self):
    msg_odometer = f"This car has {self.odometer_reading} miles on it."
    print(msg_odometer)

 # 将里程表读数设置为指定的值，禁止将里程表读数往回调
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You CANNOT roll back an odometer!")
