import json
import pandas as pd
import NotePlayer
import DataToNote
from NotePlayer import Note


def main():

    with open('config.json', 'r') as configFile:
        data = configFile.read()

    config = json.loads(data)

    print('Start to play!!!')
    player = NotePlayer.NotePlayer2(bpm=config['bmp'], instrument=config['instrument'])
    df = pd.read_excel(config['path'])

    cases = df['new cases'].to_list()
    notes = DataToNote.numbers_to_notes(cases, config['bar'])
    dead = df['dead']
    lengths = DataToNote.get_lengths(notes, dead, config['lengths'])

    for i, note in enumerate(notes):
        print(notes[i])
        player.go(Note(notes[i], lengths[i], 127))
    player.close()

    print(df)


if __name__ == "__main__":
    main()

