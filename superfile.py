import random
from datetime import datetime


class User:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_points(self, points: int):
        self.score += points

    def __str__(self):
        return f"{self.name}: {self.score} points"


def play_game(user: User):
    print(f"Привіт, {user.name}!")
    print(f"Час запуску: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    for round_number in range(1, 6):
        points = random.randint(1, 20)
        user.add_points(points)
        print(f"Раунд {round_number}: +{points} очок")

    print("-" * 40)
    print("Гра завершена!")
    print(user)


def main():
    user = User("Vadym")
    play_game(user)


if __name__ == "__main__":
    main()