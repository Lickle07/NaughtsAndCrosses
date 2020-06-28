import pygame

red = [220,20,60]

def MakeMove(player1turn, sectionclicked, game):
    if player1turn:
        pygame.draw.line(game, red, (sectionclicked.center[0] + 50, sectionclicked.center[1] + 50),
                         (sectionclicked.center[0] - 50, sectionclicked.center[1] - 50), 5)
        pygame.draw.line(game, red, (sectionclicked.center[0] + 50, sectionclicked.center[1] - 50),
                         (sectionclicked.center[0] - 50, sectionclicked.center[1] + 50), 5)
    if not player1turn:
        pygame.draw.circle(game, red, sectionclicked.center, 50, 5)