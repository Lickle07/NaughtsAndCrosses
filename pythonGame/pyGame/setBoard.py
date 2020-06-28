import pygame


def setBoardUp(gamesPlayed, player1Wins, player2Wins):
    white = [255, 255, 255]
    red = [255, 0, 0]
    grey = [100, 100, 100]

    pygame.init()

    game = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption("Joe's Naughts and Crosses")
    font = pygame.font.Font('freesansbold.ttf', 38)


    text = font.render("Naughts and Crosses", True, white)
    title = text.get_rect()
    title.center = (600,20)
    game.blit(text, title)

    font = pygame.font.Font('freesansbold.ttf', 18)

    text = font.render("Games Played: {0}".format(gamesPlayed), True, white)
    gamesPlayedText = text.get_rect()
    gamesPlayedText.center = (600, 40)
    game.blit(text, gamesPlayedText)

    text = font.render("Player 1 Wins: {0}".format(player1Wins), True, white)
    player1Winstext = text.get_rect()
    player1Winstext.center = (500, 60)
    game.blit(text, player1Winstext)

    pygame.draw.rect(game, grey, (1150, 375, 100, 50))
    pygame.draw.rect(game, grey, (1150, 575, 100, 50))

    text = font.render("Player 2 Wins: {0}".format(player2Wins), True, white)
    player2WinsText = text.get_rect()
    player2WinsText.center = (700, 60)
    game.blit(text, player2WinsText)

    text = font.render('Player 1', True, red)
    player1 = text.get_rect()
    player1.center = (1200, 400)
    game.blit(text, player1)


    text = font.render('Player 2', True, red)
    player2 = text.get_rect()
    player2.center = (1200, 600)
    game.blit(text, player2)

    section1 = pygame.draw.rect(game, white, (20, 70, 270, 270))
    section2 = pygame.draw.rect(game, white, (310, 70, 280, 270))
    section3 = pygame.draw.rect(game, white, (610, 70, 280, 270))

    section4 = pygame.draw.rect(game, white, (20, 360, 270, 270))
    section5 = pygame.draw.rect(game, white, (310, 360, 280, 270))
    section6 = pygame.draw.rect(game, white, (610, 360, 280, 270))

    section7 = pygame.draw.rect(game, white, (20, 660, 270, 270))
    section8 = pygame.draw.rect(game, white, (310, 660, 280, 270))
    section9 = pygame.draw.rect(game, white, (610, 660, 280, 270))

    sections = [section1, False], [section2, False], [section3, False], [section4, False], [section5, False], [section6, False], [section7, False], [section8, False], [section9, False]

    pygame.display.update()

    return game, sections, player1, player2