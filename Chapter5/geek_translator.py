# Geek Translator 
# Dmonstrates using dictionaries

geek = {"404": "clueless. From the web error message 404, meaining page not found",
        "Googlin": "searching the Internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in acomputer keyboards.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "The act of striking an elctronic device to make\
            it work.",
        "Uninstalled" : "being fired. Especially popular during the dot-bomb era."}
        
        
choice = None
while choice != "0":
    print(
        """
           Geek Translator
           
           0 - Quit 
           1 - Look Up a Geek Term
           2 - Add a Geek Term
           3 - Redefine a Geek Term 
           4 - Delete a Geek Term
        """
    )
    
    choice = input("Choice: ")
    print()
    
    #exit
    if choice == "0":
        print("Good bye")
        
    # get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know:, ", term)
        
    # add a term-definition pair
    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("\nWhat's the difinition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term alread exists!  Try redefining it.")