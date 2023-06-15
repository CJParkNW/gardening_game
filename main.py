# ****BASIC INFO*****
import pygame
import time
# Initalizes the Module
pygame.init()

# Assign White & Black
white = (248, 248, 248)
black = (0, 0, 0) 
red = (223, 50, 50)
blue = (14, 77, 146)

# Assigns Dimensions
x = 600
y = 400

# Creates Window
window = pygame.display.set_mode((x, y))
# Sets Window's Caption
pygame.display.set_caption("Virtual Garden")

# Establishes Font Size and Type
font = pygame.font.Font('gamebit.ttf', 16) 
cont_font = pygame.font.Font('gamebit.ttf', 12) 

# ****BASIC INFO*****


# ****BASIC FUNCTIONS*****

# Typewriter Effect (2)
def typewriter(string, dx, dy):
  text = ''
  for index in range(len(string)):
    text += string[index]
    surface = font.render(text, True, black, white)
    text_dimensions = surface.get_rect()
    text_dimensions.center = (x//dx, y//dy)
    window.blit(surface, text_dimensions)
    pygame.display.update()
    pygame.time.wait(75)

# Typewriter Effect for Continue Prompt
def cont(string, dx, dy):
  text = ''
  for index in range(len(string)):
    text += string[index]
    surface = cont_font.render(text, True, black, white)
    text_dimensions = surface.get_rect()
    text_dimensions.center = (x//dx, y//dy)
    window.blit(surface, text_dimensions)
    pygame.display.update()
    pygame.time.wait(25)

# ****BASIC FUNCTIONS*****



# ****ACTIVITIES****

def watering():
  pass

def pest_control():
  pass

def sowing_seeds():
  background2 = pygame.image.load('SowingSeeds.png').convert()

  seed_packet1 = pygame.image.load('SeedPacket1.png')
  seed_packet2 = pygame.image.load('SeedPacket2.png')
  seed_packet3 = pygame.image.load('SeedPacket3.png')
  seed_packet4 = pygame.image.load('SeedPacket4.png')
  seed_packet5 = pygame.image.load('SeedPacket5.png')
  seed_packet6 = pygame.image.load('SeedPacket6.png')
  seed_packet7 = pygame.image.load('SeedPacket7.png')

  window.fill(white)
  window.blit(background2, (0,0))
  window.blit(seed_packet1, (400, 200))
  pygame.display.update()

  index = 0
  state = True

  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          pygame.draw.rect(window, blue, (450, 290, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 300 and my > 290 and mx < 460 and mx > 450:
              window.blit(background2, (0,0))
              window.blit(seed_packet2, (400, 200))
              pygame.display.update()
              index += 1

        if index == 1:
          pygame.draw.rect(window, blue, (470, 290, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 300 and my > 290 and mx < 480 and mx > 470:
              window.blit(background2, (0,0))
              window.blit(seed_packet3, (400, 200))
              pygame.display.update()
              index += 1

        
        if index == 2:
          pygame.draw.rect(window, blue, (470, 270, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 280 and my > 270 and mx < 480 and mx > 470:
              window.blit(background2, (0,0))
              window.blit(seed_packet4, (400, 200))
              pygame.display.update()
              index += 1


        if index == 3:
          pygame.draw.rect(window, blue, (490, 265, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 275 and my > 265 and mx < 500 and mx > 490:
              window.blit(background2, (0,0))
              window.blit(seed_packet5, (400, 200))
              pygame.display.update()
              index += 1


        if index == 4:
          pygame.draw.rect(window, blue, (490, 255, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 265 and my > 255 and mx < 500 and mx > 490:
              window.blit(background2, (0,0))
              window.blit(seed_packet6, (400, 200))
              pygame.display.update()
              index += 1


        if index == 5:
          pygame.draw.rect(window, blue, (520, 235, 10, 10))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 245 and my > 235 and mx < 530 and mx > 520:
              window.blit(background2, (0,0))
              window.blit(seed_packet7, (400, 200))
              pygame.display.update()
              state = False
        
          
      


def moving_seeds():
  planting = pygame.image.load('Planting1.png').convert()
  planting1 = pygame.image.load('Planting2.png').convert()
  planting2 = pygame.image.load('Planting3.png').convert()
  planting3 = pygame.image.load('Planting4.png').convert()
  planting4 = pygame.image.load('Planting5.png').convert()
  planting5 = pygame.image.load('Planting6.png').convert()
  planting6 = pygame.image.load('Planting7.png').convert()
  planting7 = pygame.image.load('Planting8.png').convert()
  planting8 = pygame.image.load('Planting9.png')
  seed_packet7 = pygame.image.load('SeedPacket7.png')
  
  window.blit(planting, (0,0))
  window.blit(seed_packet7, (450, 250))
  pygame.display.update()

  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          window.blit(planting, (0,0))
          window.blit(seed_packet7, (450, 250))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 370 and my > 345 and mx < 65 and mx > 50:
              window.blit(planting1, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1
        
        if index == 1:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 365 and my > 350 and mx < 125 and mx > 110:
              window.blit(planting2, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1


        if index == 2:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 360 and my > 345 and mx < 190 and mx > 175:
              window.blit(planting3, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1


        if index == 3:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 365 and my > 350 and mx < 255 and mx > 240:
              window.blit(planting4, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1


        if index == 4:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 355 and my > 340 and mx < 320 and mx > 300:
              window.blit(planting5, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1


        if index == 5:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 370 and my > 345 and mx < 385 and mx > 365:
              window.blit(planting6, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1


        if index == 6:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 365 and my > 350 and mx < 435 and mx > 420:
              window.blit(planting7, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              index += 1

        if index == 7:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 355 and my > 340 and mx < 485 and mx > 470:
              window.blit(planting8, (0,0))
              window.blit(seed_packet7, (450, 250))
              pygame.display.update()
              time.sleep(3)
              state = False

        
def sowing_seeds_instructions():
  instruct = pygame.image.load('InstructScreen.png').convert()
  window.fill(white)
  window.blit(instruct, (0,0))

  dx = 2
  dy = 3
  text = 'Activity: Sowing Seeds'
  typewriter(text, dx, dy)

  dx = 2
  dy = 2.5
  text = 'Click on the Blue Squares'
  typewriter(text, dx, dy)

  dx = 2
  dy = 2.2
  text = 'to open the seed packet.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 2
  text = 'Then click on each seed'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.80
  text = 'to place in the soil.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.3
  text = 'Press Enter to Continue.'
  cont(text, dx, dy)

  enter = input()




# ****INTRO SCREEN****

# Load Background and Text for Intro (1)
background1 = pygame.image.load('GardenFrame1.png').convert()

def first_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.35
  text = 'Hello! Welcome to your'
  typewriter(text, dx, dy)


  dx = 2
  dy = 1.20
  text = 'own Virtual Garden!'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter to Continue.'
  cont(text, dx, dy)

  enter = input()


def second_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.35
  text = "Here we'll be planting"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'fruits, vegetables, & flowers!'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter to Continue.'
  cont(text, dx, dy)

  enter = input()


def third_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.35
  text = "We'll be starting with"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'an Ivy plant for practice.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()


def fourth_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.35
  text = "Fun Fact! Ivy plants represent"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = ' affectionate attachment.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()


def fifth_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.34
  text = "Which is why Smith College gifts"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.26
  text = 'Ivy plants to new students and'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.19
  text = 'has Ivy Day for Seniors.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()


def sixth_screen():
  window.fill(white)
  window.blit(background1, (0,0))

  dx = 2
  dy = 1.35
  text = "Anyways, let's start!"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'We should first sow the seeds.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()


def intro():
  first_screen()
  second_screen()
  third_screen()
  fourth_screen()
  fifth_screen()
  sixth_screen()


# ****SECOND SET SCREENS****
background2 = pygame.image.load('GardenFrame2.png').convert()

def seventh_screen():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "Great! Now we can"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'continue with other plants.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()

def eighth_screen():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "Choose what the next plant"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'should be by typing your choice.'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Press Enter.'
  cont(text, dx, dy)

  enter = input()

def choose_plant_3():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "Do you want to plant:"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'fruits, vegetables, or flowers?'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Type your choice.'
  cont(text, dx, dy)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'FRUITS' or choice == 'FRUIT' or choice == 'VEGETABLE' or choice == 'VEGETABLES' or choice == 'FLOWER' or choice == 'FLOWERS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      dx = 2
      dy = 1.35
      text = "Great Choice! Now let's"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.20
      text = "choose more specifically!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.1
      text = 'Press Enter.'
      cont(text, dx, dy)
      check = 1

      enter = input()

      return choice
    

    else:
      dx = 2
      dy = 1.1
      text = 'Please try again.'
      cont(text, dx, dy)
      choice = input()
      choice = choice.upper()

def choose_fruit():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "What type of fruit:"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'apples or grapes?'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Type your choice.'
  cont(text, dx, dy)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'APPLE' or choice == 'APPLES' or choice == 'GRAPE' or choice == 'GRAPES':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      dx = 2
      dy = 1.35
      text = "Great!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.20
      text = "Let's start again!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.1
      text = 'Press Enter.'
      cont(text, dx, dy)
      check = 1

      enter = input()

      return choice
    

    else:
      dx = 2
      dy = 1.1
      text = 'Please try again.'
      cont(text, dx, dy)
      choice = input()
      choice = choice.upper()

def choose_flower():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "What type of flower:"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'roses or sunflowers?'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Type your choice.'
  cont(text, dx, dy)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'ROSE' or choice == 'ROSES' or choice == 'SUNFLOWER' or choice == 'SUNFLOWERS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      dx = 2
      dy = 1.35
      text = "Great!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.20
      text = "Let's start again!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.1
      text = 'Press Enter.'
      cont(text, dx, dy)
      check = 1

      enter = input()

      return choice
    

    else:
      dx = 2
      dy = 1.1
      text = 'Please try again.'
      cont(text, dx, dy)
      choice = input()
      choice = choice.upper()

def choose_vegetable():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  dx = 2
  dy = 1.35
  text = "What type of flower:"
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.20
  text = 'roses or sunflowers?'
  typewriter(text, dx, dy)

  dx = 2
  dy = 1.1
  text = 'Type your choice.'
  cont(text, dx, dy)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'ROSE' or choice == 'ROSES' or choice == 'SUNFLOWER' or choice == 'SUNFLOWERS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      dx = 2
      dy = 1.35
      text = "Great!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.20
      text = "Let's start again!"
      typewriter(text, dx, dy)

      dx = 2
      dy = 1.1
      text = 'Press Enter.'
      cont(text, dx, dy)
      check = 1

      enter = input()

      return choice
    

    else:
      dx = 2
      dy = 1.1
      text = 'Please try again.'
      cont(text, dx, dy)
      choice = input()
      choice = choice.upper()

  
def main():
  intro()
  sowing_seeds_instructions()
  sowing_seeds()
  moving_seeds()
  seventh_screen()
  eighth_screen()
  second_plant = choose_plant_3()
  if second_plant == 'FRUIT' or second_plant == 'FRUITS':
    fruit = choose_fruit()

  elif second_plant == 'FLOWER' or second_plant == 'FLOWERS':
    flower = choose_flower()

  else:
  



# References

# 1) Lines : Displaying Background Image
# https://www.geeksforgeeks.org /python-display-images-with-pygame/

# 2) Lines:
#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

# 3) Lines:
# https://stackoverflow.com/questions/ 23718596/making-text-appear-one-character-at-a-time-pygame

# 4) 
# https://www.pygame.org/docs/

# 5) Mouse Clicks
# https://www.youtube.com/watch?v=qU4U4bhZ9cQ