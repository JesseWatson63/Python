# Simple Game
# Demonstrates importing modules

import games, random

print("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
num = games.ask_number(question = "How many payers? (2 - 5: ", low = 2, high = 5)

for i in range(num):
    name = input("Player name: ")