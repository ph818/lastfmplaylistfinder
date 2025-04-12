# lastfmplaylistfinder

This script looks through a scrobbles.csv from lastfm, or any compatible source, and finds repeating playlists. It may be useful for (re)discovering old playlists from a user's listening history.

Currently it finds a lot of duplicates, but ideally it would present trees of related playlists, with information about when they first appeared and when they diverged.

What you need:

* A csv to import. One possibility is https://lastfm.ghan.nl/export/ (via https://support.last.fm/t/how-can-i-download-backup-my-last-fm-scrobbling-data/171/2)

The script uses the artist, album, song title, and date/time fields to look through the file for 'n = 3' lines that repeat twice or more, not counting them if they are all from the same album. 
It displays repeating lines with a count of how  many times they repeated.


Future development ideas

Confounding variables:
* Sometimes the listener listened to a song more than once before moving to the next one. Playlist finder should still find these variants
* The time dimension provides useful context: songs listened to hours later may be a different listening 'session,' and not part of the playlist. The script currently ignores this information.
* User may have listened to just part of a playlist: a partial listen. Or part of the playlist, then some other songs, and then the second part. The program could find these too, and maybe have a setting to display them or not.
* Sometimes the csv is small (hundreds) sometimes large (tens of thousands) and the script is not yet efficient.


Advanced:
* listening history has traces of when the user first built the playlist, or listened to variants. It would be interesting to display related playlists in a representation that shows their change through time and relationship to each other.
* Possible format for above: a timeline showing a tree, branches, and diffs.
