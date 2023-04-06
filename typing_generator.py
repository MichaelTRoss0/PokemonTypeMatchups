class Typing:
    type_1 = 0              # Primary Type; an integer from 0 to 17, inclusive
    type_2 = 0              # Secondary Type; an integer from 0 to 17, inclusive
                            # If both types are the same, then the typing is single-typed
    name = 0                # The displayed name of the typing generated from its types

    # Defensive Statistics
    def_eff = {}            # Dictionary containing the lists of this typing's defensive effectiveness
    def_eff_M = {}          # Dictionary containing the lists of this typing's modified defensive effectiveness

    def_score = 0           # Value representing this typing's total defensive score
    def_score_W = 0         # Value representing this typing's total weighted defensive score
    def_score_diff = 0      # Value representing the difference in defensive score from weighting

    def_rank = 0            # Value representing this typing's defensive ranking
    def_rank_W = 0          # Value representing this typing's weighted defensive ranking
    def_rank_diff = 0       # Value representing the difference in defensive ranking from weighting

    def_score_M = 0         # Value representing this typing's total modified defensive score
    def_score_MW = 0        # Value representing this typing's total modified and weighted defensive score
    def_score_diff_M = 0    # Value representing the difference in defensive score from weighting with modifications

    def_rank_M = 0          # Value representing this typing's defensive ranking when modified
    def_rank_MW = 0         # Value representing this typing's weighted defensive ranking with modifications
    def_rank_diff_M = 0     # Value representing the difference in defensive ranking from weighting with modifications

    # Offensive Statistics
    off_eff = {}            # Dictionary containing the lists of this typing's offensive effectiveness
    off_eff_M = {}          # Dictionary containing the lists of this typing's modified offensive effectiveness

    off_score = 0           # Value representing this typing's total offensive score
    off_score_W = 0         # Value representing this typing's total weighted offensive score
    off_score_diff = 0      # Value representing the difference in offensive score from weighting

    off_score_M = 0         # Value representing this typing's total modified offensive score
    off_score_MW = 0        # Value representing this typing's total modified and weighted offensive score
    off_score_diff_M = 0    # Value representing the difference in offensive score from weighting with modifications

    # Composite Statistics
    comp_score = 0          # Value representing this typing's composite score
    comp_score_W = 0        # Value representing this typing's composite weighted score
    comp_score_diff = 0     # Value representing the difference in composite score from weighting

    comp_rank = 0           # Value representing this typing's composite ranking
    comp_rank_W = 0         # Value representing this typing's composite weighted score
    comp_rank_diff = 0      # Value representing the difference in composite score from weighting

    comp_score_M = 0        # Value representing this typing's composite modified score
    comp_score_MW = 0       # Value representing this typing's composite modified and weighted score
    comp_score_diff_M = 0   # Value representing the difference in composite score from weighting with modifications

    # Initialize a typing
    def __init__(self, t1, t2):
        self.type_1 = t1
        self.type_2 = t2
        self.name = name_typing(self.type_1, self.type_2)

# Find the name for a type, given an integer from 0 to 17
def get_type_name(t):
    type_name = {
        0:  "NORMAL",
        1:  "FIRE",
        2:  "WATER",
        3:  "ELECTRIC",
        4:  "GRASS",
        5:  "ICE",
        6:  "FIGHTING",
        7:  "POISON",
        8:  "GROUND",
        9:  "FLYING",
        10: "PSYCHIC",
        11: "BUG",
        12: "ROCK",
        13: "GHOST",
        14: "DRAGON",
        15: "DARK",
        16: "STEEL",
        17: "FAIRY"
    }

    return type_name.get(t, "???")

# Generate the name for a dual typing
def name_typing(t1, t2):
    primary = get_type_name(t1)

    if t1 == t2:
        return primary

    secondary = get_type_name(t2)

    return primary + "/" + secondary

# Generate a 2D dictionary of all possible type combinations
def generate_all_typings(gen=int):
    if gen == 1:
        num_types = 15
    elif gen == 2:
        num_types = 17
    elif gen == 6:
        num_types = 18
    else:
        num_types = 18

    typings = {}
    for t1 in range(num_types):
        typings[t1] = {}
        for t2 in range(t1, num_types):
            typings[t1][t2] = Typing(t1, t2)

    return typings
