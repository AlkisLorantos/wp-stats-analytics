"""
Shot Quality Calculator (xG model)

Inputs:  shot location [x, y], game state, goalkeeper position
Output:  goal probability (0.0 - 1.0)

Data schema expected:
{
    "location": [x, y],        # x: 0-100 (width), y: 0-100 (depth)
    "game_state": int,         # score differential at time of shot
    "goalkeeper_pos": [x, y],  # goalkeeper position at moment of shot
    "player": str,
    "outcome": "goal" | "saved" | "missed"
}
"""

def calculate_xg(location: list, game_state: int, goalkeeper_pos: list) -> float:
    # TODO: implement xG model
    pass

def run():
    print("\n--- Shot Quality Calculator ---")
    # TODO: load match data and run calculate_xg
    pass