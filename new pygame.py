import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect Points & Avoid Traps")

# Load and resize background image
background = pygame.image.load("bag.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and resize character image
character = pygame.image.load("character.jpg")
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50
character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

# Load point (coin) image
point = pygame.image.load("point.png")
POINT_SIZE = 30
point = pygame.transform.scale(point, (POINT_SIZE, POINT_SIZE))

# Load trap (dangerous point) image
trap = pygame.image.load("trap.png")
TRAP_SIZE = 40
trap = pygame.transform.scale(trap, (TRAP_SIZE, TRAP_SIZE))

# Load power-up (shield) image
power_up = pygame.image.load("power_up.png")  # Ensure this file exists
POWER_SIZE = 35
power_up = pygame.transform.scale(power_up, (POWER_SIZE, POWER_SIZE))

# Character position and speed
char_x = SCREEN_WIDTH // 2
char_y = SCREEN_HEIGHT // 2
char_speed = 5

# Point position (random)
point_x = random.randint(0, SCREEN_WIDTH - POINT_SIZE)
point_y = random.randint(0, SCREEN_HEIGHT - POINT_SIZE)

# Generate multiple traps (3 traps)
NUM_TRAPS = 3
traps = []
for _ in range(NUM_TRAPS):
    traps.append([random.randint(0, SCREEN_WIDTH - TRAP_SIZE), random.randint(0, SCREEN_HEIGHT - TRAP_SIZE)])

# Power-up position (random)
power_x = random.randint(0, SCREEN_WIDTH - POWER_SIZE)
power_y = random.randint(0, SCREEN_HEIGHT - POWER_SIZE)
power_active = False
power_timer = 0

# Timer
start_time = pygame.time.get_ticks()  # Game start time
TIME_LIMIT = 30  # Game ends after 30 seconds

# Score
score = 0
font = pygame.font.Font(None, 36)  # Font for text

# Game loop
running = True
while running:
    pygame.time.delay(30)

    # Calculate remaining time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, TIME_LIMIT - elapsed_time)

    # Check if time is up
    if remaining_time == 0:
        print("Time's Up! Final Score:", score)

        # Show game over message
        screen.fill((0, 0, 0))  # Black background
        game_over_text = font.render("Time's Up!", True, (255, 0, 0))
        final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 20))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 20))
        pygame.display.update()

        pygame.time.delay(2000)
        running = False  # End game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states (pressed or not)
    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT] and char_x > 0:
        char_x -= char_speed

    # Move right
    if keys[pygame.K_RIGHT] and char_x < SCREEN_WIDTH - CHARACTER_WIDTH:
        char_x += char_speed

    # Move up
    if keys[pygame.K_UP] and char_y > 0:
        char_y -= char_speed

    # Move down
    if keys[pygame.K_DOWN] and char_y < SCREEN_HEIGHT - CHARACTER_HEIGHT:
        char_y += char_speed

    # Check collision with the point
    if (char_x < point_x + POINT_SIZE and char_x + CHARACTER_WIDTH > point_x and
            char_y < point_y + POINT_SIZE and char_y + CHARACTER_HEIGHT > point_y):
        score += 1  # Increase score
        print("Score:", score)

        # Move the point to a new random location
        point_x = random.randint(0, SCREEN_WIDTH - POINT_SIZE)
        point_y = random.randint(0, SCREEN_HEIGHT - POINT_SIZE)

        # Move the traps to new random locations
        traps = [[random.randint(0, SCREEN_WIDTH - TRAP_SIZE), random.randint(0, SCREEN_HEIGHT - TRAP_SIZE)] for _ in
                 range(NUM_TRAPS)]

    # Check collision with power-up
    if (char_x < power_x + POWER_SIZE and char_x + CHARACTER_WIDTH > power_x and
            char_y < power_y + POWER_SIZE and char_y + CHARACTER_HEIGHT > power_y):
        power_active = True
        power_timer = pygame.time.get_ticks()  # Start shield timer
        print("Shield Activated!")

        # Move power-up to a new random location
        power_x = random.randint(0, SCREEN_WIDTH - POWER_SIZE)
        power_y = random.randint(0, SCREEN_HEIGHT - POWER_SIZE)

    # Check if power-up time has expired
    if power_active and pygame.time.get_ticks() - power_timer > 5000:  # 5 seconds
        power_active = False
        print("Shield Expired!")

    # Check collision with traps (game over if no shield)
    for trap_x, trap_y in traps:
        if (char_x < trap_x + TRAP_SIZE and char_x + CHARACTER_WIDTH > trap_x and
                char_y < trap_y + TRAP_SIZE and char_y + CHARACTER_HEIGHT > trap_y):

            if not power_active:  # Game over if shield is not active
                print("Game Over! Final Score:", score)

                # Show game over message
                screen.fill((0, 0, 0))  # Black background
                game_over_text = font.render("Game Over!", True, (255, 0, 0))
                final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
                screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 20))
                screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 + 20))
                pygame.display.update()

                pygame.time.delay(2000)
                running = False  # End game

    # Draw everything
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(character, (char_x, char_y))  # Draw character
    screen.blit(point, (point_x, point_y))  # Draw point

    # Draw multiple traps
    for trap_x, trap_y in traps:
        screen.blit(trap, (trap_x, trap_y))

    # Draw power-up
    screen.blit(power_up, (power_x, power_y))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw timer
    timer_text = font.render(f"Time: {remaining_time}s", True, (255, 255, 255))
    screen.blit(timer_text, (SCREEN_WIDTH - 120, 10))

    pygame.display.update()  # Refresh screen

# Quit pygame
pygame.quit()
