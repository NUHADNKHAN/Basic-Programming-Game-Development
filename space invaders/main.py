import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Create a Pygame window with a size of 500x500 pixels
screen = pygame.display.set_mode((500, 500))

# Load the icon image
icon = pygame.image.load("icon.png")

# Set the window icon
pygame.display.set_icon(icon)

# Set the window title
pygame.display.set_caption("Space Invaders")

# Load background image
backgroundIMG = pygame.image.load("background.jpg")

# Load player image
playerIMG = pygame.image.load("spaceship.png")
playerX = 200
playerY = 400
playerX_change = 0  # Initialize player X change

# Load alien image
alienIMG = pygame.image.load("alien.png")
alienX = random.randint(0, 436)  # Random initial X position of the alien
alienY = 50   # Initial Y position of the alien
alienX_change = 0.2  # Initial X change for alien movement
alienY_change = 5    # Initial Y change for alien movement
alien_direction = 2  # 1 for right, -1 for left

# Define player speed
player_speed = 1

# Initialize player direction
player_direction = 0  # 0 for no movement, -1 for left, 1 for right

# Function to draw the player on the screen
def player(x, y):
    screen.blit(playerIMG, (x, y))

# Function to draw the alien on the screen
def alien(x, y):
    screen.blit(alienIMG, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_direction = -1  # Move left
            if event.key == pygame.K_RIGHT:
                player_direction = 1  # Move right

        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_direction = 0  # Stop movement when the left or right key is released

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(backgroundIMG, (0, 0))

    # Update player position based on direction
    playerX += player_direction * player_speed

    # Ensure the player stays within the screen boundaries
    if playerX < 0:
        playerX = 0
    elif playerX > 500 - 64:  # Assuming the player image is 64 pixels wide
        playerX = 500 - 64

    # Update alien position
    alienX += alien_direction * alienX_change

    # Check for alien boundary collision
    if alienX <= 0 or alienX >= 436:  # Adjust the value based on your alien image width
        alien_direction = -alien_direction
        alienY += alienY_change

    # Draw the player
    player(playerX, playerY)

    # Draw the alien
    alien(alienX, alienY)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()