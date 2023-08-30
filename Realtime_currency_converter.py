from forex_python.converter import CurrencyRates # initialize the library

# create an instance
c = CurrencyRates()

# Prompt an amout as a user requirement
amount = int(input("Enter the amount: "))

# whose currency to convert
from_currency = input("From Currency: ").upper()

# you want to convert in which currency form
to_currency = input("To Currency: ").upper()

# Display the which currency to change in which form
print(from_currency,amount,"To", to_currency)
try:
  result = c.convert(from_currency,to_currency,amount)
  print(result)
except Exception as e:
  print("An error occurred:",e)  
