import logging
import pygame
from tkinter import *
from tkinter import messagebox
from pythonGame.pyGame import setBoardUp, CheckSectionClicked, MakeMove, CheckWin, toggle_fullscreen

def startGame():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    gamesPlayed = 0
    player1Wins = 0
    player2Wins = 0
    game, sections, player1, player2 = setBoardUp(gamesPlayed, player1Wins, player2Wins)
    magicSquare = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    x = []
    y = []

    won = False
    run = True
    player1turn = False

    while run:
        tie = True
        pygame.time.delay(100)
        playersMagicSquare = []
        if won:
            playerwon = ""
            if player1turn:
                playerwon = "Player 1 Won"
                player1Wins += 1
            else:
                playerwon = "Player 2 Won"
                player2Wins += 1
            Tk().wm_withdraw()
            answer = messagebox.askquestion(playerwon, "Play again?")
            if answer == "yes":
                gamesPlayed += 1
                game, sections, player1, player2 = setBoardUp(gamesPlayed, player1Wins, player2Wins)
                magicSquare = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
                x = []
                y = []
                won = False
            else:
                run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game = toggle_fullscreen()
                    continue
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                if player1turn:
                    playersMagicSquare = x
                else:
                    playersMagicSquare = y
                sectionClicked, sectionAlreadyClicked = CheckSectionClicked(playersMagicSquare, mousePosition, sections, magicSquare)
                if sectionClicked != 0:
                    if not sectionAlreadyClicked:
                        player1turn = not player1turn
                        MakeMove(player1turn, sectionClicked[0], game)
                        pygame.display.update()
                        won = CheckWin(playersMagicSquare, won)
        for section in sections:
            if not section[1]:
                tie = False
        if tie and not won:
            Tk().wm_withdraw()
            answer = messagebox.askquestion("Tied Game", "Play again?")
            if answer == "yes":
                gamesPlayed += 1
                game, sections, player1, player2 = setBoardUp(gamesPlayed, player1Wins, player2Wins)
                magicSquare = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
                x = []
                y = []
            else:
                run = False
    pygame.quit()





