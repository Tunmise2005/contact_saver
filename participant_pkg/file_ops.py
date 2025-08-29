import csv
from pathlib import Path

def save_participant(path: Path, participant: dict):
    
    file_exists = path.exists()

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Phone", "Track"])

        
        if not file_exists:
            writer.writeheader()

        
        writer.writerow(participant)


def load_participants(path: Path):
    
    participants = []
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                participants.append(row)
    return participants
