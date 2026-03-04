"""
Lineup Optimizer

Inputs:  player stats, available players
Output:  optimal formation + lineup maximizing expected goal differential

Data schema expected:
{
    "players": [
        {
            "name": str,
            "position": "field" | "goalkeeper",
            "stats": {
                "goals": int,
                "assists": int,
                "shots": int,
                "saves": int,          # goalkeeper only
                "goals_conceded": int  # goalkeeper only
            }
        }
    ]
}
"""

def optimize_lineup(players: list) -> dict:
    # TODO: implement optimizer
    pass

def run():
    print("\n--- Lineup Optimizer ---")
    # TODO: load player data and run optimize_lineup
    pass