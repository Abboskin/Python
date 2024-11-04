from tabulate import tabulate
notes = [
    [1, "Doing Homework"],
    [2, "Cleaning Room"],
    [3, "Prepare Meal"],
    [4, "Go to Gym"]
]

def show_notes():
    print("\nCurrent Notes:")
    if notes:
        print(tabulate(notes, headers=["ID", "Text"], tablefmt="rounded_grid"))
    else:
        print("No notes available.\n")

def show_note_details(note_id):
    for note in notes:
        if note[0] == note_id:
            print(f"Details of Note {note_id}: {note[1]}")
            return
    print("Note not found.")

def create_note(text):
    new_id = max([note[0] for note in notes], default=0) + 1
    notes.append([new_id, text])
    print("Note created successfully.")

def update_note(note_id, new_text):
    for note in notes:
        if note[0] == note_id:
            note[1] = new_text
            print("Note updated successfully.")
            return
    print("Note not found.")

def delete_note(note_id):
    global notes
    notes = [note for note in notes if note[0] != note_id]
    print("Note deleted successfully.")

def start():
    show_notes()
    while True:
        print("\nChoose option:")
        print("1: Show all notes")
        print("2: Show note details")
        print("3: Create note")
        print("4: Update note")
        print("5: Delete note")
        print("Q: Quit")
        print("M: Menu")

        choice = input("Choice: ")
        if choice == "1":
            show_notes()
        elif choice == "2":
                note_id = int(input("Enter note ID: "))
                show_note_details(note_id)
        elif choice == "3":
            text = input("Enter note text: ")
            create_note(text)
        elif choice == "4":
            note_id = int(input("Enter note ID to update: "))
            new_text = input("Enter new text: ")
            update_note(note_id, new_text)
        elif choice == "5":
                note_id = int(input("Enter note ID to delete: "))
                delete_note(note_id)
        elif choice == "Q":
            print("Goodbye!")
            break
        elif choice == "M":
            continue
        else:
            print("Error!")
start()