import docx2txt
from transpose_functions import *

def transpose():
    # temporary filename
    filename = "test_songsheet.docx"

    #parameters
    num_steps = 3
    sharp = True

    raw_text = docx2txt.process(filename)
    print raw_text
    text = unicode.splitlines(raw_text)
    new_text = u""

    for line in text:
        #determine whether the line is lyric or chord
        if chord_line(line):

            #find the chords in a line
            chords = line.split()

            #replace chords with the right chords
            for chord in chords:

                new_chord = transpose_chord(chord, num_steps, sharp)
                line = line.replace(chord, new_chord)

            #once done replacing in line, change all back to uppercase
            line = line.upper()
            line = line.replace("M","m")  #correct any minors that accidentally made major

        new_text = new_text + line + "\n"

    print new_text

"""
OLD METHOD -- index through the line and replace at index, not working right now
for line in text:
    # determine whether line is a lyric line or a chord line:
    if chord_line(line, 4):

        chord = []
        chord_count = 0

        for ind, letter in enumerate(line):

            if letter.isalnum() and letter != "/":
                chord_count += 1
                chord.append(letter)

            elif chord_count != 0:
                #process chord
                val = chord_to_val(chord)

                if val == -99:
                    line[ind:ind + chord_count] = u"?"

                else:
                    val = ((val + num_steps) % 11) - 1
                    line[ind:ind+chord_count] = val_to_chord(val, sharp)

                chord = []
                chord_count = 0

"""












