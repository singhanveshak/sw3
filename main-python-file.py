#ADDING COMMENTS SHOWING CHANGES

# Define the steps for each chord type
chord_steps = {
    "Major": [4, 7],
    "Minor": [3, 7],
    "Augmented fifth": [4, 8],
    "Minor fifth": [4, 6],
    "Major sixth": [4, 7, 9],
    "Minor sixth": [3, 7, 9],
    "Dominant seventh": [4, 7, 10],
    "Minor seventh": [3, 7, 10],
    "Major seventh": [4, 7, 11],
    "Diminished seventh": [3, 6, 10]
}

# Define the list of notes in order
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def get_chord_notes(key, chord_type):
    # Find the index of the key in the notes list
    start_index = notes.index(key)
    # Get the steps for the chord type
    steps = chord_steps.get(chord_type)
    
    if steps is None:
        return "Chord type not found."
    
    # Calculate the notes in the chord
    chord_notes = [notes[(start_index + step) % 12] for step in [0] + steps]
    return chord_notes

# Get input from the user
key = input("Enter the key (e.g., C, D, E): ")
chord_type = input("Enter the chord type (e.g., Major, Minor, Dominant seventh): ")

# Print the notes in the chord
chord_notes = get_chord_notes(key, chord_type)
print("The notes in the", key, chord_type, "chord are:", chord_notes)
