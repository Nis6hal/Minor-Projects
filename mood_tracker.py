
import csv
from datetime import datetime

FILENAME = "mood_log.csv"

def get_mood():
    mood = input("How are you feeling today? (happy/sad/angry/excited/etc.): ").strip().lower()
    notes = input("Any notes for today? (Optional): ").strip()
    return mood, notes

def save_mood(date, mood, notes):
    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood, notes])
    print(f"✅ Mood saved for {date}!")

def main():
    print("📝 Welcome to the Daily Mood Tracker!")
    date = datetime.now().strftime("%Y-%m-%d")
    mood, notes = get_mood()
    save_mood(date, mood, notes)

if __name__ == "__main__":
    main()
