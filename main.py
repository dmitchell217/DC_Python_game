'''
This script will run the whole game. This is where I put my menu code. 

QUESTION TO ANSWER: how to work main game loop.
Thinking I while loop for x days.
If you water trees, harvest fruit, hunt woodchucks, or go to the store, the day automatically ends afterwards
'''
import random
# from TicTacToe import display_board
# from TicTacToe import run_game
# from TicTacToe import winner
import math
from garden import Garden
# from run_time import run_time

def run_main(days):
    count = 0
    garden = Garden()
    print('Objective of the game is to have the most money at the end of the game as possible. Or to have fun. Idk. you pick.\n')
    print("Congratulations, you just purchased your own garden in DC city, walk through the menu to start your adventure\n")
    while count < days:
        while True:
            choice = int(input("Choices:\n 1.: View Garden info \n 2.: End the day \n3.: Visualize Garden \n4.: Water trees \n5.: Harvest Fruit \n6.: Go to the store \n7.: Check water levels \n8.: Catch woodchucks \n9.: play tic tac toe\n"))
            if choice == 1:
                print(garden.info())
                # garden.peak()
            if choice == 2:
                run_day(garden)
                count+=1
            if choice == 3:
                garden.display_garden()
            if choice == 4:
                for tree in garden.in_garden['trees'].values():
                    tree.grow()
                print("Wish those trees could water themselves. Time to rest")
                run_day(garden)
                count+=1
            if choice == 5:
                count = 0
                for tree in garden.in_garden['trees'].values():
                    if tree.harvest():
                        count+=1
                        garden.fruit+=1
                print(f" You gathered {count} fruit. Time to rest")
                run_day(garden)
                count+=1
            if choice == 6:
                while True:
                    option = int(input("Welcome to the store \n Choose one of the following: \n \
                    1: Buy tree(s) \n \
                    2: Buy gnome(s) \n \
                    3: Buy a gun \n \
                    4: Sell Fruit \n \
                    5: See prices \n \
                    "))
                    if option == 1:
                        trees_tobuy = int(input("How many trees do you want to buy?\n")) 
                        garden.buy_trees(trees_tobuy)
                        break
                    if option == 2:
                        gnomes_tobuy = int(input("How many gnomes do you want to buy?\n")) 
                        garden.buy_gnomes(gnomes_tobuy)
                        break
                    if option == 3:
                        garden.buy_gun()
                        break
                    if option == 4:
                        garden.sell_fruit()
                        break
                    if option == 5:
                        print(f" \
                        You have {garden.money} in your wallet \n \
                        Fruit: ${garden.PRICE_fruit} \n \
                        Gnome: ${garden.PRICE_gnomes} \n \
                        Gun: ${garden.PRICE_gun} \n \
                        Tree: ${garden.PRICE_tree} \n \
                        ")
                        continue
                print("Hopefully your day trip to the store was productive, onto a new day \n")
                run_day(garden)
                count+=1
            if choice == 7:
                for tree in garden.in_garden["trees"].values():
                    print(tree.water)
            if choice == 8:
                garden.hunt()
                print("Whew, what a day.\n")
                run_day(garden)
                count+=1
            if choice == 9:
                # play tic tac toe
                # run_game.run_game()
                print("That feauture is coming in the next patch\n")
            if count > days:
                break
    print("Gameover. You finished with the following garden stats...")
    print(garden.info())

# pass in a garden to 
def run_day(garden):

    # this stuff happens at the end of every day, automatically

    # plants wither according to their attributes
    for tree in garden.in_garden["trees"].values():
        tree.run_day()
    print("Your plants withered over night...\n")

    # gnomes have a chance to create rain
    base_rain_chance = random.randint(3,5) # base chance is x-y percent
    rain_multiplier_cap = 10 # multiplier increases with each gnome, caps at this number
    rain_multiplier = min(len(garden.in_garden["gnomes"].keys()), rain_multiplier_cap) * base_rain_chance
    if random.randint(0,100) > (100-rain_multiplier):
        for tree in garden.in_garden["trees"].values():
            tree.grow()
        print("Awesome, the gnomes brought the rain!\n")

    # woodchuck have a chance to spawn
    woodchuck = random.randint(1, 10)
    if woodchuck > 8:
    # add new wood chuck to garden
        garden.add_item("woodchuck")
        print("Ahh chucks, a new woodchuck has nested in your garden!\n")


    # woodchucks have a chance to take out a tree
    base_chuck_chance = random.randint(3,5) # base chance is x-y percent
    chuck_multiplier_cap = 10 # multiplier increases with each woodchuck, caps at this number
    chuck_multiplier = min(len(garden.in_garden["woodchucks"].keys()), chuck_multiplier_cap) * base_chuck_chance
    if random.randint(0,100) > (100-chuck_multiplier):
        # random choice from trees.values()
        unlucky_tree = random.choice(list(garden.in_garden['trees'].values()))
        # grab and remove
        print("The Woodchucks chucked down a tree!\n")
        garden.remove_item(unlucky_tree.id)

    # Other random events

    # Woodpecker migration
    migration_chance = random.randint(5,10) # base chance is 5-10 percent
    if random.randint(0,100) > (100-migration_chance):
        garden.add_item('woodchuck')
        garden.add_item('woodchuck')
        garden.add_item('woodchuck')
        print("O no! A flock of woodchucks have moved into the garden!\n")

    # Locusts (Lose one fruit)
    locusts_chance = random.randint(5,10) # base chance is 5-10 percent
    if random.randint(0,100) > (100-locusts_chance):
        if garden.fruit > 0:
            garden.fruit -=1
            print("Locust attack. They made off with one piece of fruit... pesky things\n")
        else:
            print("Locusts swarm... good thing you didn't have any fruit to eat\n")

    # Thieves (Lose half your money)
    thief_chance = random.randint(5,10) # base chance is 5-10 percent
    if random.randint(0,100) > (100-thief_chance):
        garden.money = math.floor(0.5*garden.money)
        print("O no! Thieves have ransacked your storage and half your money!\n")
run_main(15)
    

# print("Choices:\n 1.: Do nothing \n 2.: Wait one day \n3.: Wait multiple days \n4.: View your farm \n5.: Sell Fruit \n6.: Buy Gnomes \n7.: Catch woodchucks \n8.: play tic tac toe")