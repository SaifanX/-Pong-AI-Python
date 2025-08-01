import pygame
pygame.init()


screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI Game')


BG_COLOR = (50, 25, 50)
WHITE = (255, 255, 255)


# Define font for displaying text
font = pygame.font.SysFont('Constantia', 30)


# Clock to control frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second
margin = 50
paddle_speed = 5
rect_width = 20
rect_height = 100
rect_y = (screen_height - rect_height) // 2


def draw_board():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, WHITE, (0, margin), (screen_width, margin), 2)  # Top margin line


# Function to draw text on the screen
def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))




class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)  # Paddle dimensions
        self.speed = 100  # Movement speed


    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 50:                        # Move up (prevent going above margin line area)
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:  # Move down (prevent going below screen)
            self.rect.y += self.speed


    def ai(self):
        # Move down
        if self.rect.centery < ball.rect.top and self.rect.bottom < screen_height:
            self.rect.y += paddle_speed


        # Move up
        if self.rect.centery > ball.rect.bottom and self.rect.top > margin:
            self.rect.y -= paddle_speed


    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)  # Draw paddle


# Ball class
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)  # Ball size
        self.speed_x = 10
        self.speed_y = -10


    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)


    def move(self):
        # check collision with top MARGIN
        if self.rect.top < margin:
            self.speed_y = -self.speed_y 
        # check collision with the bottom of the screen
        if self.rect.top > screen_height:
           self.speed_y = -self.speed_y 


        # Checks if the ball collides with the right paddle or left paddle.
        if self.rect.colliderect(right_paddle) or self.rect.colliderect(left_paddle):
            self.speed_x = -self.speed_x


        # Move ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y




right_paddle = Paddle(screen_width - 40, rect_y)
left_paddle = Paddle(20, rect_y)
ball = Ball(screen_width//2, screen_height//2)


# Game Over flag
game_over = False
winner_text = ""


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if not game_over:
        # Move player paddle
        right_paddle.move(pygame.K_UP, pygame.K_DOWN)


        draw_board()
        right_paddle.draw()
        left_paddle.draw()
        left_paddle.ai()
        ball.draw()
        ball.move()


        # Check if the ball is out of bounds (end game condition)
        if ball.rect.left < 0:  # Left player wins
            winner_text = 'PLAYER HAS WON, CPU HAS LOST'
            game_over = True
        if ball.rect.right > screen_width:  # Right player wins
            winner_text = 'PLAYER HAS LOST, CPU HAS WON'
            game_over = True


        draw_text('CPU: ', 20, 15)
        draw_text('P1: ', screen_width - 100, 15)
        draw_text('BALL SPEED: ' + str(abs(ball.speed_x)), screen_width // 2 - 100 , 15)


    # Display winner message if the game is over
    if game_over:
        draw_text(winner_text, 100, screen_height // 2 - 100)


    # Update display
    pygame.display.update()
    clock.tick(fps)  # Maintain FPS


pygame.quit()