# Phase 1: Tagging with MusicBrainz Picard

[MusicBrainz](https://musicbrainz.org) is an amazing project.

MusicBrainz is a live, curated database of all the music ever released.
An album is called `release`, while a song is called `recording`.
When a song is included in an album, it becomes a `track`.

We'll calculate and associate rating to releases and recordings.

Each release, recording and track have a unique ID in MusicBrainz.
MusicBrainz IDs are called MBIDs. Once added to files, they make
possible for player and library managers to analyze your music collection,
fix tags, detect missing songs, retrieve additional information like
lyrics, pictures, texts, ...

Please support MusicBrainz by [donating](https:/metabrainz.org/donate).

## Configure Picard

Tagging is the process of adding MBIDs to the files. For this purpose,
many tools are available but I suggest to use [Picard](https://picard.musicbrainz.org).

You can configure Picard as you prefer, but two options must **NOT** be set
for the rating export to work properly:

- Move files when saving
- Rename files when saving.

Make sure the options are disabled during the whole process.

## Tagging the collection

Now that Picard is configured, tag your whole collection following
the instructions on the [Quick Start](https://picard.musicbrainz.org/quick-start).

Proper tags are mandatory for the rating export to work.

It's also important that files are left where they are with the name they have,
therefore I asked you not to enable the two options above.

It may take a while to tag all the files you have, but the investment
is really worth. With a properly-tagged library, you'll have
uniform artist and album artist names, well-curated tags, and more.
