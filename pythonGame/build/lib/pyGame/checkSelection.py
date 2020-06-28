import logging


def CheckSectionClicked(playersMagicSquare, mousePosition, sections, magicSquare):
    sectionClicked = 0
    sectionAlreadyClicked = False
    #first row
    if sections[0][0].collidepoint(mousePosition):
        logging.debug("Section 1 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[0]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[0][0])
    elif sections[1][0].collidepoint(mousePosition):
        logging.debug("Section 2 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[1]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[0][1])
    elif sections[2][0].collidepoint(mousePosition):
        logging.debug("Section 3 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[2]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[0][2])
    # second row
    elif sections[3][0].collidepoint(mousePosition):
        logging.debug("Section 4 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[3]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[1][0])
    elif sections[4][0].collidepoint(mousePosition):
        logging.debug("Section 5 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[4]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[1][1])
    elif sections[5][0].collidepoint(mousePosition):
        logging.debug("Section 6 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[5]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[1][2])
    # third row
    elif sections[6][0].collidepoint(mousePosition):
        logging.debug("Section 7 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[6]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[2][0])
    elif sections[7][0].collidepoint(mousePosition):
        logging.debug("Section 8 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[7]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[2][1])
    elif sections[8][0].collidepoint(mousePosition):
        logging.debug("Section 9 clicked:  %s: Row: %s Column: %s", mousePosition, mousePosition[0], mousePosition[1])
        sectionClicked = sections[8]
        if sectionClicked[1] == False:
            playersMagicSquare.append(magicSquare[2][2])
    if sectionClicked == 0:
        return sectionClicked, False
    if sectionClicked[1] == False:
        sectionClicked[1] = True
    else:
        sectionAlreadyClicked = True
    return sectionClicked, sectionAlreadyClicked