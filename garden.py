import random
from hashing import hash_code
from woodchuck import Woodchuck
from gnome import Gnome
from tree import Tree

fruit_tree_emoji = '＄'
new_tree_emoji = '✿'
gnome_emoji = '✭'
woodchuck_emoji = '✖'
typeconvert = {"tree":Tree, "woodchuck":Woodchuck, "gnome":Gnome}
black_dot = '•'

class Garden():
    # think about adding fruit and money to the garden object so I can keep track more easily
    def __init__(self, fruit=0, money=40):
        # self.trees = trees
        # self.gnomes = gnomes
        # self.woodchucks = woodchucks
        # trees = {}
        # gnomes = {}
        # woodchucks = {}
        # dictionary of dictionaries. Id (hashes) are the keys of the nested dictionary
        self.in_garden = {"trees":{}, "gnomes":{}, "woodchucks":{}}
        # self.display = [None,None,None,None,None,None,None,None,None]
        self.TREECAP = 9
        self.display = []
        [self.display.append(None) for x in range (0, self.TREECAP)]
        self.fruit = fruit
        self.money = money
        self.trees_len = len(self.in_garden["trees"].keys())
        self.gnomes_len = len(self.in_garden["gnomes"].keys())
        self.woodchucks_len = len(self.in_garden["woodchucks"].keys())
        self.PRICE_fruit = 10 # static variable for price of fruit
        self.PRICE_gnomes = 20 # static variable for price of gnomes
        self.PRICE_gun = 30 # static variable for price of gun
        self.PRICE_tree = 10 # static variable for price of tree
        self.gun = False # boolean for gun
    def info(self):
        return (f"Your garden has the following items in it: \n {self.trees_len} trees, \n {self.gnomes_len} gnomes, \n and {self.woodchucks_len} woodchucks \n  You have {self.fruit} fruit and ${self.money} under your mattress\n")
    

    def add_item(self, itemtype):
        # if the item is a tree...
        if itemtype == 'tree':
            # go through store process
            if self.money < self.PRICE_tree:
                    print(f"You don't have enough money, come back later\n")
                    return
            else:
                self.money -= self.PRICE_tree
            # make a new tree
            newTree = Tree()
            # loop through display and find the first available plot
            for x in range(0,self.TREECAP):
                # if empty plot, stick it there
                if self.display[x] == None:
                    self.display[x] = newTree
                    # Finally put new tree in the in_garden dictionary
                    self.in_garden['trees'][newTree.id] = newTree
                    return print("You just added a new tree")
            return (f"Your Garden's capacity is {self.TREECAP}, you have the max number of trees")
        elif itemtype == 'gnome':
            # make a new gnome
            newGnome = Gnome()
            self.in_garden['gnomes'][newGnome.id] = newGnome
        elif itemtype == 'woodchuck':
            # make a new woodchuck
            newWoodchuck = Woodchuck()
            self.in_garden['woodchucks'][newWoodchuck.id] = newWoodchuck
        # else:
        #     pass
            # gnome or woodchuck
            # access "in_garden" dict, use hash_code for a unique id, setting that equal to its class type
            # self.in_garden[itemtype+"s"][hash_code(itemtype)]=typeconvert[itemtype]() # will this code error out because it doesn't pass in variable parameters? solution = all default params
    
    def remove_item(self, id):
        # grab the type
        itemtype = str(id).split("_")[1]
        # delete key (id) from the corresponding dictionary in self.in_garden
        try:
            removed_element = self.in_garden[itemtype].pop(id, None)
            if itemtype == 'tree':
                # find tree using id search, the set self.display[index] 
                for x in range(0, self.TREECAP):
                    # if i find tree id in display list
                    if self.display[x].id == id:
                        self.display[x] = None
        # catch error key not found
        except:
            return print("Key not found\n")
        return removed_element

    def peak(self, itemtype=0):
        # TO DO: FIX THIS FUNCTION
        if itemtype == 0:
            for key, value in self.in_garden.items():
                print(f"\n {key} :" , {value}) 
        else:
            print(f"\n {itemtype} in garden: {self.in_garden[str(itemtype)]}\n")
    
    def sell_fruit(self, fruit_tosell):
        # sells x fruit at a static price
        if self.fruit < fruit_tosell:
            return print("You don't have enough fruit, come back later\n")
        else:
            self.money += fruit_tosell*self.PRICE_fruit
            self.fruit -= fruit_tosell
            return print(f"You sold {fruit_tosell} for {fruit_tosell*self.PRICE_fruit}\n")

    def buy_gnomes(self, gnomes_tobuy):
        # buy x gnomes at a static price
        count = 0
        while count < gnomes_tobuy:
            while True:
                if self.money < self.PRICE_gnomes:
                    print(f"You don't have enough money, you bought {count} gnomes before running out of cash\n")
                    return
                else:
                    self.money -= self.PRICE_gnomes
                    self.add_item("gnome")
                    count+=1
        return print(f"You bought {count} gnomes for ${count*self.PRICE_gnomes}")
    
    def buy_gun(self):
        if self.gun == True:
            return print("You already have your fire barrel, go out and hunt those pesky chucks!\n")
        else:  
            if self.money > self.PRICE_gun:
                self.gun = True # set gun possession to true
                self.money -= self.PRICE_gun # update money
                return print("Congrats, you now have a gun. You can now hunt woodchucks\n")
            else:
                return print("You don't have enough money to buy a gun yet, sell a bit more fruit first.\n")
    def hunt(self):
        guess = int(input("Pick a number between 0 and 8\n"))
        # determine if the garden has a gun
        if self.gun == False:
            return print("You need to buy a gun before you can hunt woodchucks")
        positions = {}
        # display the garden
        self.display_garden()
        # for woodchuck in woodchucks, randomly assign them to x positions
        for woodchuck in self.in_garden['woodchucks'].values():
            positions[woodchuck.id] = random.choice(range(0, self.TREECAP))
        # all woodchucks in guesed position are removed from the garden
        for chuck_id, position in positions.items():
            if position == guess:
                self.remove_item(chuck_id)
                print("Ya got one!\n")
        # display the garden
        self.display_garden()
        

    def display_garden(self):
        # trees / plants visual 3 by 3 for now
        dis = []
        for x in self.display:
            if x == None:
                dis.append(black_dot)
            else:
                dis.append(x.e())
        
        print(f' {dis[0]} | {dis[1]} | {dis[2]} \n___________\n {dis[3]} | {dis[4]} | {dis[5]} \
         \n ___________\n {dis[6]} | {dis[7]} | {dis[8]}')

        # gnomes visual (line)
        print('\n')
        [print(gnome_emoji + " | ") for x in range(0, self.gnomes_len)]
            

        # woodchucks visual (line)
        print('\n')
        [print(woodchuck_emoji + " | ") for x in range(0, self.woodchucks_len)]
# garden = Garden()
# print(garden.display_garden())


    
    





