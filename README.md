# samurai-quest
A simple Zelda-like RPG game created using the pygame package.

At current stage the game shows:
- A terrain map
- collideable objects and boundaries (the player cannot leave the map or step into water)
- a player icon which is animated during actions
- the player is able to attack
- the player is able to cast magic
- the player can switch between 2 weapons (katana and lance), the selected weapon is showed in a box, which is higlighted when the weapon is changed.
- the player can switch between 2 spells (thunder and heal), the selected weapon/spell is showed in its relative box, which is higlighted when the weapon/spell is changed.
- health and energy bar appears on top left of the screen (with colors)
- XPs appear on the bottom right of the screen
- the player posesses game statistics

## Recent updates
- added entity class from which both Player and Enemy class inherit the functions move() and collision()
- created Enemy class
- now the enemies are displayed on the terrain and move towards the player when the player comes within their notice radius; they are animated but not collideable yet
- the program crushes when enemies attack because attack animation is not available yet
- when the player's weapon collides with the enemies, the enemies disappear

I'm using the pygame package and the map-creator software Tiled. The tileset, characters and fonts I used I've taken from NinjaAdventure by Pixel Boy: https://pixel-boy.itch.io/ninja-adventure-asset-pack