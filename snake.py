import pygame, sys, time, random #gerekli modülleri importluyoruz, Alt alta import da açabilirsiniz fakat böyle daha basit.



# BASİT BİR YILAN OYUNU PROJESİ, KENDİMİ GELİŞTİRMEK VE EĞLENMEK AMACIYLA KODLADIM.
# GELİŞTİREBİLİR VEYA ALIŞTIRMALAR YAPABİLİRSİNİZ.


speed = 8 #yılanın gidiş hızı.

#açılan pencere boyutları

frame_size_x = 1000
frame_size_y= 600


check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Hata " + check_errors[1])
else:
    print("Oyun Başarılı Şekilde Çalıştırıldı.")
    
#açılan ekranın içine oyunu yerleştirme

pygame.display.set_caption("Kayess Snake Project")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)


fps_controller = pygame.time.Clock()
# yılan kutusunun büyüklüğü
square_size = 30

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
                random.randrange(1,(frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0
    
init_vars()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Skor: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 18, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    
    game_window.blit(score_surface, score_rect)
    

#oyun döngü kısmı

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ( event.key == pygame.K_UP or event.key == ord("w") 
                and direction != "DOWN"):
                direction = "UP"
            elif  ( event.key == pygame.K_DOWN or event.key == ord("s") 
                and direction != "UP"):
                direction = "DOWN"
            elif  ( event.key == pygame.K_LEFT or event.key == ord("a") 
                and direction != "RIGHT"):
                direction = "LEFT"
            elif  ( event.key == pygame.K_RIGHT or event.key == ord("d") 
                and direction != "LEFT"):
                direction = "RIGHT"
    
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size
        
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0
        
    #elma toplama kısmı
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # elma spawnlama
    if not food_spawn:
        food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
            random.randrange(1,(frame_size_y // square_size)) * square_size]
        food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            square_size -2, square_size -2 ))
        
    pygame.draw.rect(game_window,red, pygame.Rect(food_pos[0], 
                    food_pos[1], square_size, square_size))
    
    # oyun kaybedince olacak işlemler

    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()

    show_score(1,white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)
