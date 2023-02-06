# Corina Luca

# PART II

#– – – – – – – – – – – – – –  – – – – – – – – – – – – – – – – – – – – – – – – – – – –
# Functions

def invalid_num(x):
    if x.isdigit() and int(x) > 0:
        return False
    else:
        print("Invalid, please try again")
        return True
    
def table(list, itiration):
    print(format("Name", "13s"),format("Amount Available", "19s"), "Adoption Fee", " Type(s)", sep ="")        

    if itiration == "index":
        for i in range(len(list)):
            print(format(pokemon_names[i].capitalize(), "28s"), pokemon_amounts[i], format(adopt_fee[i], ">15,.2f"), sep ="", end = " ")        

            if len(pokemon_types[i]) == 1:
                one_type = pokemon_types[i][0]
                print(pokemon_types[i][0].capitalize())

            else:
                for j in range(len(pokemon_types[i])):
                    mult_type = (pokemon_types[i][j])
                    print(mult_type.capitalize(), end = " ")
                print()

    if itiration == "list":

        for i in list:
            print(format(pokemon_names[i].capitalize(), "28s"), pokemon_amounts[i], format(adopt_fee[i], ">15,.2f"), sep ="", end = " ")
            
            if len(pokemon_types[i]) == 1:
                one_type = str(pokemon_types[i][0])
                print(one_type.capitalize())

            else:
                for j in range(len(pokemon_types[i])):
                    mult_type = (pokemon_types[i][j])
                    print(mult_type.capitalize(), end = " ")
                print()

#– – – – – – – – – – – – – –  – – – – – – – – – – – – – – – – – – – – – – – – – – – –
# Pokemon lists

pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
adopt_fee = [100.0 ,50.0 ,25.0 , 1000.0]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

#– – – – – – – – – – – – – –  – – – – – – – – – – – – – – – – – – – – – – – – – – – –

# Print Welcome Message
print("Welcome to the Pokemon Center!")

# Code starts here:
while True:

    # Validate commands
    instr = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ").lower()

    # Invalid command    
    if not instr in ['a', 'r', 'e','t', 's','l', 'q']:

        print("Unknown command, please try again")

    # Add
    elif instr == 'a':
        while True:

            # Check if Pokemon exists
            add_name = input("Enter name of new pokemon: ").lower()

            if add_name in pokemon_names:
                print("Duplicate name, add operation cancelled")

            else:
                pokemon_names.append(add_name)
                break
            
        # Verify if amount valid int and add if so    
        amount_add = input("How many of these Pokemon are you adding? ")        

        while invalid_num(amount_add):
                 
            amount_add = input("How many of these Pokemon are you adding? ")   

        pokemon_amounts.append(int(amount_add))


        # Verify if fee is valid float and add if so
        fee_add = input("What is the adoption fee for this Pokemon? ")

        while invalid_num(fee_add):

            fee_add = input("What is the adoption fee for this Pokemon? ")

        adopt_fee.append(float(fee_add))

        # Create new empty list to keep track of new types
        new_type = []
        
        type_add = input("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'What type of Pokemon is this? ").lower()

        # Create while loop so user can add as many types using sentinel 'end'
        # Remember user must enter at least one valid type
        while True:

            # If type in list, add
            if type_add in valid_pokemon_types:
                    new_type.append(type_add)
                    print("Type", type_add, "applied")
            
            # elif it is command 'help' show options
            elif type_add == 'help':

                for i in valid_pokemon_types:
                    print("*", i)

            # elif 'end' quit loop but only if there is at least one new type        
            elif type_add == 'end' and len(new_type) == 0:
                print("You must enter at least one valid 'type'")

            elif type_add == 'end' and len(new_type) > 0:
                print("Pokemon added!")
                break

            # if input is none of these, it must be wrong so prompt error message
            # to user and if loop hasn't ended by now, prompt the question again
            else:
                print("This is not a valid type, please try again")

                            
            type_add = input("What type of Pokemon is this? ").lower()                            

        # Once we have obtained all desired type info in list, add this to original list
        pokemon_types.append(new_type)

    # Remove
    elif instr == 'r':

        name_remove = input("Enter name of Pokemon to remove: ").lower()

        if not name_remove in pokemon_names:
            print("Pokemon not found, cannot remove")

        else:
            for i in range(len(pokemon_names)):
                if name_remove == pokemon_names[i]:
                    del pokemon_names[i]
                    del pokemon_amounts[i]
                    del adopt_fee[i]
                    del pokemon_types[i]

                    print("Pokemon removed")
                    break
            
    # Reporting feature
    elif instr == 'e':
        max_price = max(adopt_fee)

        for i in range(len(adopt_fee)):
            if max_price == adopt_fee[i]:
                print("Highest priced Pokemon:", pokemon_names[i].capitalize(), "@ $" + format(adopt_fee[i], ",.2f"), "per Pokemon" )

        min_price = min(adopt_fee)

        for i in range(len(adopt_fee)):
            if min_price == adopt_fee[i]:
                print("Lowest priced Pokemon:", pokemon_names[i].capitalize(), "@ $" + format(adopt_fee[i], ",.2f"), "per Pokemon" )

        total_sum = 0

        for i in range(len(adopt_fee)):
            total_sum += adopt_fee[i] * pokemon_amounts[i]
            
        print("Total cost to adopt all Pokemon in the Center: $" + format(total_sum, ",.2f"))

        
    # Search by Type
    elif instr == 't':
        type_pokemon = input("Enter Pokemon type: ").lower()

    # Initialize boolean and list to keep track of wether
    #type is available and its index
        is_valid_type = False
        valid_i = []

        # Go through list inside list using for loops
        for i in range(len(pokemon_types)):
             if len(pokemon_types[i]) == 1:
                 if type_pokemon == pokemon_types[i][0]:
                    valid_i += [i]
                    is_valid_type = True

             elif len(pokemon_types[i]) > 1:
                 for j in range(len(pokemon_types[i])):
                     if type_pokemon == pokemon_types[i][j]:
                         valid_i += [i]
                         is_valid_type = True

        # Show table of results if it is a valid type
        if is_valid_type:
    
            table(valid_i, "list")
        else:
            print("We have no Pokemon of that type at our Pokemon Center")

    # Search by name        
    elif instr == 's':
        
        name_pokemon = input("Name of Pokemon to search for: ").lower()

        # Initialize boolean and var to keep track of existence of string in list
        # and its index
        
        ispokemon = False
        index = 0

        # Go through list with for loop
        for i in range(len(pokemon_names)):
            if name_pokemon == pokemon_names[i]:
                ispokemon = True
                index = i

        # If pokemon exists in list, display info using the index of parallel lists
        if ispokemon == True:
            print("We have", pokemon_amounts[index], name_pokemon.capitalize(), "at the Pokemon Center")
            print("It will cost $" + format(adopt_fee[index], ",.2f"), "to adopt this Pokemon")
            
            print(pokemon_names[index], " has the following types:", end = " ")

            if len(pokemon_types[index]) == 1:
                one_type = str(pokemon_types[index][0])
                print(one_type.capitalize())
            else:
                for i in range(len(pokemon_types[index])):
                    mult_type = (pokemon_types[index][i])
                    print(mult_type.capitalize(), end = " ")
                print()

        # If pokemon doesn't exist display following
        else:
            print("We do not have any", name_pokemon, "at the Pokemon Center")

    # List
    elif instr == 'l':
        
        table(pokemon_names, "index")

    # Quit
    else:
        print("See you next time!")
        break

    print()
