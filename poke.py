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
        self.pokedex.append(pokemon.name) 

stanley = trainer("stanley")
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

pikachu = pokemon("pikachu")
pikachu.greeting()
pikachu.add_move("thunderbolt")
pikachu.add_move("tackle")
print(pikachu.moves)
stanley.add_pokemon(pikachu)
print("the pokemon in " + stanley.name + "'s pokedex are " + str(stanley.pokedex))

class hospital:
#     #attribute
#     city
#     #method
#     changeName
#     hpRestore
    def __init__(self, name):
        self.name = name
        # self.pokemon = pokemon

    def hpRestore(self, pokemon):
        pokemon.hp = 1000

hospital = hospital('hospital')
hospital.hpRestore(pikachu)
print(pikachu.hp)



# class battle:
#     #attribute
#     pokemon involved
#     trainers involved 
#     #method
#     changeHp
#     levelUp