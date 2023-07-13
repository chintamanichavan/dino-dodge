import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Dinosaur character
DINO_WIDTH, DINO_HEIGHT = 64, 64
dino = pygame.Rect(WIDTH // 2, HEIGHT - DINO_HEIGHT - 50, DINO_WIDTH, DINO_HEIGHT)

# Dinosaur jumping
is_jumping = False
jump_count = 10

# Cactus obstacle
CACTUS_WIDTH, CACTUS_HEIGHT = 64, 64
cactus = pygame.Rect(WIDTH, HEIGHT - CACTUS_HEIGHT - 50, CACTUS_WIDTH, CACTUS_HEIGHT)

# Font for game over text
font = pygame.font.Font(None, 74)
game_over_text = font.render('GAME OVER', True, (255, 0, 0))

# Font for score
score_font = pygame.font.Font(None, 36)
score = 0

# Font for start screen
start_font = pygame.font.Font(None, 50)
start_text = start_font.render('Press any key to start', True, (0, 0, 0))

def show_start_screen():
    win.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                return

# Show start screen
show_start_screen()

# Game Loop
run = True
while run:
    pygame.time.delay(100)  # This will delay the game so it doesn't run too quickly

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # Detects keys that are currently being pressed
    if keys[pygame.K_SPACE]:
        is_jumping = True

    # Handle jumping
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Cactus movement
    cactus_speed = 5 + score // 100  # The speed increases with the score
    cactus.x -= cactus_speed
    if cactus.x < -CACTUS_WIDTH:
        cactus.x = WIDTH

    # Increase score
    score += 1

    # Collision detection
    if dino.colliderect(cactus):
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        run = False  # This will end the game when the dinosaur collides with the cactus

    # Fill the window with a white background
    win.fill((255, 255, 255))

    # Draw the dinosaur
    pygame.draw.rect(win, (0, 0, 0), dino)

    # Draw the cactus
    pygame.draw.rect(win, (0, 255, 0), cactus)

    # Display score
    score_text = score_font.render('Score: ' + str(score), True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
