"""
Would like functionality to be able to input:

1)desired key
2)number of steps up or down

that means we need to be able to:
    1. figure out the key of the song
    2. calculate how many steps needed

main problem:
    once you have the number of steps up or down, how do you determine which of the x#/yb to use?


0 = A
1 = A#/Bb
2 = B
3 = C
4 = C#/Db
5 = D
6 = D#/Eb
7 = E
8 = F
9 = F#/Gb
10 = G
11 = G#/Ab

"""
chord_vals = [[u"A",u"A#",u"B",u"C",u"C#",u"D",u"D#",u"E",u"F",u"F#",u"G",u"G#"],
              [u"A",u"Bb",u"B",u"C",u"Db",u"D",u"Eb",u"E",u"F",u"Gb",u"G",u"Ab"]]


#param: line, target_count is the count at the point a series of letters is considered a word
# and therefore rejected because it is a lyric line
def chord_line(line):
    #params
    word_target = 5
    space_target = 3

    word_count = 0
    letter_count = 0
    space_count = 0
    max_word = 0
    max_space = 0

    for letter in line:

        if unicode.isspace(letter):
            word_count = 0 #reset word count
            space_count += 1

        else:
            word_count += 1
            letter_count += 1
            space_count = 0 #reset space count

        if space_count > max_space: max_space = space_count
        if word_count > max_word: max_word = word_count

    if max_space >= space_target:
        return True

    if max_word >= word_target:
        return False

    #blank lines are not chord lines
    if letter_count == 0:
        return False

    #default return True
    return False


def transpose_chord(input_chord, num_steps, sharp):

    new_chord = input_chord

    chords = input_chord.split("/")

    for chord in chords:

        chord_matches = []

        #iterate through chords and see if any match
        for val, chord_match in enumerate(chord_vals[0]):

            index = chord.find(chord_match)

            if index != -1:

                chord_matches.append((val, chord_match, len(chord_match.decode("utf-8"))))

        #find best chord match (longest one)
        val = max(chord_matches, key = lambda i:i[2])[0]
        chord_match = max(chord_matches, key = lambda i:i[2])[1]

        new_val = ((val + num_steps) % 12)

        if sharp:
            #lowercase version of the chord, as a mark to indicate it has been replaced, preventing duplicate replacement
            new_chord = new_chord.replace(chord_match, chord_vals[0][new_val].lower())

        else:
            new_chord = new_chord.replace(chord_match, chord_vals[1][new_val].lower())


    return new_chord


