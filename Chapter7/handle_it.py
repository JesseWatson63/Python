# Handle it 
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")
# Specify exception type    
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
    
# Handle multiple exceptions
print()
for value in (None, "Hi!"):
    try:
        print("\nAttempting to convert", value, "-->", end=" ")
    except(TypeError, ValueError):
        print("Something went wrong.")
        
# get an exceptions argument
try:
    num = float(input("\nEnter a number:"))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)
    
# try/except/else:
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
    
input("\n\nPress the enter key to exit")