import pandas as pd
import NotePlayer
import DataToNote
from NotePlayer import Note
from config import note_config, data_config


def main():
    print('Start to play!!!')
    player = NotePlayer.NotePlayer2(bpm=note_config['bmp'], instrument=note_config['instrument'])
    df = pd.read_excel(data_config['path'])

    cases = df['new cases'].to_list()
    notes = DataToNote.numbers_to_notes(cases, note_config['bar'])
    dead = df['dead']
    lengths = DataToNote.get_lengths(notes, dead, note_config['lengths'])

    for i, note in enumerate(notes):
        print(notes[i])
        player.go(Note(notes[i], lengths[i], 127))
    player.close()

    print(df)
if __name__ == "__main__":
    main()

