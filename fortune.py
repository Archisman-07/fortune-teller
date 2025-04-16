# fortune.py - Version 1.1

import random

def main():
    name = "Archisman Roy"
    admission_number = "21JE0152"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "Your joy is contagious—spread it around!"
        ],
        "sad": [
            "Better days are coming. Hang in there.",
            "Tough times never last, but tough people do."
        ],
        "neutral": [
            "Something unexpected will bring you joy today.",
            "Stay steady. Peace is power."
        ],
        "stressed": [
            "Breathe in strength, breathe out stress.",
            f"Relax, {name}. You've got this!"
        ]
    }

    if mood in fortunes:
        print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
    else:
        print("❗ Please enter a valid mood (happy/sad/neutral/stressed).")

if __name__ == "__main__":
    main()
