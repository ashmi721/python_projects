# import periodictable abstract chemical elements
import periodictable
# enter user input of the atomic number of the element
Atomic_No = int(input("Enter element atomic No: "))

# use atomic number to retrieve details about the element from priodictable library
element = periodictable.elements[Atomic_No]
# display the various information of the element
print('Element Name:',element.name)
print('Atomic Number:',element.number)
print('Symbol:',element.symbol)
print('Atomic Mass:',element.mass)
print('Density:',element.density)
