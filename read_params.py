class Params:
    with open('params.txt', 'r') as params:
        lines = params.readlines()

        chart = lines[0][8:]
        checkWeightings = lines[1][18:]
        checkModifications = lines[2][21:]
        type1 = lines[3][8:]
        type2 = lines[4][8:]
        typeTera = lines[5][11:]
        ability = lines[6][10:]
        item = lines[7][7:]
        weather = lines[8][10:]
        terrain = lines[9][10:]
        move = lines[10][7:]
        effectsOnSelf = lines[11][16:]
        effectsOnOpponent = lines[12][20:]
