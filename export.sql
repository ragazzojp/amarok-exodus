SELECT
    d.lastmountpoint AS root,
    u.rpath AS rel_path,
    aar.name AS album_artist,
    a.name AS album,
    t.discnumber AS disc_n,
    t.tracknumber AS track_n,
    ar.name AS artist,
    t.title AS title,
    s.rating AS rating
  FROM tracks t
    JOIN urls u ON (t.url = u.id)
    JOIN devices d ON (u.deviceid = d.id)
    LEFT JOIN albums a ON (t.album = a.id)
    LEFT JOIN artists ar ON (t.artist = ar.id)
    LEFT JOIN artists aar ON (a.artist = aar.id)
    JOIN statistics s ON (t.id = s.id);
