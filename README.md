# samurai-quest
A simple Zelda-like RPG game created using the pygame package.

At current stage the game shows:
- A terrain map
- collideable objects and boundaries (the player cannot leave the map or step into water)
- a player icon which is animated during actions
- the player is able to attack
- the player is able to cast magic
- the player can switch between 2 weapons (katana and lance), the selected weapon is showed in a box, which is higlighted when the weapon is changed.
- the player can switch between 2 spells (thunder and heal), the selected weapon/spell is showed in its relative box, which is highlighted when the weapon/spell is changed.
- health and energy bar appears on top left of the screen (with colors)
- XPs appear on the bottom right of the screen
- the player posesses game statistics
- the player can inflict damages to enemies and get damaged by enemies
- the enemies move towards the player when he enters their notice radius, and attack him when he enters their attack radius; when they attack an attack animation ensues
- the player and the enemies flicker when hit
- the enemy vanishes in smoke when its health goes to 0

## Latest updates
- the player can cast a healing spell (with animation) that increases the helth bar by consuming energy from the energy bar
- the energy bar slowly recovers

I'm using the pygame package and the map-creator software Tiled. The tileset, characters and fonts I used I've taken from NinjaAdventure by Pixel Boy: https://pixel-boy.itch.io/ninja-adventure-asset-pack