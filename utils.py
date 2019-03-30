def mod12(n):
    return n % 12


def note_name(number):
    notes = "C,C#,D,D#,E,F,F#,G,G#,A,A#,B".split(",")
    return notes[mod12(number)]
