"""
Match Timeline Builder

Inputs:  match events from JSON file
Output:  visual scrubber reconstructing the match event by event

Data schema expected:
{
    "match_id": str,
    "teams": [str, str],
    "events": [
        {
            "time": int,           # seconds from match start
            "type": "shot" | "goal" | "foul" | "exclusion" | "timeout" | "substitution",
            "team": str,
            "player": str,
            "location": [x, y],    # optional, for shots
            "outcome": str         # optional, for shots
        }
    ]
}
"""

def build_timeline(match: dict) -> list:
    # TODO: parse events and build ordered timeline
    pass

def render_timeline(timeline: list):
    # TODO: render timeline to terminal or plot
    pass

def run():
    print("\n--- Match Timeline Builder ---")
    # TODO: load match file and run build_timeline + render_timeline
    pass