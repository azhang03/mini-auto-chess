# Autochess Console Game

## Overview
This project is a simple **Autochess-style game** implemented in Python and played via the console. You face off against three bots.

For those who haven't played something like this before, each round, players refresh a shop to purchase units, arrange their field, and battle against opponents. Units can be upgraded by combining duplicates, and players earn gold based on their performance each round.

---

## To-do
- **Dynamic Shop**: Players  refresh the shop to discover new units to purchase.
- **Unit Star Upgrades**: Combine duplicate units to increase their star level and enhance their stats.
- **Turn-Based Combat**: Players line up their units to fight opponents.
- **Progression System**: Gradually increase the number of units that can be fielded as the game progresses.
- **Resource Management**: Earn gold through wins or losses and allow for spending to build a team.

---

## Gameplay Rules to Implement
1. **Shop Refresh**: Each round, the shop presents 3 random units. Players can refresh the shop up to 5 times per round.
2. **Unit Placement**: Players can arrange units from their bench (max 5 slots) to their field (starting with 1 slot, max of 4 slots as the game progresses).
3. **Unit Upgrades**: Collect 2 copies of the same unit to upgrade its star level and stats.
4. **Combat**: Units battle based on their arrangement. Each unit attacks the opposing unit directly in front of it.
5. **Rewards**: Winning a round grants 10 gold, while losing grants 5 gold.
6. **Win Condition**: The last player standing wins the game.


