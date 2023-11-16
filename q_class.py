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

  # 汽车有油箱
  def fill_gas_tank(self):
    msg = f"This car has a gas tank."
    print(msg)



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
    long_name = f"{self.year} {self.make} {self.model}"
    print(long_name.title())

  # 打印一条指出汽车里程的消息
  def read_odometer(self):
    msg_odometer = f"This car has {self.odometer_reading} kilometers on it."
    print(msg_odometer)

 # 将里程表读数设置为指定的值，禁止将里程表读数往回调
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You CANNOT roll back an odometer!")

 # 将里程表读数增加指定的量
  def increment_odometer(self, km):
    self.odometer_reading = self.odometer_reading + km


##########


class Battery():
  def __init__(self, battery_size=70):
    self.battery_size = battery_size
      
  def show_battery(self):
    msg = f"This car has a {self.battery_size} -kWh battery."
    print(msg)

  def get_range(self):
    """
    电瓶的容量为70kWh，它就将续航里程设置为240英里；
    如果容量为85kWh，就将续航里程设置为270英里
    """
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270

    msg = f"This car can go approximately {range}"
    msg += f" miles on a full change."
    print(msg)

##########


class Battery():
  def __init__(self, battery_size=70):
    self.battery_size = battery_size
  
  def show_battery(self):
    msg = f"This car has a {self.battery_size} -kWh battery."
    print(msg)

  def get_range(self):
    """
    电瓶的容量为70kWh，它就将续航里程设置为240英里；
    如果容量为85kWh，就将续航里程设置为270英里
    """
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270

    msg = f"This car can go approximately {range}"
    msg += f" miles on a full change."
    print(msg)
    

##########


class ElectriCar(Car):
  def __init__(self, make, model, year):
    # 初始化父类的属性
    super().__init__(make, model, year)
    # 添加了新属性self.battery_size，并设置其初始值（如70）
    # self.battery_size = 70
    # 们添加了一个名为self.battery的属性
    self.battery = Battery()
    
 # 添加了一个名为describe_battery()的方法，它打印有关电瓶的信息  
 def describe_battery(self):
    msg_battery = f"This car has a {self.battery_size} -kWh battery."
    print(msg_battery)

  # 电动汽车没有油箱
  def fill_gas_tank(self):
    msg = f"This car dosen't need a gas tank!"
    print(msg)

