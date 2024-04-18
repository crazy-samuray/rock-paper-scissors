import random
import pygame
import sys

#pygame i başlat
pygame.init()
#ekran boyutları
WIDTH,HEIGHT=800,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Taş Kağıt Makas Oyunu")#title ayarla

#renkler
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#game loop=oyun döngüsü
#oyun başlar, oyun skor toplamak için oynanır,oyun biter

#fontlar
FONT=pygame.font.SysFont(None,50)

def draw_text(text,font,color,x,y):
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.center=(x,y)
    WIN.blit(text_surface,text_rect)

def draw_winner(winner_text):
    WIN.fill(WHITE)
    draw_text(winner_text,FONT,BLACK,WIDTH//2,HEIGHT//2)
    pygame.display.update()
    pygame.time.delay(2000)

def main(): #ana oyun kodları
    run=True
    
    while run:
        WIN.fill(WHITE)
        draw_text("Taş Kağıt Makas Oyunu ",FONT,BLACK,WIDTH//2,50)
        draw_text("Seçiminizi yapın: ",FONT,BLACK,WIDTH//2,150)

        #oyuncu seçimini göstermek için butonlar
        rock_button=pygame.Rect(50,200,200,100)
        paper_button=pygame.Rect(300,200,200,100)
        scissors_button=pygame.Rect(550,200,200,100)

        pygame.draw.rect(WIN,RED,rock_button)
        pygame.draw.rect(WIN,GREEN,paper_button)
        pygame.draw.rect(WIN,BLUE,scissors_button)
        
        draw_text("Taş",FONT,WHITE, rock_button.centerx, rock_button.centery)
        draw_text("Kağıt",FONT,WHITE, paper_button.centerx, paper_button.centery)
        draw_text("Makas",FONT,WHITE, scissors_button.centerx, scissors_button.centery)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUİT:
                run=False
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if rock_button.collidepoint(x,y):
                    user_choice="taş"
                elif paper_button.collidepoint(x,y):
                    user_choice="kağt"
                elif scissors_button.collidepoint(x,y):
                    user_choice="makas" 
                else:
                    user_choice=None

                if user_choice:
                    choices=["taş","kağıt","makas"]
                    computer_choice=random.choice(choices)

                    if user_choice==computer_choice:
                        draw_winner("Berabere!")
                    elif (user_choice=="taş" and computer_choice=="makas")or\
                         (user_choice=="kağıt" and computer_choice=="taş")or\
                         (user_choice=="makas" and computer_choice=="kağıt"):
                        draw_winner("Kazandınız")
                    else:
                        draw_winner("Kaybettiniz")

if __name__ =="__main__":
   main()