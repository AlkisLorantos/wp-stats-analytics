from modules.shot_quality import run as shot_quality_run
from modules.lineup import run as lineup_run
from modules.timeline import run as timeline_run

def menu():
    print("\n=== Water Polo Analytics ===")
    print("1. Shot Quality Calculator")
    print("2. Lineup Optimizer")
    print("3. Match Timeline Builder")
    print("0. Exit")
    return input("\nChoose: ").strip()

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            shot_quality_run()
        elif choice == "2":
            lineup_run()
        elif choice == "3":
            timeline_run()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")