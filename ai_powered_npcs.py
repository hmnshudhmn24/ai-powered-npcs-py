import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NPC_SPEED = 2
AVOID_RADIUS = 50

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI-Powered NPCs")
clock = pygame.time.Clock()

class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = random.randint(0, WIDTH)
        self.target_y = random.randint(0, HEIGHT)
        self.color = BLUE

    def move(self, npcs):
        # Avoid other NPCs
        for npc in npcs:
            if npc == self:
                continue
            dist = math.hypot(self.x - npc.x, self.y - npc.y)
            if dist < AVOID_RADIUS:
                self.target_x = random.randint(0, WIDTH)
                self.target_y = random.randint(0, HEIGHT)

        # Move towards target
        if abs(self.x - self.target_x) < NPC_SPEED:
            self.target_x = random.randint(0, WIDTH)
        else:
            self.x += NPC_SPEED if self.x < self.target_x else -NPC_SPEED

        if abs(self.y - self.target_y) < NPC_SPEED:
            self.target_y = random.randint(0, HEIGHT)
        else:
            self.y += NPC_SPEED if self.y < self.target_y else -NPC_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Create NPCs
npcs = [NPC(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(5)]

# Main loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for npc in npcs:
        npc.move(npcs)
        npc.draw(screen)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
