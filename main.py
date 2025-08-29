from pathlib import Path
from participant_pkg import file_ops


workspace = Path("workspace")
workspace.mkdir(exist_ok=True) 
csv_file = workspace / "contacts.csv"

while True:
   
    name = input("Enter participant name: ")
    
    
    age = int(input("Enter participant age: "))
    

    phone = input("Enter participant phone: ")
    while len(phone) != 11:
        print("Phone number not complete")
        phone = input("Enter participant phone: ")

    
    track = input("Enter participant track: ")
    
    participant = {
        "Name": name,
        "Age": age,
        "Phone": phone,
        "Track": track
    }

    
    file_ops.save_participant(csv_file, participant)
    print(f"Saved: {participant}")

    
    more = input("Add another participant? (y/n): ").lower()
    if more != "y":
        break


participants = file_ops.load_participants(csv_file)
print(f"Total participants: {len(participants)}")
for p in participants:
    print(f" - {p['Name']} ({p['Age']} yrs) | {p['Phone']} | {p['Track']}")
