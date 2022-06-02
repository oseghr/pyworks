
#Tip Calculator Application

# Display name of our application
print("Welcome to the Tip Calculator")

# Get user to input bill amount
bill_amount = float(input("What was the total bill? $"))

# Get the user tip percentage option from 10%, 12% or 15%
tip_rate = int(input("What percentage tip would you like to give? 10, 12, 15? "))


# Calculate the tip amount
tip_amount = (tip_rate/100) * bill_amount
#Calculate the total bill (tip included)
total_bill = bill_amount + tip_amount

# Get the number of people split the bill
number_split = int(input("How many people to split the bill? "))

#Calculate the bill split by number of people sharing
split_amount = round(total_bill / number_split, 2)

# Display each person's bill
print(f"Each person should pay: ${split_amount:.2f}")