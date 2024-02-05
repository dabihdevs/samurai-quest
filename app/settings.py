WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64 # pixels offset

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/NormalFont.ttf'
UI_FONT_SIZE = 18

# General colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# UI colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# Weapons
weapon_data = {'Katana': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/Katana/full.png'},
               'Lance': {'cooldown': 120, 'damage': 20, 'graphic': '../graphics/weapons/Lance/full.png'}}

# Magic
magic_data = {
    'shuriken': {'strength': 5, 'cost': 20, 'graphic':'../graphics/particles/magic_shuriken/frames/0.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic':'../graphics/particles/heal/heal_full.png'}
}

# Monsters
monster_data = {
    'Beast': {'health': 200, 'exp':100, 'damage': 30, 'attack_type': 'claw', 'attack_sound': "", 'speed': 2, 'resistance': 5, 'attack_radius': 50, 'notice_radius': 200},
    'Ghost': {'health': 200, 'exp':100, 'damage': 30, 'attack_type': 'claw', 'attack_sound': "", 'speed': 2, 'resistance': 5, 'attack_radius': 50, 'notice_radius': 200},
    'Cyclope': {'health': 200, 'exp':100, 'damage': 30, 'attack_type': 'claw', 'attack_sound': "", 'speed': 2, 'resistance': 5, 'attack_radius': 50, 'notice_radius': 200},
    'Reptile': {'health': 200, 'exp':100, 'damage': 30, 'attack_type': 'claw', 'attack_sound': "", 'speed': 2, 'resistance': 5, 'attack_radius': 50, 'notice_radius': 200}
}