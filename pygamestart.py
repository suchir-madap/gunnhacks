import pygame 
import sys 
import json
  
# initializing the constructor 

def start_screen():

    pygame.init() 
    clock  = pygame.time.Clock()
    screen  = pygame.display.set_mode([900,620])
    base_font = pygame.font.Font(None,32)
    user_text = ''
    bg = pygame.image.load("background.jpg")

    input_rect = pygame.Rect(400, 230, 140,32)
    color = pygame.Color('lightskyblue')
    green = (0, 30, 0)
    blue = (0, 0, 128)

    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Enter Zipcode Below', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (900 // 2, 300 // 2)


    counter = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or counter >0:
                zip_dict = {"zipcode": str(user_text)}
                json_dumping = json.dumps(zip_dict)
                with open("zipcode.json", "w") as outfile:
                    outfile.write(json_dumping)
                pygame.quit()
                sys.exit()
            

            if event.type == pygame.KEYDOWN:
                
                # if event.type == pygame.K_:
                #     zip_dict = {"zipcode": str(user_text)}
                #     json_dumping = json.dumps(zip_dict)
                #     with open("zipcode.json", "w") as outfile:
                #         outfile.write(json_dumping)
                    
                    
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.unicode.isdecimal():
                    user_text += event.unicode
        screen.fill((0,0,0))
        # background image
        screen.blit(bg,(0,0))
        screen.blit(text, textRect)
        
        # text box
        pygame.draw.rect(screen,color,input_rect, 2)
        text_surface = base_font.render(user_text, True, (0,0,0))
        screen.blit(text_surface,(input_rect.x +5 ,input_rect.y +5))
    
        pygame.display.flip()
        clock.tick(60)

start_screen()