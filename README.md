# samurai-quest
A simple Zelda-like RPG game created using the pygame package.

At current stage the game shows a player-icon moving through a terrain map with collideable trees and rocks. The player cannot leave the map or step into the water. The camera follows the player-icon.

I'm using the pygame package and the map-creator software Tiled. The tileset I used is NinjaAdventure from Pixel Boy: https://pixel-boy.itch.io/ninja-adventure-asset-pack


** Recent fixes: **
- corrected offset of trees
- added functions to read attack and magic inputs
- about to introduce player states in the game

** Current problems: **
- sometimes when colliding the main character changes position on the map
- the attack animation doesn't seem to work well