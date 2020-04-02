def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500: 
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!")


def grade_converter(gpa):
  grade = "F"
  
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"
    
  return grade

def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and not ec_count >= 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

def gs_price(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost
print("$" + str(gs_price(8.4)))

def ds_price(weight):
  if weight <= 2:
    cost = weight * 4.50
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost
print("$" + str(ds_price(1.5)))

def gs_price(weight):
  pgs = 125
  if weight <= 2:
    cost = weight * 1.50 + 20
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost
print("$" + str(gs_price(1.5)))

def ds_price(weight):
  if weight <= 2:
    cost = weight * 4.50
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost
print("$" + str(ds_price(1.5)))

gs = gs_price(weight)
ds = ds_price(weight)
def cheapest(weight):
  if gs <= ds:
    print("Ground shipping is the cheapest. The cost is $" + str(cheapest(weight)))
  else:
    print("Drone shipping is the cheapes. The cost is $" + str(cheapest)))


