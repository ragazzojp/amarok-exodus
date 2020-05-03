# The Exodus from Amarok

I've invested so much time on my music library and [Amarok](https://amarok.kde.org),
but it's now time to let it go and migrate to a different, more modern solution.

This repository is developed to document and keep track of the migration to MusicBrainz and Kodi.
It contains simple scripts and tools I wrote for myself and I leave here for others.

## Why

Maintaining ratings and a large music archive on a single Amarok instance is becoming impossible.
The main reason is that music is not consumed anymore in front of a monitor. A music consumption experience
solely on the desktop or laptop is now limiting. Accessing musics over the network, on multiple devices,
on smartphones, on the go, from the workplace, from the living room with proper hearphones or amplifier,
is the way many people including me would like to consume their own music.

Listening, but also maintaining the music archive, adding, tagging, cleaning, removing and rating songs
can still be an activity performed primarily on a deskopt or laptop, but the music archive and,
in particular, music ratings can't be locked inside one single software.

Last but not least, in the last years the development of Amarok almost stalled. While it's still ok
to use it as media player and music collection manager, there are better alternatives.

## The Goal

The goal is to move the music archive to a folder on a [NAS](https://openmediavault.org) or to any
other directory or location from where it can be directly played, accessed remotely (e.g. via DLNA),
served over the network with some sort of web music player, cached on smartphones, served
to connected amplifiers or Kodi installations on smart TVs, Raspberry PIs or Amazon TV sticks.

That would be (relatively) easy unless you have rated all the songs over more than 15 years.

This is my case. I don't want to lose my ratings. Instead, I want to keep them somewhere,
so that they're presented back to me on compatible music players like Kodi. In addition,
I want the possiblity to update the ratings while listening to the music.

Last but not least, the solution should offer the possibility of a complete backup and restore.

## The Plan

It's still not 100% clear but so far this is plan:

- [MusicBrainz](http://musicbrainz.org) is the central piece of the solution.
  MusicBrainz is an open music encyclopedia that collects music metadata and makes it available to the public.
  I'll use MusicBrainz identifiers (MBID) to uniquely identify songs and associate ratings to them.

- [Phase 1](tagging.md): all the songs in the archive must be tagged via [MusicBrainz Picard](https://picard.musicbrainz.org),
  a wonderful tool to tag your music. It fixes and completes tags, remove unwanted tags, make sure all the songs
  have proper MusicBrainz identifiers (MBID) for themselves but also for albums and authors.
  It puts order in the chaos and gives you the fantasting feeling that everything is under control.

- [Phase 2](export.md): export the ratings from Amarok to a file. Since Amarok does not store
  the MusicBrainz identifiers for the songs, this file won't have any MBIDs.
  This is a problem we'll solve later.

- [Phase 3](associate.md): associate ratings to the MBIDs and produce a mapping containing all your ratings.
  This will be the only file, in addition to the music files themselves, that must be saved from Amarok.
  Once done, you and your ratings will be independent not only from Amarok, but from any other
  specific software and from details like in which directory files are stored, file names and formats,

- [Phase 4](sync.md): upload and sync your ratings with your account on MusicBrainz (TBC).

- [Phase 5](import.md): import your ratings back to players, like Kodi (TBC).
