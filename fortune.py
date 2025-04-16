# fortune.py - Version 1.0

def main():
    name = "Archisman Roy"
    admission_number = "21JE0152"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("✨ Your fortune: Better days are coming. Hang in there. ✨")
    elif mood == "neutral":
        print("✨ Your fortune: Something unexpected will bring you joy today. ✨")
    else:
        print("❗ Please enter a valid mood (happy/sad/neutral).")

if __name__ == "__main__":
    main()
