import random
import pygame
import sys
import os

#pygame'i başlat
pygame.init()
#ekran boyutları
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taş Kağıt Makas Oyunu")#title ayarla

#renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#fontlar
FONT = pygame.font.SysFont(None, 50)

def resize_image(image, scale_factor):
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))


# Dosya yolları
CURRENT_PATH = os.path.dirname(__file__)
ROCK_IMG = pygame.image.load(os.path.join(CURRENT_PATH, 'C://Users//Monster1//Desktop//projeler//python dersleri//tas_kagıt_makas//kaya.png'))
PAPER_IMG = pygame.image.load(os.path.join(CURRENT_PATH, 'C://Users//Monster1//Desktop//projeler//python dersleri//tas_kagıt_makas//kagit.png'))
SCISSORS_IMG = pygame.image.load(os.path.join(CURRENT_PATH, 'C://Users//Monster1//Desktop//projeler//python dersleri//tas_kagıt_makas//makas.png'))

    # Görüntüleri yeniden boyutlandır

# ROCK_IMG = pygame.transform.scale(ROCK_IMG, (70,70))
# PAPER_IMG = pygame.transform.scale(PAPER_IMG, (70,70))
# SCISSORS_IMG = pygame.transform.scale(SCISSORS_IMG, (70,70))
ROCK_IMG = resize_image(ROCK_IMG, 0.1)
PAPER_IMG = resize_image(PAPER_IMG, 0.1)
SCISSORS_IMG = resize_image(SCISSORS_IMG,0.1)
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    WIN.blit(text_surface, text_rect)

def draw_winner(winner_text):
    WIN.fill(WHITE)
    draw_text(winner_text, FONT, BLACK, WIDTH//2, HEIGHT//2)
    pygame.display.update()
    pygame.time.delay(2000)

def main(): #ana oyun kodları
    run = True
    user_score = 0
    computer_score = 0
    rounds = 3
    
    while run:
        WIN.fill(WHITE)
        draw_text("Taş Kağıt Makas Oyunu", FONT, BLACK, WIDTH//2, 50)
        draw_text("Seçiminizi yapın:", FONT, BLACK, WIDTH//2, 150)

        #oyuncu seçimini göstermek için butonlar
        rock_button = pygame.Rect(50, 200, 200, 100)
        paper_button = pygame.Rect(300, 200, 200, 100)
        scissors_button = pygame.Rect(550, 200, 200, 100)

        pygame.draw.rect(WIN, RED, rock_button)
        pygame.draw.rect(WIN, GREEN, paper_button)
        pygame.draw.rect(WIN, BLUE, scissors_button)
        
        WIN.blit(ROCK_IMG, (rock_button.centerx - ROCK_IMG.get_width()//2, rock_button.centery - ROCK_IMG.get_height()//2))
        WIN.blit(PAPER_IMG, (paper_button.centerx - PAPER_IMG.get_width()//2, paper_button.centery - PAPER_IMG.get_height()//2))
        WIN.blit(SCISSORS_IMG, (scissors_button.centerx - SCISSORS_IMG.get_width()//2, scissors_button.centery - SCISSORS_IMG.get_height()//2))

        draw_text(f"Oyuncu: {user_score} - Bilgisayar: {computer_score}", FONT, BLACK, WIDTH//2, 400)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if rock_button.collidepoint(x, y):
                    user_choice = "taş"
                elif paper_button.collidepoint(x, y):
                    user_choice = "kağıt"
                elif scissors_button.collidepoint(x, y):
                    user_choice = "makas" 
                else:
                    user_choice = None

                if user_choice:
                    choices = ["taş", "kağıt", "makas"]
                    computer_choice = random.choice(choices)

                    if user_choice == computer_choice:
                        draw_winner("Berabere!")
                    elif (user_choice == "taş" and computer_choice == "makas") or\
                         (user_choice == "kağıt" and computer_choice == "taş") or\
                         (user_choice == "makas" and computer_choice == "kağıt"):
                        draw_winner("Kazandınız")
                        user_score += 1
                    else:
                        draw_winner("Kaybettiniz")
                        computer_score += 1

                    rounds -= 1
                    if rounds == 0:
                        if user_score > computer_score:
                            draw_winner("Oyun Bitti. Kazandınız!")
                        elif user_score < computer_score:
                            draw_winner("Oyun Bitti. Kaybettiniz!")
                        else:
                            draw_winner("Oyun Bitti. Berabere!")
                        run = False

if __name__ == "__main__":
    main()