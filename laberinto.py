#!/usr/bin/python3
#########################################################
# Create, print and resolve a console based laberinth
# python3 laberinto.py 
# 2020 - Antonio Royo Moraga
##########################################################
import time
import curses
from curses import wrapper
import random

def main(stdscr):
    #Wall colour
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #Laberinth path colour
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    #Colour of the text messages
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    #Resolution path colour
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    #The laberinth is initially filled with the border character (space) and the wall character (#)
    #The laberinth has a fixed size in each execution
    maxH = 35 
    maxV = 23
    A = []
    A.append("                                   ")
    for i in range (1,maxV-1,1):
        A.append(" ################################# ")
    A.append("                                   ")

    #Initialize the address counter that stores addresses in pairs V, H (Vertical, Horizontal)
    C = []
    C.append([0,0])
    #Flag to end the main loop
    finalizado = False
    #Start position is initially assigned
    V = 13
    H = 3
    A [V] = A [V-1][:H] + "O" + A [V-1][H+1:]
    #We print the laberinth on the screen for the first time
    for i in range (0,maxV-1,1):
        stdscr.addstr(i,0,A[i], curses.color_pair(1))
    #Function to count the number of open paths from a given position
    def numCaminos():
        nonlocal V
        nonlocal H
        nonlocal A
        nonlocal maxH
        nonlocal maxV
        caminos = 0
        if (V+2) < maxV :
            if A[V+2][H] == "#": caminos += 1
        if (V-2) >= 0:
            if A[V-2][H] == "#": caminos += 1
        if (H+2) < (maxH -2):
            if A[V][H+2] == "#": caminos += 1
        if (H-2) >= 0:
            if A[V][H-2] == "#": caminos += 1
        return caminos
    #Function to store the current position (in case we need to back track)
    def guardaPosic():
        nonlocal V
        nonlocal H
        nonlocal C
        temp = [V, H]
        C.append(temp)
    #Main loop to create the laberinth
    while not(finalizado):
        time.sleep (0.05) #Small delay to make the laberinth build more visually attractive
        LI = numCaminos()
        stdscr.refresh()
        if LI == 0: #What happens if there are no open paths from the current position
            #The last address stored in the address stack is popped up
            # as we back track when there are no open paths at a given point
            temp = C.pop()
            V = temp[0]
            H = temp[1]
            #If the returned address is (0,0) then the laberinth is done
            if H == 0 and V == 0:
                finalizado = True
        elif LI > 1: #What happens if there are more than one open path
            avanzando = False
            while not (avanzando):
                #Loop to create the laberinth
                stdscr.refresh()
                if (random.random() > 0.6 and V-2 > 0):
                    if (A[V-2][H] == "#"):
                        A[V-1] = A [V-1][:H] + "O" + A [V-1][H+1:]
                        A[V-2] = A [V-2][:H] + "O" + A [V-2][H+1:]
                        stdscr.addstr(V-1,H,"O", curses.color_pair(2))
                        stdscr.addstr(V-2,H,"O", curses.color_pair(2))
                        V -= 2
                        guardaPosic()
                        avanzando = True
                elif (random.random() > 0.5 and H+2 < maxH):
                    if (A[V][H+2] == "#"):
                        #old = len (A[V])
                        A[V] = A [V][:H] + "OO" + A [V][H+2:]
                        stdscr.addstr(V,H+1,"OO", curses.color_pair(2))
                        H += 2
                        guardaPosic()
                        avanzando = True
                elif (random.random() > 0.4 and V+2 < maxV):
                    if (A[V+2][H] == "#"):
                        A[V+1] = A [V+1][:H] + "O" + A [V+1][H+1:]
                        A[V+2] = A [V+2][:H] + "O" + A [V+2][H+1:]
                        stdscr.addstr(V+1,H,"O", curses.color_pair(2))
                        stdscr.addstr(V+2,H,"O", curses.color_pair(2))
                        V += 2
                        guardaPosic()
                        avanzando = True
                elif (random.random() > 0.3 and H-2 > 0):
                    if (A[V][H-2] == "#"):
                        A[V] = A [V][:H-2] + "OO" + A [V][H:]
                        stdscr.addstr(V,H-2,"OO", curses.color_pair(2))
                        H -= 2
                        guardaPosic()
                        avanzando = True
        elif LI == 1: #What happens if there are more than one open path
            stdscr.refresh()
            if (random.random() > 0.6 and V-2 > 0):
                if (A[V-2][H] == "#"):
                    A[V-1] = A [V-1][:H] + "O" + A [V-1][H+1:]
                    A[V-2] = A [V-2][:H] + "O" + A [V-2][H+1:]
                    stdscr.addstr(V-1,H,"O", curses.color_pair(2))
                    stdscr.addstr(V-2,H,"O", curses.color_pair(2))
                    V -= 2
                    guardaPosic()
                    avanzando = True
            elif (random.random() > 0.5 and H+2 < maxH):
                if (A[V][H+2] == "#"):
                    #old = len (A[V])
                    A[V] = A [V][:H] + "OO" + A [V][H+2:]
                    stdscr.addstr(V,H+1,"OO", curses.color_pair(2))
                    H += 2
                    guardaPosic()
                    avanzando = True
            elif (random.random() > 0.4 and V+2 < maxV):
                if (A[V+2][H] == "#"):
                    A[V+1] = A [V+1][:H] + "O" + A [V+1][H+1:]
                    A[V+2] = A [V+2][:H] + "O" + A [V+2][H+1:]
                    stdscr.addstr(V+1,H,"O", curses.color_pair(2))
                    stdscr.addstr(V+2,H,"O", curses.color_pair(2))
                    V += 2
                    guardaPosic()
                    avanzando = True
            elif (random.random() > 0.3 and H-2 > 0):
                if (A[V][H-2] == "#"):
                    A[V] = A [V][:H-2] + "OO" + A [V][H:]
                    stdscr.addstr(V,H-2,"OO", curses.color_pair(2))
                    H -= 2
                    guardaPosic()
                    avanzando = True

    #Final messages and build algorithm closure
    stdscr.addstr(maxV-1,0,"Wall symbol: #  Laberinth path: O", curses.color_pair(3))
    stdscr.addstr(0,0,"Finished! Press a key to solve     ", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()
    ##############################################
    #Algorithm to solve the laberinth
    ##############################################
    #We always start at this position
    V = 1
    H = 1
    #The direction variable means the way to follow. 0 -> right, 1 -> down, 2 -> left, 3 -> up
    #Always starts with direction 0
    direction = 0
    #Coordinates of the next laberinth cell to try. Initially equal to the start position
    nV = V
    nH = H
    #Resolution coordinates
    fV = 21
    fH = 33
    #Create a copy of the laberith for the resolution algorithm
    B = A.copy()
    #List to host all the coordinates in case we have to back up
    caminoRetroceso = [[V,H,direction]]
    retroceder = False

    stdscr.addstr(0,0,"Starting laberith resolution       ", curses.color_pair(4))
    stdscr.refresh()
    finalizado = False

    #Loop to search for a solution
    while not(finalizado):
        time.sleep (0.1) #Small delay to make the laberinth resolution visually more attractive
        #stdscr.getkey() # Debugging
        retroceder = False
        #Check for termination
        if (V == fV and H == fH):
            #Final messages and algorithm closure
            stdscr.addstr(maxV-1,0,"Exit path: *                       ", curses.color_pair(3))
            stdscr.addstr(0,0,"Exit found! Press a key to exit    ", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getkey()
            finalizado = True
        if (B[V][H] == "O"):
            B[V] = B [V][:H] + "*" + B [V][H+1:]
            stdscr.addstr(V,H,"*", curses.color_pair(4))
            stdscr.addstr(0,0,"Direction: " + str(direction) + "  H: " + str(H) + " V: " + str(V) + "        ", curses.color_pair(4))
            stdscr.refresh()
            if (direction == 0 and B[V+1][H] == "O"):
                nV = nV + 1
                direction = 1
            elif (direction == 0 and B[V][H+1] == "O"):
                nH = nH + 1
                direction = 0
            elif (direction == 0 and B[V-1][H] == "O"):
                nV = nV - 1
                direction = 3
            elif (direction == 1 and B[V][H-1] == "O"):
                nH = nH -1
                direction = 2
            elif (direction == 1 and B[V][H+1] == "O"):
                nH = nH + 1
                direction = 0
            elif (direction == 1 and B[V+1][H] == "O"):
                nV = nV + 1
                direction = 1
            elif (direction == 2 and B[V-1][H] == "O"):
                nV = nV - 1
                direction = 3
            elif (direction == 2 and B[V+1][H] == "O"):
                nV = nV + 1
                direction = 1
            elif (direction == 2 and B[V][H-1] == "O"):
                nH = nH - 1
                direction = 2
            elif (direction == 3 and B[V][H+1] == "O"):
                nH = nH + 1
                direction = 0
            elif (direction == 3 and B[V][H-1] == "O"):
                nH = nH - 1
                direction = 2
            elif (direction == 3 and B[V-1][H] == "O"):
                nV = nV - 1
                direction = 3
            caminoRetroceso.append([V,H,direction])
        else:
            retroceder = True
            while (retroceder):
                time.sleep (0.1) #Small delay to make the laberinth resolution visually more attractive
                temp = caminoRetroceso.pop()
                nV = temp[0]
                nH = temp[1]
                direction = temp[2]
                B[nV] = B [nV][:nH] + "O" + B [nV][nH+1:]
                stdscr.addstr(nV,nH,"O", curses.color_pair(2))
                stdscr.addstr(0,0,"Direction: " + str(direction) + "  H: " + str(nH) + " V: " + str(nV) + "        ", curses.color_pair(4))    
                stdscr.refresh()
                #stdscr.getkey() # Debugging   
                if (random.random() > 0.6 and B[nV-1][nH] == "O"):
                    direction = 3
                    retroceder = False
                elif (B[nV][nH-1] == "O"):
                    direction = 2
                    retroceder = False
                elif (random.random() > 0.6 and B[nV+1][nH] == "O"):
                    direction = 1
                    retroceder = False
                elif (random.random() > 0.6 and B[nV][nH+1] == "O"):
                    direction = 0
                    retroceder = False    
        V = nV
        H = nH
wrapper(main)


