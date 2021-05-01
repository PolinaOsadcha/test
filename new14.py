import sys, pygame, time, random
pygame.init()

size = width, height = 320, 240
speed = [10, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
rab1 = pygame.image.load("rabbit.jpg")
rab1rect = rab1.get_rect()
presscount = 0
rab1_pos = [0,0]
rab1_spawn = True

while 1:
    time.sleep(0.003)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              speed[0] = 1
              speed[1] = 0
          elif event.key == pygame.K_LEFT:
              speed[0] = -1
              speed[1] = 0
          elif event.key == pygame.K_UP:
              speed[1] = -1
              speed[0] = 0
          elif event.key == pygame.K_DOWN:
              speed[1] = 1
              speed[0] = 0
          elif event.key == pygame.K_ESCAPE or event.key == ord('q'):
              pygame.quit()
              sys.exit()
          presscount += 1 
          if presscount == 5:
             presscount = 0
             rab1rect.update(random.randint(0, width), random.randint(0, height), rab1rect.width, rab1rect.height)
           #  rab1rect = rab1rect.move_ip(100,100)
      if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(rab1, rab1rect)
    pygame.display.flip()