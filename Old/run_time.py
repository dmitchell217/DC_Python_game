
import random
from TicTacToe import display_board
from TicTacToe import run_game
from TicTacToe import winner
from garden import Garden
import math
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
    rain_multiplier = math.ceil(garden.gnomes_len, rain_multiplier_cap) * base_rain_chance
    if random.randint(0,100) < (100-rain_multiplier):
        for tree in garden.in_garden["trees"].values():
            tree.grow()
        print("Awesome, the gnomes brought the rain!\n")

    # woodchuck have a chance to spawn
    woodchuck = random.randint(1, 10)
    if woodchuck > 90:
    # add new wood chuck to garden
        garden.add_item("woodchuck")
        print("Ahh chucks, a new woodchuck has nested in your garden!\n")


    # woodchucks have a chance to take out a tree
    base_chuck_chance = random.randint(3,5) # base chance is x-y percent
    chuck_multiplier_cap = 10 # multiplier increases with each woodchuck, caps at this number
    chuck_multiplier = math.ceil(garden.woodchucks_len, chuck_multiplier_cap) * base_chuck_chance
    if random.randint(0,100) < (100-chuck_multiplier):
        # random choice from trees.values()
        unlucky_tree = random.choice(list(garden.in_garden['trees'].values()))
        # grab and remove
        garden.remove_tree(unlucky_tree.id)

    # Other random events

    # Woodpecker migration
    base_chance = random.randint(5,10) # base chance is 5-10 percent
    multiplier_cap = 3 # multiplier increases with each woodchuck, caps at 3
    multiplier = math.ceil(garden.woodchucks_len, chuck_multiplier_cap) * base_chuck_chance
    if random.randint(0,100) < (100-multiplier):
        pass
        # garden.add_woodchuck()
        # garden.add_Woodchuck()
        # garden.add_woodchuck()

    # Locusts (Lose one fruit)
    base_chance = random.randint(5,10) # base chance is 5-10 percent
    multiplier_cap = 3 # multiplier increases with each woodchuck, caps at 3
    multiplier = math.ceil(garden.woodchucks_len, multiplier_cap) * base_chance
    if random.randint(0,100) < (100-chuck_multiplier):
        pass
        # if garden.fruit > 0:
        #     garden.fruit -=1



    # # Farm bullies (Challenged to a game of Tic Tac Toe, if you lose the game, they take your farm and the game quits)
    # # figure out how to call function without error
    # result = run_game.run_game()
    # if result == False:
    #     exit_game = True
    #     # exit the entire program. 
    # if result == True:
    #     pass
    #     # all good, just send a print message and move on

# def run_time(days, garden):
#     elapsed = 0
#     while elapsed < days:
#         run_day(garden)
#         elapsed +=1

