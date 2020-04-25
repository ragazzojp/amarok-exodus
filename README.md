# Amarok Exodus

I've invested so much time on my music library and Amarok, but it's now time to let it goo and migrate to Kodi.

## Exporting Ratings from Amarok

Install MySQL if you don't have it already running. This procedure was tested with MySQL 5.7.

On (K)Ubuntu:

```bash
sudo apt install mysql-server
```

Connect to MySQL and create an empty database called `amarok`.

```bash
sudo mysql -u root -e "create database amarok"
```

Then stop the service, we're going in inject the Amarok files manually.

```bash
sudo service mysql stop

sudo cp ~/.kde/share/apps/amarok/mysqle/amarok/* /var/lib/mysql/amarok

sudo chown mysql:mysql /var/lib/mysql/amarok/*
```

We can then now restart the service.

```bash
sudo service mysql start
```

Let's check:

```bash
sudo mysql amarok -u root -e "SHOW TABLES"

sudo mysql amarok -u root -e "SELECT COUNT(*) FROM tracks"

sudo mysql amarok -u root -e "SELECT COUNT(*) FROM albums"

sudo mysql amarok -u root -e "SELECT COUNT(*) FROM artists"

sudo mysql amarok -u root -e "SELECT COUNT(*) FROM statistics"
```

If the counts are correct, we can proceed with dumping the data.

```base
sudo mysql amarok -u root --xml -e "SELECT \
    d.lastmountpoint AS 'root', \
    u.rpath AS 'rel_path', \
    aar.name AS 'album_artist', \
    a.name AS 'album', \
    t.discnumber AS 'disc_n', \
    t.tracknumber AS 'track_n', \
    ar.name AS 'artist', \
    t.title, \
    s.rating \
  FROM tracks t \
    JOIN urls u ON (t.url = u.id) \
    JOIN devices d ON (u.deviceid = d.id) \
    LEFT JOIN albums a ON (t.album = a.id) \
    LEFT JOIN artists ar ON (t.artist = ar.id) \
    LEFT JOIN artists aar ON (a.artist = aar.id) \
    JOIN statistics s ON (t.id = s.id)" \
  > amarok_export.xml
```

Let's check the result:

```bash
less amarok_export.xml
```

Press `Q` to quit `less`.

Alternatively:

```base
cat amarok_export.xml | grep "<row>" | wc -l
```

You should see the same number you've seen above for the count of tracks.

Export is complete.
