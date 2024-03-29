# ADD ALL CONSTANTS HERE
# Rec. import as 'const':
#      import Cdb_Constants as const

TROOPS = {
    "Barbarian": "troops\\Troop_Barbarian.png",
    "Archer": "troops\\Troop_Archer.png",
    "Giant": "troops\\Troop_Giant.png",
    "Goblin": "troops\\Troop_Goblin.png",
    "Wall Breaker": "troops\\Troop_Wall_Breaker.png",
    "Balloon": "troops\\Troop_Balloon.png",
    "Wizard": "troops\\Troop_Wizard.png",
    "Healer": "troops\\Troop_Healer.png",
    "Dragon": "troops\\Troop_Dragon.png",
    "Pekka": "troops\\Troop_Pekka.png",
    "Baby Dragon": "troops\\Troop_Baby_Dragon.png",
    "Miner": "troops\\Troop_Miner.png",
    "Electro Dragon": "troops\\Troop_Electro_Dragon.png",
    "Root Rider": "troops\\Troop_Root_Rider.png", 
    "Yeti": "troops\\Troop_Yeti.png",
    "Dragon Rider": "troops\\Troop_Dragon_Rider.png",
    "Electro Titan": "troops\\Troop_Electro_Titan.png",
    "Minion": "troops\\Troop_Minion.png",
    "Hog Rider": "troops\\Troop_Hog_Rider.png",
    "Valkyrie": "troops\\Troop_Valkyrie.png",
    "Golem": "troops\\Troop_Golem.png",
    "Witch": "troops\\Troop_Witch.png",
    "Lava Hound": "troops\\Troop_Lava_Hound.png",
    "Bowler": "troops\\Troop_Bowler.png",
    "Ice Golem": "troops\\Troop_Ice_Golem.png",
    "Headhunter": "troops\\Troop_Headhunter.png",

    # Super Troops
    # 🐒🐒🐒 MAKE SURE YOU SEE WHAT THEY ARE CALLED ITS NOT ALL JUST SUPER🦍🦍🦍
    "Super Barbarian": "troops\\Troop_S_Barbarian.png",
    "Super Archer": "troops\\Troop_S_Archer.png",
    "Sneaky Goblin": "troops\\Troop_Sneaky_Goblin.png",  
    "Super Wall Breaker": "troops\\Troop_S_Wall_Breaker.png",
    "Super Giant": "troops\\Troop_S_Giant.png",
    "Rocket Balloon": "troops\\Troop_Rocket_Balloon.png",  
    "Super Wizard": "troops\\Troop_S_Wizard.png",
    "Super Dragon": "troops\\Troop_S_Dragon.png",
    "Inferno Dragon": "troops\\Troop_Inferno_Dragon.png",  
    "Super Minion": "troops\\Troop_S_Minion.png",
    "Super Valkyrie": "troops\\Troop_S_Valkyrie.png",
    "Super Witch": "troops\\Troop_S_Witch.png",
    "Ice Hound": "troops\\Troop_Ice_Hound.png",  

    # Siege Machines
    "Wall Wrecker": "troops\\Troop_Wall_Wrecker.png",
    "Battle Blimp": "troops\\Troop_Battle_Blimp.png",
    "Stone Slammer": "troops\\Troop_Stone_Slammer.png",
    "Siege Barracks": "troops\\Troop_Siege_Barracks.png",
    "Log Launcher": "troops\\Troop_Log_Launcher.png",
    "Flame Flinger": "troops\\Troop_Flame_Flinger.png", 
    "Battle Drill": "troops\\Troop_Battle_Drill.png",

    # Spells
    "Lightning Spell": "troops\\Spell_Lightning.png",
    "Heal Spell": "troops\\Spell_Heal.png",
    "Rage Spell": "troops\\Spell_Rage.png",
    "Jump Spell": "troops\\Spell_Jump.png",
    "Freeze Spell": "troops\\Spell_Freeze.png",
    "Clone Spell": "troops\\Spell_Clone.png",
    "Invisibility Spell": "troops\\Spell_Invisibility.png",
    "Recall Spell": "troops\\Spell_Recall.png",
    "Poison Spell": "troops\\Spell_Poison.png",
    "Earthquake Spell": "troops\\Spell_Earthquake.png",
    "Haste Spell": "troops\\Spell_Haste.png",
    "Skeleton Spell": "troops\\Spell_Skeleton.png",
    "Bat Spell": "troops\\Spell_Bat.png",
    "Overgrowth Spell": "troops\\Spell_Overgrowth.png"
}

# Composition of wtvr the current army is make sure we update this
currentArmy = {
    "Barbarian": 0,
    "Archer": 0,
    "Giant": 0,
    "Goblin": 0,
    "Wall Breaker": 0,
    "Balloon": 0,
    "Wizard": 0,
    "Healer": 0,
    "Dragon": 0,
    "Pekka": 0,
    "Baby Dragon": 0,
    "Miner": 0,
    "Electro Dragon": 0,
    "Root Rider": 0,
    "Yeti": 0,
    "Dragon Rider": 0,
    "Electro Titan": 0,
    "Minion": 0,
    "Hog Rider": 0,
    "Valkyrie": 0,
    "Golem": 0,
    "Witch": 0,
    "Lava Hound": 0,
    "Bowler": 0,
    "Ice Golem": 0,
    "Headhunter": 0,
    "Super Barbarian": 0,
    "Super Archer": 0,
    "Sneaky Goblin": 0,
    "Super Wall Breaker": 0,
    "Super Giant": 0,
    "Rocket Balloon": 0,
    "Super Wizard": 0,
    "Super Dragon": 0,
    "Inferno Dragon": 0,
    "Super Minion": 0,
    "Super Valkyrie": 0,
    "Super Witch": 0,
    "Ice Hound": 0,
    "Wall Wrecker": 0,
    "Battle Blimp": 0,
    "Stone Slammer": 0,
    "Siege Barracks": 0,
    "Log Launcher": 0,
    "Flame Flinger": 0,
    "Battle Drill": 0,
    "Lightning Spell": 0,
    "Heal Spell": 0,
    "Rage Spell": 0,
    "Jump Spell": 0,
    "Freeze Spell": 0,
    "Clone Spell": 0,
    "Invisibility Spell": 0,
    "Recall Spell": 0,
    "Poison Spell": 0,
    "Earthquake Spell": 0,
    "Haste Spell": 0,
    "Skeleton Spell": 0,
    "Bat Spell": 0,
    "Overgrowth Spell": 0
}


#we should probably add something that j like makes sure we are back on the home base screen (chat isnt open or the shop or wtvr)
isCOCOpen = False
isChatOpen = False

# statistics for fun
userAllTimeDonateCounter = 0 #increment with housing space



