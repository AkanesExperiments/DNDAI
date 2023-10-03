import random
import time
import requests
# import only system from os
from os import system, name
from gtts import gTTS
from playsound import playsound
from pprint import pprint
import inquirer

tts_enabled = True


def TTSmodule(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    while True:
        try:
            playsound('output.mp3')
            break  # Break out of the loop if playsound succeeds
        except Exception as e:
            print(f"An error occurred while playing the sound")
            time.sleep(1)  # Wait for a moment before trying again


message_prompts = []

dndCombatrulesandexample = """D&D 5e Combat Basics:
        Initiative: At the start of combat, each participant, including player characters and creatures, rolls a d20 and adds their initiative modifier. The result determines the order in which everyone takes their turns.
        Turn Order: Combat is divided into rounds, and each round consists of turns for every participant. A typical turn includes a movement, an action, and a potential bonus action and reaction.
        Movement: Characters can move a certain distance (measured in feet) during their turn. Movement can be split before and after taking an action.
        Actions: During a turn, a character can take an action, which includes attacking, casting spells, using special abilities, or interacting with objects. Some actions, like attacking, require rolling a d20 and adding modifiers to determine success.
        Bonus Actions and Reactions: Some abilities and spells allow characters to take bonus actions or reactions, respectively, on their turn or in response to specific triggers.
        Attacks and Damage: To attack, roll a d20 and add relevant modifiers (like the character's proficiency and ability score modifiers). If the result meets or exceeds the target's Armor Class (AC), the attack hits. Damage is then rolled based on the weapon or ability being used.
        Hit Points (HP): Each character and creature has hit points representing their health. When a character takes damage, their hit points decrease. If hit points drop to zero, the character falls unconscious and might die if not stabilized.
    
    Example Combat:
    Player Character (PC):
    Name: Aric
    Class: Fighter
    AC: 18
    HP: 32
    Weapon: Longsword (+5 to hit, 1d8+3 slashing damage)
    Bandits (x3):
    AC: 12
    HP: 11 each
    Weapon: Shortsword (+3 to hit, 1d6+1 piercing damage)
    
    Round 1:
        Initiative: Aric rolls a 17 for initiative (+2 initiative modifier). Bandits roll 10, 8, and 12 (+0 initiative modifier). Order: Aric, Bandit 3, Bandit 1, Bandit 2.
        Aric's Turn: Aric charges at Bandit 1 and swings his longsword. He rolls a 14 on the attack roll (+5 to hit), which hits the Bandit 1's AC of 12. Aric deals 9 slashing damage (1d8+3).
        Bandits' Turn: Bandit 3 moves closer to Aric and attacks with a shortsword. The attack roll is a 15 (+3 to hit), which meets Aric's AC of 18. Aric takes 4 piercing damage (1d6+1).
    ...and the combat encounter continues with each participant taking turns until the encounter concludes.
    Remember that D&D combat involves rolling dice, determining successes, and reacting to the actions of others. The outcome can be influenced by a variety of factors, including character abilities, tactics, and the luck of the dice rolls."""

dnd5erules = """Basic rules for Dungeons & Dragons 5th Edition (D&D 5e):
    Ability Scores: Characters have six primary ability scores: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma. These scores determine your character's capabilities and bonuses.
    Character Creation: You choose a race, class, background, and alignment for your character. You roll dice to determine ability scores or use a point-buy system.
    Hit Points (HP): Your character's health is measured in hit points. When you take damage, your HP decreases. If your HP drops to zero, you fall unconscious and may die if you take more damage.
    Classes: There are various classes (e.g., Fighter, Wizard, Rogue) with unique abilities and features. Each class has its own progression and playstyle.
    Levels: Characters gain experience points (XP) to level up. With each level, you gain new abilities, hit points, and sometimes access to spells.
    Skills: Skills represent your character's proficiency in certain activities (e.g., Stealth, Persuasion). Your proficiency bonus is added to skill checks you're proficient in.
    Saving Throws: These are checks made to resist harmful effects such as spells, traps, or poisons. They're based on your ability scores and may benefit from your proficiency bonus.
    Advantage and Disadvantage: In some situations, you roll two d20s and take the higher (advantage) or lower (disadvantage) result, depending on the circumstance.
    Combat: Combat involves initiative (determining who acts first), attacks, and various actions (e.g., Move, Dash, Dodge). You roll a d20 and add relevant modifiers to hit and deal damage.
    Spellcasting: Some classes can cast spells. Spells have levels, components (verbal, somatic, material), and effects. Spellcasters prepare spells from their spell list.
    Resting: Short rests allow you to regain hit points through hit dice, and long rests restore hit points, spells, and class features.
    Alignment: Your character's alignment reflects their moral and ethical beliefs. It ranges from Lawful Good to Chaotic Evil.
    Equipment: Characters start with equipment and may find or buy new items like weapons, armor, and magical items.
    Death Saving Throws: When your character reaches zero hit points, they start making death saving throws to determine if they stabilize or die.
    Roleplaying: D&D is about storytelling and roleplaying. You interact with NPCs (non-player characters), make choices, and engage in imaginative adventures.
    Create a World: Design a rich and immersive world for your players to explore. Develop places, NPCs, factions, and lore to make the world feel alive.
    Set the Tone: Decide on the tone and style of your campaign. Is it serious or lighthearted? Epic or gritty? This sets the atmosphere for your players.
    Adapt and Improvise: Players are unpredictable. Be prepared to adapt your plans on the fly and improvise when they take unexpected actions.
    Fairness and Fun: Your role is to facilitate fun for the players. Strive for a balance between challenging encounters and rewarding victories.
    Describe Environments: Use vivid descriptions to help players visualize the settings, NPCs, and encounters. Engage their senses to make the world come alive.
    Player Agency: Allow players to make meaningful choices that affect the story. Avoid railroading and let them shape the narrative.
    Roll Behind the Screen: For some rolls, like secret perception checks, roll dice behind a screen to keep outcomes hidden. This adds suspense and mystery.
    Listen to Players: Pay attention to your players' preferences, feedback, and ideas. This helps you tailor the game to their interests.
    Encourage Roleplaying: Reward creative roleplaying and character interactions. NPCs with distinct personalities can enhance the roleplaying experience.
    Homebrew and Customization: Feel free to create your own content, rules, and homebrew elements. Just ensure they are balanced and enhance the game.
    Rulings Over Rules: If a rule is unclear or slows down the game, make a ruling in the moment and research the specifics later.
    NPCs and Voices: Give NPCs distinct voices and personalities. This makes interactions memorable and helps players differentiate between characters.
    Challenge and Growth: Provide challenges that match the players' capabilities. Balancing encounters keeps the game engaging without being overwhelming.
    Player Backstories: Incorporate player backstories into the campaign to create personal investment and character development.
    Pacing: Control the pacing of the game. Balance combat, exploration, and roleplaying to maintain engagement.
    Session Prep: Prepare key story points, encounters, and NPCs. Have a general idea of where the story is heading, but remain flexible.
    Consequences: Actions have consequences. Players' choices can impact the world and how NPCs react to them.
    Safety and Comfort: Establish boundaries and ensure a safe and comfortable environment for all players. Use tools like Session Zero to discuss expectations.
    Have Fun: As the DM, your enjoyment matters too. Embrace the unexpected moments and enjoy the collaborative storytelling experience."""

varHomebrew = "True"

testmodevar = "False"


def textGen(text):
    googleapikey = "" # Add you own Api Key get it at https://makersuite.google.com/app

    url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={googleapikey}"

    json_output = "n/a"

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "prompt": {
            "text": text
        },
        "safety_settings": [
            {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 4},
            {"category": "HARM_CATEGORY_TOXICITY", "threshold": 4},
            {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 4},
            {"category": "HARM_CATEGORY_SEXUAL", "threshold": 4},
            {"category": "HARM_CATEGORY_MEDICAL", "threshold": 4},
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 4}
        ]
    }

    # Make a POST request with JSON data
    response = requests.post(url, json=data, headers=headers)
    # print(response.text)
    if response.status_code == 200:
        # Request was successful
        json_data = response.json()
        candidates = json_data.get('candidates', [])
        if candidates:
            json_output = candidates[0].get('output', '')
            return json_output


DMExt = """DM Profile:
    Name: Alex
    Experience: Alex has been playing D&D for several years and has experience running campaigns for both new and experienced players. They enjoy creating immersive worlds and incorporating homebrew elements into their games.
    Campaign Setting: Alex has crafted a high-fantasy world called "Eldoria," where magic and mystical creatures abound. The campaign takes place in a diverse realm with bustling cities, ancient ruins, and untamed wilderness.
    Session Setup: Alex prepares for the session by creating a town called "Rivervale" as the starting point for the adventurers. They've populated the town with colorful NPCs, including the enigmatic innkeeper Elyndra and the boisterous blacksmith Garik.
    Session Start: The players' characters arrive in Rivervale seeking adventure. Alex describes the bustling town, the smell of freshly baked bread wafting from the bakery, and the sound of a bard playing a lively tune in the square.
    Player Interaction: One player, playing a rogue named Sylas, decides to approach the innkeeper Elyndra to gather information. Alex adopts a soft-spoken and mysterious voice for Elyndra, giving the character an air of intrigue. Elyndra reveals rumors of a hidden treasure deep within the nearby Whispering Woods.
    Exploration: The party decides to investigate the Whispering Woods. Alex describes the dense trees, the soft rustling of leaves, and the feeling that the forest is alive with secrets. As they delve deeper, Alex describes the eerie silence that falls upon them and the discovery of an overgrown path.
    Encounter: Upon the path, the party encounters a group of goblins. Alex sets the scene with the goblins huddled around a campfire, arguing over a stolen bag of gold. They initiate a skill challenge to negotiate with or sneak past the goblins. Dice rolls determine the outcome, and the players successfully convince the goblins to share information in exchange for some rations.
    Decision Time: The goblins reveal that the treasure is guarded by an ancient guardian deep within the woods. The players must decide whether to face the guardian or seek an alternative route to the treasure.
    Session End: As the session comes to a close, Alex describes the setting sun casting a warm glow over Rivervale. They ask the players what their characters plan to do next and suggest that they take time to discuss their next steps before the next session.
    In this example, Alex, the DM, creates an engaging world, introduces NPCs with distinct personalities, and provides choices for the players to make. They incorporate both exploration and roleplaying elements while staying flexible to adapt to player decisions. This type of storytelling and interaction is what makes D&D campaigns come to life!"""

CampignExt = """Campaign Title: Shadows of Arcanum
    Campaign Setting:
    The campaign is set in the realm of Arcanum, a land shrouded in mystery and magic. The world is a blend of steampunk technology and arcane wonders, where ancient ruins hold both untold power and forgotten secrets.
    Premise:
    The players are a group of freelance investigators known as the "Arcane Defenders." In Arcanum, strange phenomena have been occurring: sudden dimensional rifts, bizarre creatures appearing, and whispers of an otherworldly threat.
    Session 1: The Enigmatic Rift
    The campaign starts in the city of Steamhaven. The players receive a job offer from a nervous scholar named Professor Elara. She reports a sudden dimensional rift in the outskirts of the city, and she fears it might be connected to the rise of unknown magical forces.
    Session Highlights:
    The players investigate the rift, discovering that it leads to a realm of twisted shadows.
    They encounter "Shadowspawn," creatures that feed on arcane energy and have been leaking into Arcanum.
    The players close the rift temporarily, gaining the attention of the enigmatic Arcane Council.
    Session 2: Council Conundrum
    The Arcane Council, a secretive organization that safeguards magic, summons the players. The council tasks them with investigating the source of the dimensional rifts and stopping the Shadowspawn incursions.
    Session Highlights:
    The players research ancient tomes, discovering an old prophecy that warns of a cosmic imbalance.
    They follow leads to an abandoned clockwork factory where Shadowspawn are being summoned.
    The players face a clockwork monstrosity guarding a portal to the Shadow Plane.
    Session 3: Veiled Machinations
    The players track down an enigmatic figure named Orlan Blackthorn, rumored to be behind the rifts. They infiltrate his hidden lair, uncovering a complex network of portals and plans to bring the Shadow Plane into Arcanum.
    Session Highlights:
    The players navigate traps and puzzles within Blackthorn's lair, using their wits and teamwork.
    They confront Orlan Blackthorn, who reveals he seeks to harness the power of the Shadow Plane for his own ambitions.
    A climactic battle ensues, leading to Blackthorn's escape and the partial collapse of the lair.
    Session 4: Ascendant Shadows
    As the campaign intensifies, the players learn that Blackthorn seeks to summon an ancient entity known as the "Eclipse Serpent" from the Shadow Plane. The fate of Arcanum hangs in the balance.
    Session Highlights:
    The players seek out allies within the resistance against Blackthorn's plans.
    They gather materials and knowledge to seal the rifts and prevent the Eclipse Serpent's arrival.
    In a final showdown, the players confront Blackthorn atop an ancient spire as the dimensions tremble.
    Session 5: Eclipse's End
    The campaign reaches its climax as the players face the Eclipse Serpent in a realm where light and shadow merge. They must prevent the serpent's emergence and restore the cosmic balance.
    Session Highlights:
    The players navigate through a shifting landscape of light and shadow, solving puzzles to weaken the Eclipse Serpent.
    They engage in a multi-phase battle, using their abilities and teamwork to exploit weaknesses.
    With the help of their allies and the knowledge they've gained, the players seal the rifts and banish the Eclipse Serpent back to the Shadow Plane.
    Conclusion:
    The campaign ends with the players hailed as heroes who saved Arcanum from the brink of darkness. The dimensional rifts close, but mysteries of the Shadow Plane and the enigmatic Orlan Blackthorn remain. The Arcane Defenders have made their mark, ready to face new challenges and explore the uncharted corners of their world.
    This example campaign, "Shadows of Arcanum," blends elements of steampunk and arcane fantasy, introducing a unique setting and a central conflict involving dimensional rifts and shadowy entities. The campaign's progression follows the players' journey from investigating a single rift to facing a cosmic threat."""

SPAWNPLACESLIST = ["a small Tavern", "a large Tavern", "in the Center of town", "in a small rest stop"]

TownPrefixlist = [
    "Whispering",
    "Gloomy",
    "Silver",
    "Golden",
    "Mystic",
    "Haunted",
    "Ancient",
    "Enchanted",
    "Cursed",
    "Radiant",
    "Lost",
    "Eternal",
    "Forgotten",
    "Emerald",
    "Sapphire",
    "Ruby",
    "Diamond",
    "Shadow",
    "Crystal",
    "Rusty",
    "Iron",
    "Wooden",
    "Sunny",
    "Moonlit",
    "Starlight",
    "Frozen",
    "Flaming",
    "Thundering",
    "Windy",
    "Stormy",
    "Dusty",
    "Whirling",
    "Foggy",
    "Serpent",
    "Dragon",
    "Phoenix",
    "Unicorn",
    "Lion",
    "Griffin",
    "Basilisk",
    "Dread",
    "Shimmering",
    "Grim",
    "Witch's",
    "Sorcerer's",
    "Alchemist's",
    "Black",
    "White",
    "Grey",
    "Mystical",
    "Shrouded",
    "Crimson",
    "Azure",
    "Jeweled",
    "Glimmering",
    "Ethereal",
    "Twin",
    "Hidden",
    "Ravens'",
    "Owls'",
    "Foxes'",
    "Wolves'",
    "Bears'",
    "Eagles'",
    "Hawks'",
    "Ravens'",
    "Owls'",
    "Foxes'",
    "Wolves'",
    "Bears'",
    "Eagles'",
    "Hawks'",
    "Elven",
    "Dwarven",
    "Halfling",
    "Gnomish",
    "Orcish",
    "Trollish",
    "Goblin",
    "Kobold",
    "Undead",
    "Fey",
    "Elemental",
    "Celestial",
    "Infernal",
    "Abyssal",
    "Underdark",
    "High",
    "Low",
    "Middle",
    "Outer",
    "Inner",
    "Rustic",
    "Coastal",
    "Mountain",
    "Swampy",
    "Desert",
    "Frozen",
    "Volcanic",
    "Underwater",
]

TownSuffixlist = [
    "Haven",
    "Vale",
    "Meadow",
    "Hill",
    "Glen",
    "Wood",
    "Thorn",
    "Crossing",
    "Ford",
    "Bridge",
    "Harbor",
    "Port",
    "Market",
    "Square",
    "Bazaar",
    "Plaza",
    "Borough",
    "Quarter",
    "Hamlet",
    "Village",
    "Town",
    "City",
    "Keep",
    "Fortress",
    "Castle",
    "Tower",
    "Cathedral",
    "Sanctuary",
    "Chapel",
    "Shrine",
    "Temple",
    "Mausoleum",
    "Grave",
    "Crypt",
    "Cemetery",
    "Grove",
    "Gardens",
    "Orchard",
    "Forest",
    "Woods",
    "Jungle",
    "Swamp",
    "Marsh",
    "Wetlands",
    "Tundra",
    "Desert",
    "Sands",
    "Cliffs",
    "Falls",
    "Ravine",
    "Canyon",
    "Foothills",
    "Mountains",
    "Peaks",
    "Summit",
    "Pass",
    "Ridge",
    "Glacier",
    "Volcano",
    "Crater",
    "Cave",
    "Tunnel",
    "Mines",
    "Cavern",
    "Labyrinth",
    "Chasm",
    "Gulf",
    "Bay",
    "Lagoon",
    "Lake",
    "River",
    "Stream",
    "Brook",
    "Pond",
    "Falls",
    "Island",
    "Atoll",
    "Peninsula",
    "Coast",
    "Shore",
    "Haven",
    "Haven",
    "Refuge",
    "Retreat",
    "Oasis",
    "Waters",
    "Wharf",
    "Docks",
    "Boathouse",
    "Shipyard",
    "Harbor",
    "Inn",
    "Tavern",
    "Hall",
    "Lodge",
    "Manor",
    "Estate",
    "House",
    "Hovel",
    "Hut",
    "Shack",
]

starting_town = random.choice(TownPrefixlist) + random.choice(TownSuffixlist)

map_feature_list = ["town", "cave", "Forrest clearing", "city", "Swamp", "Swamp Hut", "Village", "Ocean", "Pirate Ship",
                    "Ship", "Ship Wreck", "Floating Island", "Flying Pirate Ship", "Mineshaft", "Underwater Ravine",
                    "Underwater Ravine With Glowing algae on the walls and floor", "Ravine"]

tts = "yes"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def start():
    global tts
    global tts_enabled
    print("The Default Options are in Capital letters")
    tts = input("enable TTS Yes Or no (Y/n): ")
    tts = tts.lower()
    tts = tts.strip()
    if tts == "yes" or tts == "y":
        print(
            "Warning This Uses a Google AI so it has limits. (This Uses Text To Speech) and saving campaigns is currently not available")
        TTSmodule(
            "Warning This Uses a Google AI so it has limits. (This Uses Text To Speech) and saving campaigns is currently not available. Please Press Enter To Start")
    elif tts == "no" or tts == "n":
        print(
            "Warning This Uses a Google AI so it has limits. and saving campaigns is currently not available")
        tts_enabled = False
    elif tts == "":
        print(
            "Warning This Uses a Google AI so it has limits. (This Uses Text To Speech) and saving campaigns is currently not available")
        TTSmodule(
            "Warning This Uses a Google AI so it has limits. (This Uses Text To Speech) and saving campaigns is currently not available. Please Press Enter To Start")
    else:
        print(
            f"The answer you've provided is not a valid answer please try again.\nProvided answer {tts}, valid answers are Yes or No")
        start()


start()
start_input = input("Please Press Enter To Start: ")


def DM_Block():
    campaign_prompt = f"You are the DM for a DND 5e campaign. Never Act as the players or party. Here are the rules: {dnd5erules}."
    campaign_prompt += f"Make sure your answers are short. because its player lead so introduce the environment"
    campaign_prompt += f"If Homebrew content is allowed, use it wisely. DM information: {DMExt}."
    campaign_prompt += f"Test Mode: {'Yes' if testmodevar else 'No'}."
    campaign_prompt += f"Starting town: {starting_town}."
    campaign_prompt += f"Combat rules and example: {dndCombatrulesandexample}."
    campaign_prompt += f"How to generate town names add one of the prefixes {TownPrefixlist} to one of the Suffixes {TownSuffixlist}."
    campaign_prompt += f"(Make sure You do this) Random starting place: {random.choice(SPAWNPLACESLIST)}."
    campaign_prompt += (f"first use the starting town, then generate a new map feature after the party moves a good "
                        f"amount of distance away from the last map feature from the list")
    campaign_prompt += f"{map_feature_list}. "
    campaign_prompt += (f"Make sure your answers are super short. because its player lead so introduce the "
                        f"environment. dont move the party away from the starting town unless they say they want to "
                        f"move away from the party. your just the dm not the party the party will respond on its "
                        f"own.")
    campaign_prompt += (f"You are the DM for a DND 5e campaign (Your only a DM not a Player. dont use the 'Player:' or "
                        f"the 'Party:' name tags How ever if your acting out a NPC your alowed to use the npcs name "
                        f"before he says words).")
    campaign_prompt += (f"Your allowed to kill off characters, when all of the party is dead say (End Campaign). "
                        f"remember Never Act as the players or party. and describe the scene without moving the "
                        f"characters")
    print(campaign_prompt)
    print("""\n
    DnD Game Start
    \n""")

    response = textGen(campaign_prompt)

    if response:
        print(response)
        if tts_enabled:
            TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
            message_prompts.append(response)  # Store the response

    while True:
        player_input = input("What do you do? ")

        response = textGen(
            f"Master Prompt (contains all info that made the first prompt) Remember to follow the instructions set in this prompt: {campaign_prompt}'', you will continue the story based on the last prompts. The last prompts were {message_prompts}.The Player responds with: {player_input}")

        if response:
            message_prompts.append(f"The Player responds with: {player_input}")
            message_prompts.append(response)  # Store the response
            print(response)
            if tts_enabled:
                TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
        else:
            print("No text received from the API.")


def NPC_Block():
    print("""
        Please put the NPC Stats Like this
        Name:"Name", Max_HP:"Number", Current_HP:"Number", Level:"1", Race:"DND Race", Class:"Class", Pronoun:""
        If the Current Hp is Not there or blank it will set The max hp as the current hp
        """)
    npc_name = input("Add the NPCs, Name: ")
    npc_max_hp = input("Add the NPCs, Max Hp: ")
    npc_current_hp = input("Add the NPCs, Current Hp: ")
    npc_level = input("Add the NPCs, Level: ")
    npc_race = input("Add the NPCs, Race: ")
    npc_class = input("Add the NPCs, Class: ")
    npc_pronoun = input("Add the NPCs, Pronoun: ")
    npc_town = input("Add the NPCs, Town: ")
    npc_quests = input("Add the NPCs, Quest: ")
    npc_quests_disc = input("Add the NPCs, Quest description: ")
    campaign_prompt = f"You are an NPC in a DND 5e campaign. Here are your stats: "
    campaign_prompt += f"Name: {npc_name}, Max HP: {npc_max_hp}, Current HP: {npc_current_hp}, Level: {npc_level}, Race: {npc_race}, Class: {npc_class}, Pronoun: {npc_pronoun}."
    campaign_prompt += f"Make sure your answers are short, as your an NPC in this campaign"
    campaign_prompt += f"Your in town: {npc_town}."
    campaign_prompt += f"Combat rules and example, You may need these to defend yourself: {dndCombatrulesandexample}."
    campaign_prompt += f"How to generate town names add one of the prefixes {TownPrefixlist} to one of the Suffixes {TownSuffixlist}."
    campaign_prompt += f"You give the quest called {npc_quests}, the description of the quest is {npc_quests_disc}."
    campaign_prompt += f"You are an NPC in a DND 5e campaign. Act accordingly."
    campaign_prompt += f"Say Hello to the party and introduce yourself and wait for the party's response."
    print(campaign_prompt)
    response = textGen(campaign_prompt)
    if response:
        print(response)
        message_prompts.append(response)  # Store the response
        if tts_enabled:
            TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
        else:
            print("No text received from the API.")

        while True:
            party_input = input("What Is the Parties responce: ")
            party_input = f"the Parties Responds is: {party_input}"

            response = textGen(
                f"Master Prompt (contains all info that made the first prompt) Remember to follow the instructions set in this prompt: {campaign_prompt}'', you will continue the story based on the last prompts. The last prompts were {message_prompts}.The Player responds with: {party_input}")
            if response:
                message_prompts.append(party_input)
                message_prompts.append(response)  # Store the response
                print(response)
                if tts_enabled:
                    TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
            else:
                print("No text received from the API.")


def PC_Block():
    global tts_enabled
    roll1 = random.randint(1, 18)
    roll2 = random.randint(1, 18)
    roll3 = random.randint(1, 18)
    roll4 = random.randint(1, 18)
    roll5 = random.randint(1, 18)
    roll6 = random.randint(1, 18)

    masterprompt = f"""Your are acting as a player character (Not a DM) in a dnd campain.
        Combat rules and example, You will need these to defend yourself: {dndCombatrulesandexample}, this data is only for example don't use it for making your player character.
        Keep Your answers short ask for a roll and the dm will tell you what you rolled and you will start by saying your player sheet and asking when to start and then the dm will set the scene.
        remember you are not the dm
        heres what rolls you have to assign to the following stats, STATS: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, ROLLS: {roll1}, {roll2}, {roll3}, {roll4}, {roll5}, {roll6}
        do not generate any story you are only a player character"""
    print(masterprompt)
    response = textGen(masterprompt)
    if response:
        print(response)
        message_prompts.append(response)  # Store the response
        if tts_enabled:
            TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
        else:
            print("No text received from the API.")

        while True:
            DM_input = input("What do you do? ")

            response = textGen(
                f"master prompt: {masterprompt}. previous responses: {message_prompts}. the DM responds with {DM_input}")

            if response:
                message_prompts.append(f"The DM responds with: {DM_input}")
                message_prompts.append(response)  # Store the response
                print(response)
                if tts_enabled:
                    TTSmodule(response + " What Do You Do?")  # You can still use TTS if needed
            else:
                print("No text received from the API.")


if __name__ == "__main__":
    # Define the choices
    choices = [
        inquirer.List(
            "ai",
            message="Select an AI mode",
            choices=[
                ("AI DM", DM_Block),
                ("AI PC", PC_Block),
                ("AI NPC (WIP)", NPC_Block),
            ],
        ),
    ]

    answers = inquirer.prompt(choices)
    # Execute the selected function
    selected_function = answers["ai"]
    selected_function()
