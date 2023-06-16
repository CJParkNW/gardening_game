# --------------------------------------------------------
#        Name: Catherine Park
# Course Info: CSC111 - Fall 2020
# Description: Virtual Garden - Final Project
#        Date: December 14th, 2020
# I did not collaborate with anyone 
# on this assignment.
# --------------------------------------------------------

# ****BASIC INFO*****
# Modules that needed to be imported
import pygame
import time

# Initializes the Module
pygame.init()

# Assign White, Black, and Blue Colors
white = (248, 248, 248)
black = (0, 0, 0) 
blue = (14, 77, 146)

# Assigns Window Dimensions
x = 600
y = 400

# Creates Basic Window
window = pygame.display.set_mode((x, y))
# Sets Window's Caption
pygame.display.set_caption("Virtual Garden")

# Establishes Font Size and Type
font = pygame.font.Font('gamebit.ttf', 16) 
cont_font = pygame.font.Font('gamebit.ttf', 12) 


# ****BASIC FUNCTIONS*****
# Typewriter Effect for Main Text
def typewriter(string, dx, dy):
  '''Basic Function for Main Text in Game. Allows for typewriter game effect.
  Takes the inputs for string(text), dx, and dy'''
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
  '''Basic Function for Press Enter to Continue Text. Allows for
  typewriter game effect. Takes input string, dx, and dy (Loading time is shorter)'''
  text = ''
  for index in range(len(string)):
    text += string[index]
    surface = cont_font.render(text, True, black, white)
    text_dimensions = surface.get_rect()
    text_dimensions.center = (x//dx, y//dy)
    window.blit(surface, text_dimensions)
    pygame.display.update()
    pygame.time.wait(45)



# *****FIRST GROUP OF STATEMENT PAGES******

# Loads Intro Page Image to Use
statementimg = pygame.image.load('BlankIntro.png').convert()

def statement1():
  '''Loads First Set of Text for Introduction'''
  window.fill(white)
  window.blit(statementimg, (0,0))

  text = 'Fall 2020: CSC111'
  typewriter(text, 2, 3)

  text = 'Catherine Park 2023'
  typewriter(text, 2, 2.5)

  text = 'This game was inspired by'
  typewriter(text, 2, 2.2)

  text = 'Gardening Mama (Nintendo DS)'
  typewriter(text, 2, 2)

  text = 'and other 8-Bit games.'
  typewriter(text, 2, 1.80)

  dx = 2
  dy = 1.3
  text = 'Press Enter to Continue.'
  cont(text, 2, 1.3)

  enter = input()

def statement2():
  '''Loads Second Set of Text for Introduction'''
  window.fill(white)
  window.blit(statementimg, (0,0))

  text = 'Images were created by'
  typewriter(text, 2, 3)

  text = 'Catherine Park with '
  typewriter(text, 2, 2.5)

  text = 'inspiration from the '
  typewriter(text, 2, 2.2)

  text = 'different games'
  typewriter(text, 2, 2)

  text = 'mentioned earlier.'
  typewriter(text, 2, 1.80)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.3)

  enter = input()

def statement():
  '''Groups Basic Intro Text Together'''
  statement1()
  statement2()


# *******ACTIVITIES IN GAME*******

# Watering Activity

# Loads all Watering Backgrounds to use later and converts
# image to same format used by pygame
wateringimg1 = pygame.image.load('watering_background/Watering1.png').convert()
wateringimg2 = pygame.image.load('watering_background/Watering2.png').convert()
wateringimg3 = pygame.image.load('watering_background/Watering3.png').convert()
wateringimg4 = pygame.image.load('watering_background/Watering4.png').convert()
wateringimg5 = pygame.image.load('watering_background/Watering5.png').convert()
wateringimg6 = pygame.image.load('watering_background/Watering6.png').convert()
wateringimg7 = pygame.image.load('watering_background/Watering7.png').convert()
wateringimg8 = pygame.image.load('watering_background/Watering8.png').convert()


def watering1():
  '''Loads First Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          window.blit(wateringimg1, (0,0))
          pygame.display.update()
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg2, (0,0))
              pygame.display.update()
              index += 1
              state = False


def watering2():
  '''Loads Second Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg3, (0,0))
              pygame.display.update()
              index += 1
              state = False

              
def watering3():
  '''Loads Third Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg4, (0,0))
              pygame.display.update()
              index += 1
              state = False


def watering4():
  '''Loads Fourth Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg5, (0,0))
              pygame.display.update()
              index += 1
              state = False

def watering5():
  '''Loads Fifth Set of Watering Activity'''
  window.fill(white)
  
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg6, (0,0))
              pygame.display.update()
              index += 1
              state = False


def watering6():
  '''Loads Sixth Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg7, (0,0))
              pygame.display.update()
              index += 1
              state = False


def watering7():
  '''Loads Seventh Set of Watering Activity'''
  window.fill(white)
  index = 0
  state = True
  while state == True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      else:
        if index == 0:
          if event.type == pygame.MOUSEBUTTONDOWN:
            (mx, my) = pygame.mouse.get_pos()
            if my < 310 and my > 275 and mx < 550 and mx > 535:
              window.blit(wateringimg8, (0,0))
              pygame.display.update()
              index += 1
              time.sleep(3)
              state = False


def watering_instructions():
  '''Loads Watering Activity Instructions'''
  instruct = pygame.image.load('InstructScreen.png').convert()
  window.fill(white)
  window.blit(instruct, (0,0))

  text = 'Activity: Water the Garden!'
  typewriter(text, 2, 3)

  text = 'Press the white bar on the '
  typewriter(text, 2, 2.5)

  text = 'water pump to fill the '
  typewriter(text, 2, 2.2)

  text = 'watering can or until the '
  typewriter(text, 2, 2)

  text = 'water bar is filled.'
  typewriter(text, 2, 1.80)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.3)

  enter = input()


def watering():
  '''Groups Watering Activity All Together'''
  watering_instructions()
  watering1()
  watering2()
  watering3()
  watering4()
  watering5()
  watering6()
  watering7()


# Pest Control Activity

# Loads all Pest Control Backgrounds to use later and converts
# image to same format used by pygame
pestcontrol1 = pygame.image.load('pest_screens/PestControl1.png').convert()
pestcontrol2 = pygame.image.load('pest_screens/PestControl2.png').convert()
pestcontrol3 = pygame.image.load('pest_screens/PestControl3.png').convert()
pestcontrol4 = pygame.image.load('pest_screens/PestControl4.png').convert()
pestcontrol5 = pygame.image.load('pest_screens/PestControl5.png').convert()
pestcontrol6 = pygame.image.load('pest_screens/PestControl6.png').convert()


def pest_control_act():
    '''Loads complete pest control activity'''
    index = 0
    state = True
    while state == True:
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        else:
          if index == 0:
            window.blit(pestcontrol1, (0, 0))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
              (mx, my) = pygame.mouse.get_pos()
              if my < 185 and my > 130 and mx < 90 and mx > 30:
                window.blit(pestcontrol2, (0, 0))
                pygame.display.update()
                index += 1

          if index == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
              (mx, my) = pygame.mouse.get_pos()
              if my < 240 and my > 185 and mx < 180 and mx > 120:
                window.blit(pestcontrol3, (0,0))
                pygame.display.update()
                index += 1

          if index == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
              (mx, my) = pygame.mouse.get_pos()
              if my < 60 and my > 0 and mx < 300 and mx > 240:
                window.blit(pestcontrol4, (0,0))
                pygame.display.update()
                index += 1

          if index == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
              (mx, my) = pygame.mouse.get_pos()
              if my < 390 and my > 330 and mx < 370 and mx > 315:
                window.blit(pestcontrol5, (0, 0))
                pygame.display.update()
                index += 1

          if index == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
              (mx, my) = pygame.mouse.get_pos()
              if my < 205 and my > 145 and mx < 535 and mx > 480:
                window.blit(pestcontrol6, (0, 0))
                pygame.display.update()
                index += 1
                time.sleep(3)
                state = False


def pest_instructions():
  '''Loads Instructions for Pest Control'''
  instruct = pygame.image.load('InstructScreen.png').convert()
  window.fill(white)
  window.blit(instruct, (0,0))

  text = 'Activity: Pest Control!'
  typewriter(text, 2, 3)

  text = 'Click on the pests from left'
  typewriter(text, 2, 2.5)

  text = 'to right in order to get'
  typewriter(text, 2, 2.2)

  text = 'rid of them and ensure that'
  typewriter(text, 2, 2)

  text = 'our plants grow healthy.'
  typewriter(text, 2, 1.80)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.3)

  enter = input()


def pest_control():
  '''Groups Pest Control Activity Together'''
  pest_instructions()
  pest_control_act()


# Sowing Seeds Activity

# Loads all Seed Packet Images to use later
seed_packet1 = pygame.image.load('seed_packet/SeedPacket1.png')
seed_packet2 = pygame.image.load('seed_packet/SeedPacket2.png')
seed_packet3 = pygame.image.load('seed_packet/SeedPacket3.png')
seed_packet4 = pygame.image.load('seed_packet/SeedPacket4.png')
seed_packet5 = pygame.image.load('seed_packet/SeedPacket5.png')
seed_packet6 = pygame.image.load('seed_packet/SeedPacket6.png')

def sowing_seeds():
  '''Loads sowing seeds open packet activity'''
  background2 = pygame.image.load('sowing_seeds/SowingSeeds.png').convert()

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


# Loads all Sowing Seeds Backgrounds to use later and converts
# image to same format used by pygame
planting = pygame.image.load('sowing_seeds/Planting1.png').convert()
planting1 = pygame.image.load('sowing_seeds/Planting2.png').convert()
planting2 = pygame.image.load('sowing_seeds/Planting3.png').convert()
planting3 = pygame.image.load('sowing_seeds/Planting4.png').convert()
planting4 = pygame.image.load('sowing_seeds/Planting5.png').convert()
planting5 = pygame.image.load('sowing_seeds/Planting6.png').convert()
planting6 = pygame.image.load('sowing_seeds/Planting7.png').convert()
planting7 = pygame.image.load('sowing_seeds/Planting8.png').convert()
planting8 = pygame.image.load('sowing_seeds/Planting9.png')
seed_packet7 = pygame.image.load('seed_packet/SeedPacket7.png')


def moving_seeds():
  '''Loads sowing seeds moving seeds activity'''
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
  '''Loads instructions for sowing seeds activities'''
  instruct = pygame.image.load('InstructScreen.png').convert()
  window.fill(white)
  window.blit(instruct, (0,0))

  text = 'Activity: Sowing Seeds'
  typewriter(text, 2, 3)

  text = 'Click on the Blue Squares'
  typewriter(text, 2, 2.5)

  text = 'to open the seed packet.'
  typewriter(text, 2, 2.2)

  text = 'Then click on each seed'
  typewriter(text, 2, 2)

  text = 'to place in the soil.'
  typewriter(text, 2, 1.80)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.3)

  enter = input()


def sow_seeds_full():
  '''Groups all Sowing seeds function activities together'''
  sowing_seeds_instructions()
  sowing_seeds()
  moving_seeds()


# *****WELCOME & FIRST PLANT SCREEN******

# Loads first background of the main garden
background1 = pygame.image.load('garden_background/GardenFrame1.png').convert()

def first_screen():
  '''First Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = 'Hello! Welcome to your'
  typewriter(text, 2, 1.35)

  text = 'own Virtual Garden!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.1)

  enter = input()


def second_screen():
  '''Second Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = "Here we'll be planting"
  typewriter(text, 2, 1.35)

  text = 'fruits, vegetables, & flowers!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter to Continue.'
  cont(text, 2, 1.1)

  enter = input()


def third_screen():
  '''Third Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = "We'll be starting with"
  typewriter(text, 2, 1.35)

  text = 'an Ivy plant for practice.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()


def fourth_screen():
  '''Fourth Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = "Fun Fact! Ivy plants represent"
  typewriter(text, 2, 1.35)

  text = ' affectionate attachment.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()


def fifth_screen():
  '''Fifth Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = "Which is why Smith College gifts"
  typewriter(text, 2, 1.34)

  text = 'Ivy plants to new students and'
  typewriter(text, 2, 1.26)

  text = 'has Ivy Day for Seniors.'
  typewriter(text, 2, 1.19)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()


def sixth_screen():
  '''Sixth Screen Introducing'''
  window.fill(white)
  window.blit(background1, (0,0))

  text = "Anyways, let's start!"
  typewriter(text, 2, 1.35)

  text = 'We should first sow the seeds.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()


def intro():
  '''Group all Intro/Welcome Screens Together'''
  first_screen()
  second_screen()
  third_screen()
  fourth_screen()
  fifth_screen()
  sixth_screen()


# *****SECOND SET OF SCREENS******

# Loads Second Background of Main Garden
background2 = pygame.image.load('garden_background/GardenFrame2.png').convert()

def seventh_screen():
  '''Seventh Screen in Main Garden'''
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "Great! Now we can"
  typewriter(text, 2, 1.35)

  text = 'continue with other plants.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def eighth_screen():
  '''Eighth Screen in Main Garden'''
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "Choose what the next plant"
  typewriter(text, 2, 1.35)

  text = 'should be by typing your choice.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Third Background of Main Garden
background3 = pygame.image.load('garden_background/GardenFrame3.png').convert()

def ninth_screen():
  '''Ninth Screen in Main Garden'''
  window.fill(white)
  window.blit(background3, (0,0))
  pygame.display.update()

  text = "Oh no! Our first plant's wilting."
  typewriter(text, 2, 1.35)

  text = 'We should go check on it.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Fourth Background of Main Garden
background4 = pygame.image.load('garden_background/GardenFrame4.png').convert()

def tenth_screen():
  '''Tenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()

  text = "Amazing! Our plants are"
  typewriter(text, 2, 1.35)

  text = 'growing really well.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def eleventh_screen():
  '''Eleventh Screen in Main Garden'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()

  text = "Now, let's choose our"
  typewriter(text, 2, 1.35)

  text = 'third plant to grow!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Fifth Background of Main Garden
background5 = pygame.image.load('garden_background/GardenFrame5.png').convert()

def twelfth_screen():
  '''Twelfth Screen in Main Garden'''
  window.fill(white)
  window.blit(background5, (0, 0))
  pygame.display.update()

  text = "Oh dear! Looks like our"
  typewriter(text, 2, 1.35)

  text = 'second plant needs help!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Sixth Background of Main Garden
background6 = pygame.image.load('garden_background/GardenFrame6.png').convert()

def thirteenth_screen():
  '''Thirteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background6, (0, 0))
  pygame.display.update()

  text = "Brilliant! You're a"
  typewriter(text, 2, 1.35)

  text = 'natural at gardening!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def fourteenth_screen():
  '''Fourteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background6, (0, 0))
  pygame.display.update()

  text = "Oh! Looks like our first"
  typewriter(text, 2, 1.35)

  text = 'plant is ready for harvest!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# **** ICONS LOADING FOR HARVEST *****

# Loads all Icons for the Plants
ivy = pygame.image.load('plant_icons/IvyIcon.png').convert()
apple = pygame.image.load('plant_icons/AppleIcon.png').convert()
bellpepper = pygame.image.load('plant_icons/BellPepperIcon.png').convert()
corn = pygame.image.load('plant_icons/CornIcon.png').convert()
grapes = pygame.image.load('plant_icons/GrapesIcon.png').convert()
roses = pygame.image.load('plant_icons/RoseIcon.png').convert()
sunflower = pygame.image.load('plant_icons/SunflowerIcon.png').convert()

# Loads Seventh Background of Main Garden
background7 = pygame.image.load('garden_background/GardenFrame7.png')

def fifteenth_screen():
  '''Fifteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background7, (0, 0))
  window.blit(ivy, (225, 100))
  pygame.display.update()

  text = "How beautiful!"
  typewriter(text, 2, 1.35)

  text = 'You did an amazing job!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def sixteenth_screen():
  '''Sixteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background7, (0, 0))
  pygame.display.update()

  text = "We can now choose our"
  typewriter(text, 2, 1.35)

  text = 'final plant to grow!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()


def second_set():
  '''Groups Second Set of Screens in Main Garden'''
  twelfth_screen()
  pest_control()
  thirteenth_screen()
  fourteenth_screen()
  fifteenth_screen()
  sixteenth_screen()


# ******** THIRD SET OF SCREENS AND HARVEST FACTS *******

# Loads Eighth Background of Main Garden
background8 = pygame.image.load('garden_background/GardenFrame8.png')

def seventeenth_screen():
  '''Seventeenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background8, (0, 0))
  pygame.display.update()

  text = 'Oh! We need to go check'
  typewriter(text, 2, 1.35)

  text = 'on our third set of plants!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Ninth Background of Main Garden
background9 = pygame.image.load('garden_background/GardenFrame9.png')

def eighteenth_screen():
  '''Eighteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background9, (0, 0))
  pygame.display.update()

  text = 'Looks like our second set'
  typewriter(text, 2, 1.35)

  text = 'of plants are ready to harvest!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Tenth Background of Main Garden
background10 = pygame.image.load('garden_background/GardenFrame10.png')


def harvest_sec(plant_name):
  '''Second Harvest Screen in Main Garden with Fun Facts'''
  window.fill(white)
  window.blit(background10, (0,0))

  if plant_name == 'APPLE' or plant_name == 'APPLES':
    window.blit(apple, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Crabapples are the only"
    typewriter(text, 2, 1.35)

    text = 'native apple to North America!'
    typewriter(text, 2, 1.20)

    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'GRAPE' or plant_name == 'GRAPES':
    window.blit(grapes, (225, 100))
    pygame.display.update()

    text = "Fun Fact! It takes 2.5 pounds of"
    typewriter(text, 2, 1.35)

    text = 'grapes to make one bottle of wine!'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'BELLPEPPER' or plant_name == 'BELLPEPPERS' or \
          plant_name == 'BELL PEPPER' or plant_name == 'BELL PEPPERS':
    window.blit(bellpepper, (225, 100))
    pygame.display.update()

    text = "Fun Fact! All peppers are fruits."
    typewriter(text, 2, 1.35)


    text = 'So, I actually made a mistake...'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'CORN' or plant_name == 'CORNS':
    window.blit(corn, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Corn can be produce in"
    typewriter(text, 2, 1.35)


    text = 'various colors (blue,purple,etc.)'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'ROSE' or plant_name == 'ROSES':
    window.blit(roses, (225, 100))
    pygame.display.update()

    text = "Fun Fact! The color of the rose"
    typewriter(text, 2, 1.35)


    text = 'determines what it symbolizes.'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'SUNFLOWER' or plant_name == 'SUNFLOWERS':
    window.blit(sunflower, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Sunflowers at bud stage"
    typewriter(text, 2, 1.35)


    text = 'can track the sun (heliotropism).'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()


def nineteenth_screen():
  '''Nineteenth Screen in Main Garden'''
  window.fill(white)
  window.blit(background10, (0, 0))
  pygame.display.update()

  text = 'Looks like our fourth group'
  typewriter(text, 2, 1.35)

  text = 'of plants needs some help!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Eleventh Background of Main Garden
background11 = pygame.image.load('garden_background/GardenFrame11.png')

def twentieth_screen():
  '''Twentieth Screen in Main Garden'''
  window.fill(white)
  window.blit(background11, (0, 0))
  pygame.display.update()

  text = 'Looks like our third set'
  typewriter(text, 2, 1.35)

  text = 'of plants are ready to harvest!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Twelfth Background of Main Garden
background12 = pygame.image.load('garden_background/GardenFrame12.png')

def harvest_third(plant_name):
  '''Third Harvest Screen in Main Garden with Fun Facts'''
  window.fill(white)
  window.blit(background12, (0,0))

  if plant_name == 'APPLE' or plant_name == 'APPLES':
    window.blit(apple, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Crabapples are the only"
    typewriter(text, 2, 1.35)

    text = 'native apple to North America!'
    typewriter(text, 2, 1.20)

    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'GRAPE' or plant_name == 'GRAPES':
    window.blit(grapes, (225, 100))
    pygame.display.update()

    text = "Fun Fact! It takes 2.5 pounds of"
    typewriter(text, 2, 1.35)

    text = 'grapes to make one bottle of wine!'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'BELLPEPPER' or plant_name == 'BELLPEPPERS' or \
          plant_name == 'BELL PEPPER' or plant_name == 'BELL PEPPERS':
    window.blit(bellpepper, (225, 100))
    pygame.display.update()

    text = "Fun Fact! All peppers are fruits."
    typewriter(text, 2, 1.35)


    text = 'So, I actually made a mistake...'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'CORN' or plant_name == 'CORNS':
    window.blit(corn, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Corn can be produce in"
    typewriter(text, 2, 1.35)


    text = 'various colors (blue,purple,etc.)'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'ROSE' or plant_name == 'ROSES':
    window.blit(roses, (225, 100))
    pygame.display.update()

    text = "Fun Fact! The color of the rose"
    typewriter(text, 2, 1.35)


    text = 'determines what it symbolizes.'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'SUNFLOWER' or plant_name == 'SUNFLOWERS':
    window.blit(sunflower, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Sunflowers at bud stage"
    typewriter(text, 2, 1.35)


    text = 'can track the sun (heliotropism).'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

def twentyfirst_screen():
  '''Twentyfirst Screen in Main Garden'''
  window.fill(white)
  window.blit(background12, (0, 0))
  pygame.display.update()

  text = 'Looks like our fourth set'
  typewriter(text, 2, 1.35)

  text = 'of plants are ready to harvest!'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

# Loads Thirteenth Background of Main Garden
background13 = pygame.image.load('garden_background/GardenFrame13.png')

def harvest_fourth(plant_name):
  '''Fourth Harvest Screen in Main Garden with Fun Facts'''
  window.fill(white)
  window.blit(background13, (0,0))

  if plant_name == 'APPLE' or plant_name == 'APPLES':
    window.blit(apple, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Crabapples are the only"
    typewriter(text, 2, 1.35)

    text = 'native apple to North America!'
    typewriter(text, 2, 1.20)

    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'GRAPE' or plant_name == 'GRAPES':
    window.blit(grapes, (225, 100))
    pygame.display.update()

    text = "Fun Fact! It takes 2.5 pounds of"
    typewriter(text, 2, 1.35)

    text = 'grapes to make one bottle of wine!'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'BELLPEPPER' or plant_name == 'BELLPEPPERS' or \
          plant_name == 'BELL PEPPER' or plant_name == 'BELL PEPPERS':
    window.blit(bellpepper, (225, 100))
    pygame.display.update()

    text = "Fun Fact! All peppers are fruits."
    typewriter(text, 2, 1.35)


    text = 'So, I actually made a mistake...'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'CORN' or plant_name == 'CORNS':
    window.blit(corn, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Corn can be produce in"
    typewriter(text, 2, 1.35)


    text = 'various colors (blue,purple,etc.)'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'ROSE' or plant_name == 'ROSES':
    window.blit(roses, (225, 100))
    pygame.display.update()

    text = "Fun Fact! The color of the rose"
    typewriter(text, 2, 1.35)


    text = 'determines what it symbolizes.'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()

  elif plant_name == 'SUNFLOWER' or plant_name == 'SUNFLOWERS':
    window.blit(sunflower, (225, 100))
    pygame.display.update()

    text = "Fun Fact! Sunflowers at bud stage"
    typewriter(text, 2, 1.35)


    text = 'can track the sun (heliotropism).'
    typewriter(text, 2, 1.20)


    text = 'Press Enter.'
    cont(text, 2, 1.1)

    enter = input()




# ***** CHOOSING SPECIFICALLY WHICH PLANT *****

def choose_plant_3():
  '''Choosing plant screen'''
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "Do you want to plant:"
  typewriter(text, 2, 1.35)

  text = 'fruits, vegetables, or flowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'FRUITS' or choice == 'FRUIT' or choice == 'VEGETABLE' or choice == 'VEGETABLES' or choice == 'FLOWER' or choice == 'FLOWERS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      text = "Great Choice! Now let's"
      typewriter(text, 2, 1.35)

      text = "choose more specifically!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_fruit():
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "What type of fruit:"
  typewriter(text, 2, 1.35)

  text = 'apples or grapes?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'APPLE' or choice == 'APPLES' or choice == 'GRAPE' or choice == 'GRAPES':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()


def choose_fruit_final():
  '''Choosing fourth plant screen'''
  window.fill(white)
  window.blit(background7, (0, 0))
  pygame.display.update()

  text = "What type of fruit:"
  typewriter(text, 2, 1.35)

  text = 'apples or grapes?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'APPLE' or choice == 'APPLES' or choice == 'GRAPE' or choice == 'GRAPES':

      window.fill(white)
      window.blit(background7, (0, 0))
      pygame.display.update()

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice


    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()


def choose_flower():
  '''Choosing which flower specifically'''
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "What type of flower:"
  typewriter(text, 2, 1.35)

  text = 'roses or sunflowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'ROSE' or choice == 'ROSES' or choice == 'SUNFLOWER' or choice == 'SUNFLOWERS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()


def choose_flower_final():
  '''Last Choice of Plant if Flower'''
  window.fill(white)
  window.blit(background7, (0, 0))
  pygame.display.update()

  text = "What type of flower:"
  typewriter(text, 2, 1.35)

  text = 'roses or sunflowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'ROSE' or choice == 'ROSES' or choice == 'SUNFLOWER' or choice == 'SUNFLOWERS':

      window.fill(white)
      window.blit(background7, (0, 0))
      pygame.display.update()

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
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
  '''Choose which type of vegetable'''
  window.fill(white)
  window.blit(background2, (0,0))
  pygame.display.update()  

  text = "What type of vegetable:"
  typewriter(text, 2, 1.35)

  text = 'bell pepper or corn?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'BELLPEPPER' or choice == 'BELLPEPPERS' or choice == 'BELL PEPPER' or choice == 'BELL PEPPERS' or choice == 'CORN' or choice == 'CORNS':

      window.fill(white)
      window.blit(background2, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()


def choose_vegetable_final():
  '''Last Choice if Final is Vegetable'''
  window.fill(white)
  window.blit(background7, (0, 0))
  pygame.display.update()

  text = "What type of vegetable:"
  typewriter(text, 2, 1.35)

  text = 'bell pepper or corn?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'BELLPEPPER' or choice == 'BELLPEPPERS' or \
            choice == 'BELL PEPPER' or choice == 'BELL PEPPERS' or \
            choice == 'CORN' or choice == 'CORNS':

      window.fill(white)
      window.blit(background7, (0, 0))
      pygame.display.update()

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice


    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()


def choose_wo_fruit():
  '''Third Choice without Fruit'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()

  text = "Do you want to plant:"
  typewriter(text, 2, 1.35)

  text = 'vegetables or flowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'VEGETABLE' or choice == 'VEGETABLES' or \
            choice == 'FLOWER' or choice == 'FLOWERS':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great Choice! Now let's"
      typewriter(text, 2, 1.35)

      text = "choose more specifically!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_wo_flower():
  '''Third Choice Without Flower'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()  

  text = "Do you want to plant:"
  typewriter(text, 2, 1.35)

  text = 'fruits, or vegetables?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'FRUITS' or choice == 'FRUIT' or \
            choice == 'VEGETABLE' or choice == 'VEGETABLES':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great Choice! Now let's"
      typewriter(text, 2, 1.35)

      text = "choose more specifically!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_wo_vegetable():
  '''Third Choice without Vegetable'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()  

  text = "Do you want to plant:"
  typewriter(text, 2, 1.35)

  text = 'fruits or flowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'FRUITS' or choice == 'FRUIT' or choice == 'FLOWER' or choice == 'FLOWERS':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great Choice! Now let's"
      typewriter(text, 2, 1.35)

      text = "choose more specifically!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_fruit_third():
  '''Choosing Fruit for Third'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()  

  text = "What type of fruit:"
  typewriter(text, 2, 1.35)

  text = 'apples or grapes?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'APPLE' or choice == 'APPLES' or choice == 'GRAPE' or choice == 'GRAPES':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_flower_third():
  '''Choosing Flower for Third'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()  

  text = "What type of flower:"
  typewriter(text, 2, 1.35)

  text = 'roses or sunflowers?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'ROSE' or choice == 'ROSES' or choice == 'SUNFLOWER' or choice == 'SUNFLOWERS':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

def choose_vegetable_third():
  '''Choosing Vegetable for Third'''
  window.fill(white)
  window.blit(background4, (0,0))
  pygame.display.update()  

  text = "What type of vegetable:"
  typewriter(text, 2, 1.35)

  text = 'bell pepper or corn?'
  typewriter(text, 2, 1.20)

  text = 'Type your choice.'
  cont(text, 2, 1.1)

  check = 0
  choice = input()
  choice = choice.upper()

  while check == 0:

    if choice == 'BELLPEPPER' or choice == 'BELLPEPPERS' or \
            choice == 'BELL PEPPER' or choice == 'BELL PEPPERS' or \
            choice == 'CORN' or choice == 'CORNS':

      window.fill(white)
      window.blit(background4, (0,0))
      pygame.display.update()  

      text = "Great!"
      typewriter(text, 2, 1.35)

      text = "Let's start again!"
      typewriter(text, 2, 1.20)

      text = 'Press Enter.'
      cont(text, 2, 1.1)
      check = 1

      enter = input()

      return choice
    

    else:
      text = 'Please try again.'
      cont(text, 2, 1.1)
      choice = input()
      choice = choice.upper()

# CLOSING FINAL STATEMENTS

def final_statement1():
  '''First Final Closing Statement'''
  window.fill(white)
  window.blit(background13, (0, 0))
  pygame.display.update()

  text = "You were amazing at everything! I"
  typewriter(text, 2, 1.35)

  text = 'hope you enjoyed this short game.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def final_statement2():
  '''Second Final Closing Statement'''
  window.fill(white)
  window.blit(background13, (0, 0))
  pygame.display.update()

  text = "As well as consider planting your"
  typewriter(text, 2, 1.35)

  text = 'own garden wherever you are.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def final_statement3():
  '''Third Final Closing Statement'''
  window.fill(white)
  window.blit(background13, (0, 0))
  pygame.display.update()

  text = "Thank you so much for"
  typewriter(text, 2, 1.35)

  text = 'playing! -Catherine P.'
  typewriter(text, 2, 1.20)

  text = 'Press Enter.'
  cont(text, 2, 1.1)

  enter = input()

def final():
  '''Group Final Statements Together'''
  final_statement1()
  final_statement2()
  final_statement3()


# ****** MAIN LOOP *****

def main():

  # Introduction and Start with Ivy Plant
  statement()
  intro()
  sow_seeds_full()
  seventh_screen()
  eighth_screen()

  # Choose Type of Second Plant
  second_plant = choose_plant_3()

  # If Second Plant is Fruit
  if second_plant == 'FRUIT' or second_plant == 'FRUITS':
    second_harvest_plant = choose_fruit()
    sow_seeds_full()
    ninth_screen()
    watering()
    tenth_screen()
    eleventh_screen()
    third_plant = choose_wo_fruit()

    # If Third Plant is Flower
    if third_plant == 'FLOWER' or third_plant == 'FLOWERS':
      third_harvest_plant = choose_flower_third()
      sow_seeds_full()
      second_set()

      # Choose Type of Vegetable as Fourth Plant
      fourth_harvest_plant = choose_vegetable_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()

    # If Third Plant is Vegetable
    else:
      third_harvest_plant = choose_vegetable_third()
      sow_seeds_full()
      second_set()
      # Choose Type of Flower as Fourth Plant
      fourth_harvest_plant = choose_flower_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()


  # If Second Plant is Flower
  elif second_plant == 'FLOWER' or second_plant == 'FLOWERS':
    second_harvest_plant = choose_flower()
    sow_seeds_full()
    ninth_screen()
    watering()
    tenth_screen()
    eleventh_screen()
    third_plant = choose_wo_flower()
    # If Third Plant is Fruit
    if third_plant == 'FRUIT' or third_plant == 'FRUITS':
      third_harvest_plant = choose_fruit_third()
      sow_seeds_full()
      second_set()
      # Choose Type of Vegetable as Fourth Plant
      fourth_harvest_plant = choose_vegetable_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()


    # If Third Plant is Vegetable
    else:
      third_harvest_plant = choose_vegetable_third()
      sow_seeds_full()
      second_set()
      # Choose Type of Fruit as Fourth Plant
      fourth_harvest_plant = choose_fruit_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()

  # If Second Plant is Vegetable
  else:
    second_harvest_plant = choose_vegetable()
    sow_seeds_full()
    ninth_screen()
    watering()
    tenth_screen()
    eleventh_screen()
    third_plant = choose_wo_vegetable()

    # If Third Plant is Fruit
    if third_plant == 'FRUIT' or third_plant == 'FRUITS':
      third_harvest_plant = choose_fruit_third()
      sow_seeds_full()
      second_set()
      # Choose Type of Flower as Fourth Plant
      fourth_harvest_plant = choose_flower_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()


    # If Third Plant is Flower
    else:
      third_harvest_plant = choose_flower_third()
      sow_seeds_full()
      second_set()
      # Choose Type of Fruit as Fourth Plant
      fourth_harvest_plant = choose_fruit_final()
      sow_seeds_full()
      seventeenth_screen()
      watering()
      eighteenth_screen()
      harvest_sec(second_harvest_plant)
      nineteenth_screen()
      pest_control()
      twentieth_screen()
      harvest_third(third_harvest_plant)
      twentyfirst_screen()
      harvest_fourth(fourth_harvest_plant)
      final()

main()

# References

# 1) Displaying Background Image = Used in Multiple Screens
# (Ex: first_screen(), second_screen(), etc.)
# https://www.geeksforgeeks.org/python-display-images-with-pygame/

# 2) Creating Font Object and Showing Text = Used in Multiple Screens
# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

# 3) Creating Typerwriter Effect by Making Letters appear one at a time
# https://stackoverflow.com/questions/ 23718596/making-text-appear-one-character-at-a-time-pygame

# 4) Reasons for Converting Loaded Images in Pygame
# https://stackoverflow.com/questions/46245779/very-simple-pygame-very-slow
# https://gamedev.stackexchange.com/questions/81280/pygame-surfaces-which-and-
# when-do-i-need-to-convert#:~:text=convert()%20is%20used%20to,same%20one%20created%20from%20pygame.

# 5) Understanding Pygame Mouse Clicks and Positioning
# https://www.youtube.com/watch?v=qU4U4bhZ9cQ

# 6) Pygame Docs to Understand Functions
# https://www.pygame.org/docs/

# **** Used in Harvest Icon Screens in
# fourth_screen(), harvest_sec(), harvest_third(), and harvest_fourth *****

# 7) Ivy Fact
# https://www.vancouverflorist.com/ivy.aspx

# 8) Apple Fact
# https://web.extension.illinois.edu/apples/facts.cfm

# 9) Grape Fact
# https://www.webmd.com/diet/features/8-healthy-facts-about-grapes#1

# 10) Pepper Fact
# https://www.natureandmore.com/en/products/bell-pepper

# 11) Corn Fact
# https://www.iowacorn.org/media-page/corn-facts

# 12) Rose Fact
# https://www.1800flowers.com/blog/flower-facts/rose-facts/

# 13) Sunflowers Fact
# https://www.thespruce.com/fun-facts-about-sunflowers-3972329

# ******* Font Used for Text ******

# 14) Font Used to Create 8-Bit Look
# https://fonts.google.com/specimen/Press+Start+2P