# Phase 2: Exporting Ratings from Amarok

Install MySQL if you don't have it already running. This procedure was tested with MySQL 5.7.

On (K)Ubuntu:

```bash
sudo apt install mysql-server
```

Connect to MySQL and create an empty database called `amarok`.

```bash
sudo mysql -u root -e "CREATE DATABASE amarok"
```

Note: many commands are prefixed with `sudo` and in general this should be avoided.
The reason for this is that (K)Ubuntu integrated MySQL in a way that requires
you being the super-user to administer the database. We'll use `sudo`
a couple of times to avoid creating a temporary user.

Stop the service, we're going in inject the Amarok files manually.

```bash
sudo service mysql stop

sudo cp ~/.kde/share/apps/amarok/mysqle/amarok/* /var/lib/mysql/amarok

sudo chown -R mysql:mysql /var/lib/mysql/amarok
```

We can then now restart the service.

```bash
sudo service mysql start
```

Let's check:

```bash
sudo mysql amarok -u root < inspect.sql
```

If the counts match the numbers of your music archive, we can proceed with exporting the data.

```base
sudo mysql amarok -u root --xml < export.sql > amarok_export.xml
```

The exported file, `amarok_export.xml`, should contain one `<row>` element per track, similar to the following:

```xml
  <row>
    <field name="root">/home</field>
    <field name="rel_path">./username/Music/Library/U2/1987. The Joshua Tree/01. Where The Streets Have No Name.flac</field>
    <field name="album_artist">U2</field>
    <field name="album">The Joshua Tree</field>
    <field name="disc_n" xsi:nil="true" />
    <field name="track_n">1</field>
    <field name="artist">U2</field>
    <field name="title">Where The Streets Have No Name</field>
    <field name="rating">9</field>
  </row>
```

Let's inspect the result and check if the export is successful:

```bash
less amarok_export.xml
```

Press `Q` to quit `less`.

Alternatively:

```base
cat amarok_export.xml | grep "<row>" | wc -l
```

You should see the same number you've seen above for the count of tracks.

Export is complete, you can now delete the database and stop the MySQL server.

```bash
sudo mysql -u root -e "DROP DATABASE amarok"

sudo service mysql stop
```

If you want, you can also uninstall MySQL this way:

```bash
sudo apt purge mysql-server
```
