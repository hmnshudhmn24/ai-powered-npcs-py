# AI-Powered NPCs

## Overview
This project implements AI-driven NPCs (Non-Player Characters) that move intelligently within a 2D environment. The NPCs navigate towards random targets while also avoiding other NPCs to prevent clustering.

## Features
- AI-driven movement for NPCs
- Random target selection for each NPC
- Avoidance mechanism to prevent NPCs from clustering
- Real-time movement and interaction simulation using Pygame

## Requirements
- Python 3.8+
- Pygame

## Installation
1. Install dependencies:
```sh
pip install pygame
```
2. Clone the repository:
```sh
git clone https://github.com/yourusername/ai-powered-npcs.git
cd ai-powered-npcs
```

## Running the Program
Run the following command:
```sh
python ai_powered_npcs.py
```

## How It Works
- Each NPC moves towards a randomly assigned target.
- If an NPC detects another NPC within a defined radius, it changes its target to avoid collision.
- The NPCs continuously update their targets and positions to create dynamic movement.
- The environment is displayed using Pygame.

## License
This project is open-source and free to use.
