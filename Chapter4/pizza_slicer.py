# Pizza Slicer
# Demonstrates string slicing

word = "pizza"

print(
    """
        Slicing 'Cheat sheet'
        
        0   1   2   3   4   5
        +---+---+---+---+---+
        | P | I | Z | Z | A |
        +---+---+---+---+---+
       -5  -4  -3  -2  -1  
    """
)

print("Enter the beginning and ending index for you slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")
start = None
while start != "":
    start = (input("\nStart: "))
    
    if start:
        start = int(start)
        
        finish = int(input("Finish: "))
        
        print("word[", start, " : ", finish, "] is", end=" ")
        print(word[start:finish])
        
input("\n\nPress enter to exit")