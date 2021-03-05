#OOP Desing Challenge
#Created four classes : trainer, pokemon, hospital,
#created attributes and methods for said classes
#attribute: property of a class 
#methods: modify attributes


class trainer:
    # #attribute
    # name 
    # level
    # #methods
    # greeting
    # pokedex
    # #prop

    #Initialize attributes for the trainer class
    def __init__(self, name):
        self.name = name
        self.pokedex = [] 

    #Prints greeting with trainer name
    def greeting(self):
        print("Hello, my name is " + self.name + "!")

    #Appends a pokemon's name to the self.poke list
    def add_pokemon(self, pokemon):
        self.pokedex.append(pokemon) 
#Instantiate object stanley of the trainer class
stanley = trainer("stanley")
#Method greeting for trainer class called for stanley object
stanley.greeting()
# print(stanley.pokedex)


class pokemon:
#     # #attribute
#     # name 
#     # level
#     # hp 
#     # #methods
#     # name 
#     # heal
#     # #prop
    #Initialize attributes for the pokemon class
    #Initially set hp to 1000 and level to 5
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.level = 5
        self.moves = []
    
    #Prints pokemon name three times
    def greeting(self):
        print(((self.name + '! ') * 3))

    #Appends a move to the self.moves list
    def add_move(self, move):
        self.moves.append(move) 

    def attack(self, move_index):
        print(self.name + " used " + self.moves[move_index].use_move())


class hospital:
#     #attribute
#     city
#     #method
#     changeName
#     hpRestore
    #Initialize attributes for the hospital class
    def __init__(self, name):
        self.name = name
        # self.pokemon = pokemon

    #This method sets the hp attribute of this pokemon class to a number(1000 in this case)
    def hpRestore(self, pokemon):
        pokemon.hp = 9000





class move:
#     #attribute
#     pokemon involved
#     trainers involved 
#     #method
#     changeHp
#     levelUp
    #Attributes for move class
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    #Move class methods
    def use_move(self):
        return(self.name + " for " + str(self.damage) + " damage!")



#Instantiated pokemon class with name pikachu
pikachu = pokemon("pikachu")
#Calls greeting method for pikachu instance
pikachu.greeting()
#Append moves to self.moves list of pikachu instnace
pikachu.add_move(move('thunderbolt', 30))
pikachu.add_move(move("tackle", 10))
#print self.moves list of pikachu instance
print(pikachu.moves)
#appends pikachy instance to pokedex of stanley instance
stanley.add_pokemon(pikachu)
#print name attribute of stanley instance and pokedex attribute of stanley instance
print("the pokemon in " + stanley.name + "'s pokedex are ")
for pokemon in stanley.pokedex:
    print(pokemon.name)
stanley.pokedex[0].attack(0)


#Hospital instance call 'hospital'
hospital = hospital('hospital')
#Call hpRestore method of pikachu instance
hospital.hpRestore(pikachu)
#Print hp attribute of pikachu instance
print(pikachu.hp)