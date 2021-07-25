# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 23:31:54 2021

@author: DIVYAPRAKASH
"""

import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and resources"""
    def __init__(self):
        """Initialize the game and generate resources"""
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        #Set the background color.
        self.bg_color = (230,230,230)
        
    def run_game(self):
        """Start the main loop of the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
                    
            #Make the most recently drawn screen visible
            pygame.display.flip()
            
if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    
        
        
