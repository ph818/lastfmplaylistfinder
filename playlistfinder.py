# Detects playlists in listening history

"""
Plan:
    import csv( Downloaded from https://lastfm.ghan.nl/export/ via
    https://support.last.fm/t/how-can-i-download-backup-my-last-fm-scrobbling-data/171/2 )
    look through the file for tunable 'minsongs = 3' songs that repeat 'minrepeat = 2' times or more
    use recursive method to determin the maximum version of that sequence which repeats minrepeat times.
    Display the sequence with a count of how many times it repeated.

Confounding variables:

    Sometimes the listener listened to a song more than once before moving to the next one. Playlist finder should still find these variants
    The time dimension provides useful context: songs listened to hours later would be a different 'session'
    User may have listened to just part of the playlist: partial listen. Or part of the playlist, some other songs, and the second part. The program should find these too, and maybe have a setting to display them or not.
    Sometimes the csv is small (hundreds) sometimes large (tens of thousands)

Advanced:

    Listening history has traces of when the user first built the playlist, or listened to variants. It would be interesting to display related playlists in a representation that shows their change through time and relationship to each other.
    Possible format for above: a timeline showing a tree, branches, and diffs.

Feature Request:

    input a sequence of tracks to look for

"""


from sys import argv, exit
from csv import reader, DictReader
from more_itertools import windowed


def main():
    if len(argv) != 2:
        print("Usage: python playlistfinder.py [ListeningHistory.csv]")
        exit(1)

    # Create dictionary names:
    dictartists = {}
    dictalbums = {}
    dictsongs = {}

    # CSV Format: Artist,Album,Song,Date 24h Time
    # example   : Flying Lotus,You're Dead!,Stirring,14 Aug 2022 16:34

    with open(argv[1], newline='') as csvfile:
        names = ('artist', 'album', 'song', 'date')
        for line in DictReader(csvfile, fieldnames=names):
            dictartists[line['date']] = line['artist']
            dictalbums[line['date']] = line['album']
            dictsongs[line['date']] = line['song']

    # Convert 2D problem to 1D by making everything a string.
    # Do I need to use .strip()?

    listofkeys = list(dictsongs.keys())
    listofsongs = list(dictsongs.values())
    # This is not giving me a concatenated string like I expect
    strofsongs = "".join(dictsongs.values())

    # TODO: Make These into runtime arguments
    minsongs = 3
    mincount = 2

    # This makes a sequence 'minsongs' long to check the big list against
    songwindows = windowed(listofsongs, minsongs)
    keywindows = windowed(listofkeys, minsongs)

    # These are generator objects with 3 things each...?
    for wkeys, wsongs in zip(keywindows, songwindows):

        # Test if all are from same album
        samealbum = True
        for i, key in enumerate(wkeys):
            if i == 0:
                testalbum = dictalbums[key]

            if dictalbums[key] != testalbum:
                samealbum = False
                break
        if samealbum:
            continue

        # Make a string to test against
        teststr = "".join(wsongs)
        testcounter = 0

        # Find how many times teststr repeats
        # Feature Request rewrite to see if it occurs 'min_repetitions' times.
        testcount = strofsongs.count(teststr)
        if testcount >= mincount:
            # debug
            print(f"Found {testcount} instances of {teststr}")

            # ToDo: call recursive function to get max number of songs in recurring sequence.

        # how will I store the results? List of lists of songs? Dict of first song (key) + n repeats?

'''You can take all the rows, order them by timestamp,
then put every run of three songs (that isn't from the same album i guess) into a Counter

https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed
or https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.peekable'''


main()
