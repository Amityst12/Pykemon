import random
import os
import sys

MAX_LEVEL = 36
MIN_LEVEL = 5

chosen_name = ""
chosen_pokemon_index = 0
pokemon_level = MIN_LEVEL

pokemon_current_hp = 0
enemy_current_hp = 0

pokemon_MaxHp = 0
enemy_MaxHP = 0

path_encounter = {
    1 : 5, #"Pidgey",
    2 : 7, #"Geodude",
    3 : 16, #"Zubat",
    4 : 10, #"Caterpie",
    5 : 8, #"Eevee",
    6 : 17,#"Poliwag",
    7 : 18,#"Gastly",#
    8 : 19,#"Moltres",#
    9 : 20,#"Ponyta",#
    10 : 21,#"Jynx", #
    11 : 13, #"Machop",
    12 : 22, #"Sandshrew",#
    13 : 23,#"Tangela",#
    14 : 24,#"Magnemite",#
    15 : 25,#"Scyther",#
    16 : 26,#"Mr. Mime",#
    17 : 27,#"Gyarados",#
    18 : 28, #"Kabuto"#
    19 : 29, #Lapras
    20 : 30, #Machamp
    21 : 31, #Gengar
    22 : 32, #Dragonite
    23 : 33, #Lucario
    
}
path_route = {
    1 : "On your way to the neighboring town, you encounter a mischievous group of wild Pokémon that you have to fend off to protect the package.",
    2 : "In the neighboring town, you meet a skilled Gym Leader who challenges you to a battle.\nIf you win, they grant you a Badge and offer valuable advice for your journey.",
    3 : "As you continue your journey, \nyou stumble upon a mysterious cave where you uncover ancient Pokémon artifacts, \nleading you on a quest to find the legendary Pokémon that once inhabited the region.",
    4 : "While exploring a dense forest,\nyou encounter a group of Pokémon trainers who form a friendship and travel together, helping each other become stronger.",
    5 : "In a bustling city,\nyou discover a Pokémon Contest where you can showcase your Pokémon's beauty and talent, and aim to become the Contest Champion.",
    6 : "While crossing a vast ocean, \nyour ship gets caught in a storm, \nyou find yourself stranded on a remote island where you uncover a secret society of Pokémon trainers with unique battling techniques.",
    7 : "In a haunted mansion,\nyou solve puzzles and battle ghostly Pokémon to uncover the mansion's dark secrets and put the spirits to rest.",
    8 : "You stumble upon a legendary Pokémon in a sacred grove\nmust prove your worthiness through a series of tests to form a bond with it and harness its power.",
    9 : "Deep in a volcanic region, \nyou encounter a group of villainous trainers who seek to control powerful Fire-type Pokémon and must stop their destructive plans.",
    10 : "You journey to a snowy mountain peak where you meet a wise hermit. \nHe teaches you the ways of Ice-type Pokémon and helps you master their abilities.",
    11 : "In a bustling metropolis, \nyou become involved in an underground Pokémon battling league, facing off against skilled trainers and working your way to the top.",
    12 : "While exploring a vast desert, \nyou stumble upon an ancient civilization that has harnessed the power of Ground-type Pokémon.\nthey train you in their unique battle techniques.",
    13 : "You discover a hidden valley. \nan ancient tribe lives in harmony with nature and trains Grass-type Pokémon. \nThey teach you the importance of balance and respect for the environment.",
    14 : "In a futuristic city, \nYou uncover a plot to control Electric-type Pokémon \nYou must team up with a group of tech-savvy trainers to foil the evil organization's plans.",
    15 : "While traveling through a dense jungle, \nYou encounter a Bug-type Pokémon that has been causing havoc. \nYou must calm it down and earn its trust to restore peace.",
    16 : "You stumble upon a secret training facility. \nTheir experienced trainers help you strengthen your Pokémon through intense battles and rigorous training regimes.",
    17 : "In a coastal town, \nYou join a group of fishermen and participate in fishing competitions to find a rare Water-type Pokémon and contribute to research efforts.",
    18 : "You explore a series of ancient ruins. \nYou uncover the history of a forgotten civilization and encounter trainers who specialize in Rock-type Pokémon.",
    19 : "You reach the Pokémon League, \nYou face off against the Elite Four and the Champion, proving your worth as a trainer and aiming to become the new Champion yourself!",
    20 : "Get reay for the next elite four battle.",
    21 : "Get reay for the next elite four battle.",
    22 : "Get reay for the next elite four battle.",
    23 : "Get reay for the next elite four battle.",
    22 : "Is that it?",
}
path_progress = 0
path_index = 1

pokemon_index = {
    1 : "Charmander",
    2 : "Balbasaur",
    3 : "Squirtel",
    4 : "Pikachu",
    5 : "Pidgy",
    6 : "Rattata",
    7 : "Geodude",
    8 : "Eevee",
    9 : "Nidoran",
    10 : "Caterpie",
    11 : "Widdle",
    12 : "Meowth",
    13 : "Machop",
    14 : "Magikarp",
    15 : "Oddish",
    16 : "Zubat",
    17 : "Poliwag",
    18 : "Gastly",
    19 : "Moltres",
    20 : "Ponyta",
    21 : "Jynx",
    22 : "Sandshrew",
    23 : "Tangela",
    24 : "Magnemite",
    25 : "Scyther",
    26 : "Mr. Mime",
    27 : "Gyarados",
    28 : "Kabuto",
    29 : "Lapras",
    30 : "Machamp",
    31 : "Gengar",
    32 : "Dragonite",
    33 : "Lucario"
    
}
pokemon_baseMove = {
    1 : "Ember",
    2 : "Vine Whip",
    3 : "Bubble",
    4 : "Spark",
    5 : "Peck",
    6 : "Tackle",
    7 : "Rollout",
    8 : "Tackle",
    9 : "Poison Sting",
    10 : "Tackle",
    11 : "Poison Sting",
    12 : "Scratch",
    13 : "Karate Chop",
    14 : "Splash",
    15 : "Absorb",
    16 : "Absorb",
    17 : "Bubble",
    18 : "Lick",
    19 : "Flamethrower",
    20 : "Ember",
    21 : "Powder Snow",
    22 : "Scratch",
    23 : "Absorb",
    24 : "Thunder Shock",
    25 : "Fury Cutter",
    26 : "Psychic",
    27 : "Hydro Pump",
    28 : "Scratch",
    29 : "Ice Shard",
    30 : "Cross Chop",
    31 : "Shadow Ball",
    32 : "Hyper Beam",
    33 : "Close Combat"
}
pokemon_baseAttack = {
    1 : "6",
    2 : "6",
    3 : "6",
    4 : "6",
    5 : "5",
    6 : "4",
    7 : "4",
    8 : "4",
    9 : "6",
    10 : "4",
    11 : "5",
    12 : "5",
    13 : "5",
    14 : "0",
    15 : "4",
    16 : "4",
    17 : "4",
    18 : "5",
    19 : "9",
    20 : "5",
    21 : "5",
    22 : "5",
    23 : "4",
    24 : "5",
    25 : "6",
    26 : "6",
    27 : "7",
    28 : "4",
    29 : "6",
    30 : "7",
    31 : "9",
    32 : "9",
    33 : "10"
}
pokemon_baseHp = {
    1 : "22",
    2 : "23",
    3 : "22",
    4 : "23",
    5 : "15",
    6 : "17",
    7 : "20",
    8 : "18",
    9 : "18",
    10 : "16",
    11 : "15",
    12 : "18",
    13 : "19",
    14 : "10",
    15 : "17",
    16 : "16",
    17 : "18",
    18 : "17",
    19 : "26",
    20 : "17",
    21 : "17",
    22 : "18",
    23 : "16",
    24 : "16",
    25 : "21",
    26 : "20",
    27 : "25",
    28 : "15",
    29 : "25",
    30 : "24",
    31 : "22",
    32 : "26",
    33 : "30"
}

def clear_terminal():
    #Clearing terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def Choose_Pokemon():
    #Making "Chosen" pokemon ours
    global chosen_pokemon_index,pokemon_current_hp,pokemon_MaxHp,chosen_name
    while True:
        q = input("Welcome to my pokemon game! press Enter to proceed.(q to quit)")
        if q == "q":
            sys.exit()
        clear_terminal()
        print("You wake up in your hometown and receive your first Pokémon from professor Erez\nhe asks you to deliver an important package to a neighboring town.")
        print("Chose from the following 3:")
        while True:
            Chosen = input("1 = Charmander, 2 = Balbasaur, 3 = Squirtel\n")
            if Chosen.isdigit():
                Chosen = int(Chosen)
                if 1<=Chosen<=4:
                    print(pokemon_index[Chosen] +" was selected.")
                    chosen_pokemon_index = Chosen
                    name = input(f"Type a name for {pokemon_index[Chosen]}, leave empty to not change\n")
                    if name != "":
                        chosen_name = name
                        print(f"Great!, {pokemon_index[Chosen]}'s new name is {name}")
                    else:
                        chosen_name = pokemon_index[Chosen]
                    print("Sounds like a beggining of a great adventure!")
                    input()
                    pokemon_current_hp = pokemon_MaxHp = get_HP(Chosen,pokemon_level)
                    return Chosen
            clear_terminal()
            print(f"{Chosen} is invalid, try again:")

def get_Wild(Chosen):
    #Choosing wild pokemon
    clear_terminal()
    while True:
        wildPokemon = random.choice(list(pokemon_index.keys()))
        if int(Chosen) != int(wildPokemon):
            print(f"A wild {pokemon_index[wildPokemon]} has appeared!")
            return wildPokemon           
         
def make_Path_Encounter():
    #Making encounter
    global path_index
    if path_progress < 24:
        path_index = path_encounter[path_progress]
    clear_terminal()
    if path_progress == 1:
        print(f"A wild {pokemon_index[path_index]} has appeared!")
    elif path_progress == 2:
        print(f"Brock, the gym leader fights you with his {pokemon_index[path_index]}!!")
    elif 3 <= path_progress <= 5:
        print(f"A wild {pokemon_index[path_index]} has appeared!")
    elif path_progress == 6:
        print(f"Tom , the local fisherman, challenges you to a battle using his {pokemon_index[path_index]}")
    elif path_progress == 7:
        print(f"A wild {pokemon_index[path_index]} has appeared!")
    elif path_progress == 8:
        print("THE MIGHTY MOLTRESS HAS APPEARED!")
    elif path_progress == 9:        
        print(f"A wild {pokemon_index[path_index]} has appeared!")
    elif path_progress == 10:
        print(f"The wise hermit challenges you with his Ice-Type {pokemon_index[path_index]}")
    elif path_progress == 11:
        print(f"Bellamy pulls his {pokemon_index[path_index]} for a battle!")
    elif path_progress == 12:
        print(f"Blel thinks its a good time for a pokemon battle using his {pokemon_index[path_index]}!")
    elif path_progress == 13:
        print(f"The ancient tribe's leader didn't think twice and quickly surprised you with his {pokemon_index[path_index]}")
    elif 14<= path_progress <= 18:
        print(f"A wild {pokemon_index[path_index]} has appeared!")
    elif path_progress == 19:
        print("Its time for the finallll fourrr!!!")
        print(f"For first, you fight Loelei's {pokemon_index[path_index]}")
    elif path_progress == 20:
        print(f"Second fight! you fight Bruno's {pokemon_index[path_index]}")
    elif path_progress == 21:
        print(f"For third, time to battle Agatha's {pokemon_index[path_index]}")
    elif path_progress == 22:
        print(f"Is it the last battle? get ready for Cynthia's {pokemon_index[path_index]}")
    elif path_progress == 23:
        print("What a surprise!!\nIts Amit!!!\nGet ready to face his MIGHTY Lucario.")

def Make_Battle_Stats(Chosen,wildPokemon):
    #Declaring battle and lvls
    global pokemon_current_hp, enemy_current_hp, enemy_MaxHP, pokemon_MaxHp
    wildPokemonLvl = random.randrange(pokemon_level-4, pokemon_level+2) 
    enemy_current_hp = enemy_MaxHP = get_HP(wildPokemon,wildPokemonLvl)
    print(f"\nGOOOOO {chosen_name}!")
    print(f"Lvl.{pokemon_level} {chosen_name} HP:{pokemon_current_hp}")
    print("VS.")
    print(f"Lvl.{wildPokemonLvl} {pokemon_index[wildPokemon]} HP:{enemy_current_hp}")
    return wildPokemonLvl
            
def Pokemon_Battle(Chosen,WildPokemon,wildPokemonLvl):
    global pokemon_current_hp, enemy_current_hp
        
    # 1 = Ally 2 = Enemy , stronger pokemon goes first
    if wildPokemonLvl <= pokemon_level:
        Turn = 1
        input(f"{chosen_name} is faster so he gets to start!")
    else:
        Turn = 2
        input(f"{pokemon_index[WildPokemon]} is faster so he gets to start!")
    
    #Start combat untill done:     
    while True:
        clear_terminal()
        if check_Win(): #Checks win for every turn
            input("Fight is over.")
            return Winner(Chosen,WildPokemon)
        
        print(f"{chosen_name} HP: {pokemon_current_hp}\n{pokemon_index[WildPokemon]} HP: {enemy_current_hp}") #Print status
        if Turn == 1: #ALLY TURN
            print("\nYour turn")
            print(f"1 - Use {pokemon_baseMove[Chosen]}!")
            print("2 - Heal")
            print("3 - RUN")
            while True:
                Decision = input()
                if Decision.isdigit() and 1<= int(Decision) <= 3:
                    break
                print(f"{Decision} is not viable!")
            
            #Ally attack    
            if int(Decision) == 1:
                allyDamage = get_DMG(Chosen,pokemon_level)
                odds = random.randint(1,100)
                criticalAlly = allyDamage * 2
                if 95 <= odds <=100: #MISSED
                    print(f"{pokemon_index[WildPokemon]} has managed to dodge!")
                    input("No damage was dealt.")
                elif 1 <= odds <= 15: #CRITICALHIT
                    print("Its a critical hit!!")
                    input(f"{chosen_name} used {pokemon_baseMove[Chosen]}, he dealt {criticalAlly} damage!")
                    set_HP("Enemy","Deal", criticalAlly)
                else:
                    input(f"{chosen_name} used {pokemon_baseMove[Chosen]}, he dealt {allyDamage} damage!")
                    set_HP("Enemy","Deal", allyDamage)
                    
            #Ally heal
            if int(Decision) == 2:
                Healed = make_Heal("Ally")
                input(f"{chosen_name} has healed for {Healed} HP!")
                
            #Ally run
            if int(Decision) == 3:
                run = random.randint(1,100)
                if 1 <= run <= 30:
                    print("You ran....")
                    input(f"{chosen_name} has left with {pokemon_current_hp} HP.")
                    break
                input("You tried to run, yet failed")
                
            Turn = 2
            
        elif Turn == 2 :#ENEMY TURN
            print("\nEnemy turn!")
            EDecision = random.randint(1,10)
            if enemy_MaxHP == enemy_current_hp: #Max HP: enemy rarely heals.
                EDecision = random.randint(1,6)
            if 1<=EDecision <=5: #Enemy chose to attack
                enemyDamage = get_DMG(WildPokemon,pokemon_level)
                odds = random.randint(1,100)
                criticalEnemy = enemyDamage * 2
                if 95<= odds <=100: #MISSED
                    print(f"{chosen_name} has managed to dodge!")
                    input("No damage was dealt.")
                elif 1 <= odds <= 10: #CRITICAL
                    print("Its a critical hit!!")
                    input(f"{pokemon_index[WildPokemon]} used {pokemon_baseMove[WildPokemon]}, he dealt {criticalEnemy} damage!")
                    set_HP("Ally","Deal", criticalEnemy)
                else:
                    input(f"{pokemon_index[WildPokemon]} used {pokemon_baseMove[WildPokemon]}, he dealt {enemyDamage} damage!")
                    set_HP("Ally","Deal", enemyDamage)
            
            else: #Enemy chose to heal
                Healed = make_Heal("Enemy")
                input(f"{pokemon_index[WildPokemon]} has healed for {Healed} HP!")
                        
            Turn = 1
            
    print(f"Battle is over.\n{chosen_name} has left with {pokemon_current_hp} HP. ")       

        
def get_HP(Pokemon ,level):
    #Getting any desired pokemon starting HP with level
    HP = int(pokemon_baseHp[Pokemon]) + int(2.3 * level)
    return HP

def set_HP(Target, Type, HP): #Enemy, Ally - Heal,Deal , Amount
    #Sets hp using Heal and Deal
    global pokemon_current_hp, enemy_current_hp, pokemon_MaxHp, enemy_MaxHP
    #Ally
    if Target == "Ally": 
        if Type == "Deal":
            if pokemon_current_hp - HP <= 0: 
                pokemon_current_hp = 0
            else:
                pokemon_current_hp += - HP
            
        if Type == "Heal":
            if (pokemon_current_hp < pokemon_MaxHp):
                if pokemon_current_hp + HP > pokemon_MaxHp:
                    pokemon_current_hp = pokemon_MaxHp
                else:
                    pokemon_current_hp += HP 
            else:
                input("Already have max HP!")        
    #Enemy                         
    elif Target =="Enemy":
        if Type == "Deal":
            if enemy_current_hp - HP <= 0: 
                enemy_current_hp = 0
            else:
                enemy_current_hp += - HP
            
        if Type == "Heal":
            if (enemy_current_hp < enemy_MaxHP):
                if enemy_current_hp + HP > enemy_MaxHP:
                    enemy_current_hp = enemy_MaxHP
                else:
                    enemy_current_hp += HP 
            else:
                input("Already have max HP!")
        
def get_DMG(Pokemon,level):
    #Getting pokemon damage
    Pokemon_Damage = int(pokemon_baseAttack[Pokemon])
    Pokemon_Damage += int(level*1.5)
    Pokemon_Damage = random.randint(Pokemon_Damage-3, Pokemon_Damage+2)
    return Pokemon_Damage

def get_fixed_DMG(Pokemon,level):
    #Get fixed amount of damage
    Pokemon_Damage = int(pokemon_baseAttack[Pokemon])
    Pokemon_Damage += int(level*1.5)
    return Pokemon_Damage

def make_Heal(Target):
    #Make heal for "Ally" or "Enemy" pokemon infight
    global pokemon_MaxHp, enemy_MaxHP, pokemon_current_hp, enemy_current_hp
    if Target == "Ally":
        inc = random.uniform(1.8,4.0)
        Amount = int(pokemon_MaxHp/inc)
        if Amount + pokemon_current_hp >= pokemon_MaxHp:
            Efresh = (Amount + pokemon_current_hp) - pokemon_MaxHp
            Amount = Amount - Efresh
            pokemon_current_hp = pokemon_MaxHp
        else:
            pokemon_current_hp = pokemon_current_hp + Amount
        return Amount
    
    elif Target =="Enemy":
        inc = random.uniform(2.0,4.0)
        Amount = int(enemy_MaxHP/inc)
        if Amount + enemy_current_hp >= enemy_MaxHP:
            Efresh = (Amount + enemy_current_hp) - enemy_MaxHP
            Amount = Amount - Efresh
            enemy_current_hp = enemy_MaxHP
        else:
            enemy_current_hp = enemy_current_hp + Amount
        return Amount

def check_Win():
    #Checks if pokemon's HP reaches 0 - win
    global enemy_current_hp, pokemon_current_hp
    if enemy_current_hp == 0 or pokemon_current_hp == 0:
        return True
    return False

def Winner(Chosen,WildPokemon):
    #After check_win -> see who lost and rewards the other
    global pokemon_level, pokemon_current_hp, pokemon_MaxHp
    if enemy_current_hp == 0:
        input(f"{pokemon_index[WildPokemon]} has fainted. \n{chosen_name} has won the battle!")
        if random.randint(1,2) == 1:
            level_Up()
        return Chosen
    
    elif pokemon_current_hp == 0:
        pokemon_current_hp = pokemon_MaxHp
        input(f"{chosen_name} has fainted and will be sent to the nurse.")
        return WildPokemon
    
def level_Up():
    #Adjust stats on LEVELUP
    global pokemon_level, chosen_pokemon_index,pokemon_current_hp,pokemon_MaxHp
    pokemon_level += 1
    HP = get_HP(chosen_pokemon_index, pokemon_level) - pokemon_MaxHp
    DMG = int(pokemon_level * 0.3)
    pokemon_MaxHp = get_HP(chosen_pokemon_index, pokemon_level)
    input(f"Congratulations, {chosen_name} has level'd up to {pokemon_level}!!\n+{HP} HP \n+{DMG} DMG")
    if pokemon_MaxHp != pokemon_current_hp:
        pokemon_current_hp = pokemon_MaxHp
        input(f"{chosen_name}'s HP has been restored.")
    
def Menu():
    #Main menu
    global pokemon_current_hp, pokemon_MaxHp
    while True:
        clear_terminal()
        print("Select your next deicison:")
        print("1 - To adventure")
        print("2 - Search for wild pokemon")
        print("3 - Inspect pokemon stats")
        print("4 - Visit nurse")
        print("0 - Quit game.")
        decision = input()
        if decision.isdigit(): 
            decision = int(decision)
            if  0<= decision <=4:
                if decision == 1: #Adventure 
                    Adventure()
                if decision == 2: #Wild
                    return
                if decision == 3: #Stats
                    input(f"{pokemon_index[chosen_pokemon_index]}:\nName: {chosen_name}\n{pokemon_current_hp}/{pokemon_MaxHp} HP\n{get_fixed_DMG(chosen_pokemon_index, pokemon_level)} DMG")
                if decision == 4: #Nurse
                    if pokemon_MaxHp == pokemon_current_hp:
                        input(f"{chosen_name} already has max health.")
                    else:
                        input(f"You visited the hospital.\n{chosen_name} has recovered to full health.")
                        pokemon_current_hp = pokemon_MaxHp
                if decision == 0: # Quit game
                    q = input("Are you sure? type 0 to confirm")  
                    if q =="0":
                        sys.exit()
                    else:
                        clear_terminal()
            else:
                clear_terminal()
                input(f"{decision} is invalid")
        else:
            clear_terminal()                
            input(f"{decision} is invalid")                  
 
def Adventure():
    #Adventure menu
    global chosen_pokemon_index,pokemon_level,path_progress, pokemon_current_hp, pokemon_MaxHp
    
    if path_progress >= 24:
        again = True
        while again:
            clear_terminal()
            re = input("You have finished the main story, would you like to restart with your current pokemon?[Y,N]\n")
            if re == "Y" or re == "y":
                path_progress = 0
                again = False
            elif re == "N" or re =="n":
                again = False
                input("As you wish.")
                break
            else:
                print(f"{re} is invalid, try again.")
         
    
    clear_terminal()
    if path_progress == 0 : #First time
        input("Get ready to start your adventure!")
        path_progress += 1
        
    while True:
        if path_progress >= 18: #FINAL 4
            clear_terminal()
            if path_progress < 24 :
                input(f"-{path_route[path_progress]}")
            else:
                break
                
            make_Path_Encounter()
            enemy_path_level = Make_Battle_Stats(chosen_pokemon_index, path_index)
            winner = Pokemon_Battle(chosen_pokemon_index, path_index, enemy_path_level)
            if winner == chosen_pokemon_index :
                path_progress += 1
            
            if path_progress == 24 : 
                input("\n-The adventure is finally all over.\nThank you very much for playing!")
                break
        
        if path_progress != 1 and path_progress <= 24: #After first
            Think = True
            while Think:
                clear_terminal()
                if path_progress %3 == 0:
                    decision = input("1 - Keep going!\n2 - Inspect pokemon stats \n3 - Back to menu\n4 - Visit nurse\n")
                else:
                    decision = input("1 - Keep going!\n2 - Inspect pokemon stats \n3 - Back to menu\n")
                    
                if decision.isdigit():
                    decision = int(decision)
                    if 1<= decision <= 4:
                        if decision == 1: #Keep playing
                            Think = False
                        elif decision == 2: #Stats
                            input(f"{pokemon_index[chosen_pokemon_index]}:\nName: {chosen_name}\n{pokemon_current_hp}/{pokemon_MaxHp} HP\n{get_fixed_DMG(chosen_pokemon_index, pokemon_level)} DMG")
                        elif decision == 3: #Back to menu
                            return
                        elif decision == 4 and path_progress %3 == 0: #Nurse option every 3th turn
                            if pokemon_MaxHp == pokemon_current_hp:
                                input(f"{chosen_name} already has max health.")
                            else:
                                input(f"You visited the hospital.\n{chosen_name} has recovered to full health.")
                                pokemon_current_hp = pokemon_MaxHp
                    else:
                        input(f"{decision} is invalid") 
                else:
                    input(f"{decision} is invalid")
            clear_terminal()
        
        if path_progress < 24:
            input(f"-{path_route[path_progress]}")
            make_Path_Encounter()
            enemy_path_level = Make_Battle_Stats(chosen_pokemon_index, path_index)
            winner = Pokemon_Battle(chosen_pokemon_index, path_index, enemy_path_level)
        
        if winner == chosen_pokemon_index :
            path_progress += 1
                              
def Main():
    #Main event
    clear_terminal()
    Chosen = Choose_Pokemon()
    while True:
        Menu()
        wildPokemon = get_Wild(Chosen)
        wildPokemonLvl = Make_Battle_Stats(Chosen,wildPokemon)
        Pokemon_Battle(Chosen,wildPokemon,wildPokemonLvl)
    
    
Main()