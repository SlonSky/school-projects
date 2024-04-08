import guitarpro
import numpy as np
import csv

START = [1] * 12 * 4 + [0] * 12 * 5
END = [0] * 12 * 4 + [1] * 12 * 5

def make_data_matrix(measures_amount, base_duration):
    """ Make matrix of data with all music notes
        as features by columns and base_duration
        subdivison of note duration in track

    :param measures_amount: number of tacts
    :param base_duration: the smallest part of duration subdivision
    :return: formed data matrix as ndarray
    """

    base_labels = 'C C# D D# E F F# G G# A A# B'.split()

    # note_label + octave_num
    features = [l + str(i) for i in range(9) for l in base_labels]

    data = list()
    data.append(features)  # add header

    counts_num = int(measures_amount / base_duration)

    empty_object = [[0] * len(features)]
    data += empty_object * counts_num
    data.insert(1, START)
    data.append(END)

    return np.array(data, dtype=object)


def get_note_label(note, strings):
    """ Get note label from Note object and
    string of track's instrument

    :param note: Note object
    :param strings: list of GuitarString
    :return: string label of note consits of label and octave
    """

    notes = 'C C# D D# E F F# G G# A A# B'.split()

    note_string = strings[note.string - 1].value
    note_semitones = note_string + note.value
    octave, semitone = divmod(note_semitones, len(notes))

    return '{note}{octave}'.format(note=notes[semitone], octave=octave)


def get_note_counts(beat, base_duration):
    """ Get number of note counts after expanding
    by the smallest duration

    :param beat: guitarpro.models.Beat
    :param base_duration: the smallest duration to subdivide
    :return: number of counts of current note after splitting
             by the smallest duration
    """
    note_duration = 1 / beat.duration.value
    return int(note_duration / base_duration)


def write_note(note, data, current_point, counts_num):
    """ Write note to data matrix

    :param note: note string label
    :param data: data matrix
    :param current_point: number of row, time point,
           where the note starts
    :param counts_num: duration of note in counts
    :return: None
    """
    column = np.where(data[0] == note)[0]
    data[current_point:current_point + counts_num, column] = 1


def extract_data(track, base_duration):
    """ Extract data from track

    :param track: track of gtp composition
    :param base_duration: the smallest temporal step
    :return: data of track's notes with encoded START
             and END stored in ndarray
    """
    strings = track.strings  # get strings notes

    data = make_data_matrix(len(track.measures), base_duration)
    current_data_point = 2  # current row in data

    for measures in track.measures:  # explore tacts
        for voice in measures.voices:
            for beat in voice.beats:

                counts_num = get_note_counts(beat, base_duration)

                for note in beat.notes:
                    note_label = get_note_label(note, strings)
                    write_note(note_label, data, current_data_point, counts_num)

                current_data_point += counts_num
    return data


def extract_from_song(path, base_duration):
    """ Extract data from song

    :param path: filepath to the song (Windows format)
    :param base_duration: the smallest temporal step
    :return: data of track's notes with encoded START
             and END stored in ndarray
    """
    song = guitarpro.parse(path)
    track = song.tracks[0]
    return extract_data(track, base_duration)

def save_to_csv(name, data):
    """ Save data matrix to csv file

    :param name: name of csv file
    :param data: data matrix
    :return: None
    """
    with open(name, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def main(path, out, base_duration):

    from os import listdir

    a,b = base_duration.split('/')
    base_duration = int(a)/int(b)

    if path[-1] == '/':
        files = [f for f in listdir(path) if f.endswith(('.gp3', '.gp4', '.gp5'))]
        for i, filepath in enumerate(files):
            try:
                data = extract_from_song(path + filepath, base_duration)
                name = filepath.split('.')[0]
                save_to_csv('{out}{name}.csv'.format(out=out, name=name), data)
                print(name + ' extracted')
            except Exception as e:
                print(filepath, ' : ', e)
    else:
        if path.endswith(('.gp3', '.gp4', '.gp5')):
            data = extract_from_song(path, base_duration)
            name = path.split('.')[0]
            save_to_csv('{out}{name}.csv'.format(out=out, name=name), data)

if __name__ == '__main__':
    import argparse
    description = """
        Extract GP tabs and convert to CSV data in suitable format for machine learning.
        <input file/folder> <output folder> <base duration>
        """
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        metavar='source file/folder',
                        help='path to gtp file of folder with gtp files')
    parser.add_argument('out',
                        metavar='output folder',
                        help='path output folder')

    parser.add_argument('base_duration',
                        metavar='base duration',
                        help='base duration, e.g. 1/128')
    args = parser.parse_args()
    kwargs = dict(args._get_kwargs())
    main(**kwargs)