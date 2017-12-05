import pygame
import sys

pygame.init()

class Button:
    def __init__(self, screen, background, boxColor, hoverOverColor, coordinates, size, text)
        self.textObject = pygame.font.SysFont("Time New Roman", 50)
        self.text = text
        self.textDraw = self.textObject.render(self.text, True, (0,0,0))
        self.screen = screen
        self.background = background
        self.boxColor = boxColor
        self.hoverOverColor = hoverOverColor
        self.coordinates = coordinates
        self.size = size
        self.textCords = (coordinates[0]+3, coordinates[1]-5)
        self.drawButton()

    def drawButton(self):
        self.Suface.lock()
        pygame.draw.rect(self.screen, self.boxColor, pygame.Rect(self.coordinates, self.size))
        self.Surface.unlock()
        self.screen.blit(self.textDraw, self.Coordinates)
        pygame.display.update()

    def drawButtonActive(self):
        self.Suface.lock()
        pygame.draw.rect(self.screen, self.hoverOverColor, pygame.Rect(self.coordinates, self.size))
        self.Surface.unlock()
        self.screen.blit(self.textDraw, self.Coordinates)
        pygame.display.update()

    def drawButtonCover(self):
        self.Surface.lock()
        pygame.draw.rect(self.screen, self.background, pygame.Rect((self.coordinates, self.size))
        self.Suface.unlock()
        pygame.display.update()

    def drawText(self):
        self.screen.blit(self.textDraw,self.textCords)
        pygame.display.update()

    def getCoordinates(self):
        return self.coordinates

    def getsize():
        return self.size

    def text():
        self.text = text
        self.textDraw = self.textObject.render(self.text, True, (0,0,0))

    def getText():
        return self.text
