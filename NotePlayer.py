import pygame.midi
import time


class Note:
    def __init__(self, midi_number, length, volume):
        self.midi_number = midi_number
        self.length = length
        self.volume = volume


class NotePlayer2:
    # initiate pygame MIDI ----------------------------------------------------------
    pygame.midi.init()

    # this class use pygame.midi.Output object to play notes with midi numbers

    # cons
    # diff parameter is the difference between first note and rest of the notes in bar
    def __init__(self, device=0, diff=0, instrument=1, bpm=0):
        self.player = pygame.midi.Output(device)
        self.player.set_instrument(instrument)
        self.bpm = bpm
        # seconds per single beet
        self.spb = 60 / bpm
        self.diff = diff

    # this method play note , the note represented by tuple , first element is midi number
    # and the second element is note length
    def go(self, note):
        self.player.note_on(note.midi_number,  note.volume)
        time.sleep(note.length * self.spb)
        self.player.note_off(note.midi_number, note.volume)

    # this play bar
    def play_bar(self, notes):
        self.go(notes[0])
        for note in notes[1:]:
            self.go(note)

    def play_accord(self, notes, volume, length):
        for note in notes:
            self.player.note_on(note, volume)
        time.sleep(length)
        for note in notes:
            self.player.note_on(note, volume)

    def close(self):
        self.player.close()
