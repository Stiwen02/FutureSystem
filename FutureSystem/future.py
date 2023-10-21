import threading

import pygame
from pygame.locals import *

pygame_screen_size = (160, 128)
# pygame_scale_screen_size_by = 3

# pygame_scaled_screen_size = list(pygame_screen_size)
# for index in range(len(pygame_scaled_screen_size)): 
    # pygame_scaled_screen_size[index] *= pygame_scale_screen_size_by
# pygame_scaled_screen_size = tuple(pygame_scaled_screen_size)

pygame.init()
pygame_screen = pygame.display.set_mode(pygame_screen_size) # , HWSURFACE|DOUBLEBUF|RESIZABLE)

# pygame_fake_screen = pygame_screen.copy()
# pygame_picture = pygame.surface.Surface(pygame_scaled_screen_size)
# pygame_picture.fill((0, 0, 0))

class screen:
	sync = 1
	def text(text, x=0, y=0, color=(255, 255, 255)):
		# Use font from Future Board screenshot
		font = pygame.font.SysFont(None, 24)
		img = font.render(text, True, color)
		pygame_screen.blit(img, (x, y))
		screen.sync_refresh()
	def fill(color = (255, 255, 255)):
		pygame_screen.fill(color)
	def sync_refresh():
		if screen.sync == 1:
			screen.refresh()
	def refresh():
		# pygame_fake_screen.fill((0, 0, 0))
		# pygame_fake_screen.blit(pygame_picture, (100, 100))
		# pygame_screen.blit(pygame.transform.scale(pygame_fake_screen, pygame_screen.get_rect().size), (0, 0))
		pygame.display.flip()

class MeowPin:
	pin = ""
	type = ""
	def __init__(self, pin, type):
		self.pin = pin
		self.type = type
	def getDigital(self):
		keys = pygame.key.get_pressed()
		if self.pin.lower == "p2":
			if keys[pygame.K_UP]:
				return 0
			else:
				return 1
		if self.pin.lower == "p13":
			if keys[pygame.K_DOWN]:
				return 0
			else:
				return 1
		if self.pin.lower == "p14":
			if keys[pygame.K_LEFT]:
				return 0
			else:
				return 1
		if self.pin.lower == "p15":
			if keys[pygame.K_RIGHT]:
				return 0
			else:
				return 1
		return 1