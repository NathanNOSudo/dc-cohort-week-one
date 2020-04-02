train_mass = 22680
train_acceleration = 10
train_distance = 100

# bomb_mass = 1
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(22680, 10)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")
# def f_to_c(f_temp):
#   c_temp = (f_temp - 32) * 5/9
#   return c_temp

# print(f_to_c(75))


# def f_to_c(f_temp):
#   c_temp = (f_temp - 32) * 5/9
#   return c_temp
# f100_in_celsius =(100 - 32) * 5/9
  
# print(f100_in_celsius)