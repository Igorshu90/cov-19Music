def numbers_to_notes(data, scale):
    tmp_data = [str(d) for d in data]
    str_data = ''

    for d in tmp_data:
        str_data += str(d)
    data = []
    for d in str_data:
        data.append(int(d))
    notes = []
    for d in data:
        notes.append(scale[d])

    return notes


def ajust_scale(scale):
    scale.extend([i + 12 for i in scale[:3]])
    return scale


def to_bars(notes, size):
    bar = []
    for i in range(0, len(notes), size):
        bar.append(notes[i: i + 3])
    return bar


def get_lengths(data,deads,sizes):
    n = len(sizes)
    deads = [x % n for x in deads]
    lengths = []
    for i, size in enumerate(data):
        lengths.append(sizes[i % len(sizes)])

    return lengths
