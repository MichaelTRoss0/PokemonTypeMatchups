class Params:
    with open('params.txt', 'r') as params:
        lines = params.readlines()

        chart = lines[0][8:]
        single_types_only = [1][20:]
        check_weightings = lines[2][19:]
        check_modifications = lines[3][22:]
        type_1 = lines[4][9:]
        type_2 = lines[5][9:]
        tera_type = lines[6][12:]
        ability = lines[7][10:]
        item = lines[8][7:]
        weather = lines[9][10:]
        terrain = lines[10][10:]
        move = lines[11][7:]
        effects_on_self = lines[12][18:]
        effects_on_opponent = lines[13][22:]
        effects_on_battle = lines[14][20:]
