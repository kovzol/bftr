Introduction
------------

Battle for the Ring is another game about the Middle Earth story. It is
heavily based on Mike Singleton's War in Middle Earth series, available
on PC and other platforms. For a reference video, watch the following
YouTube movies:

  * http://www.youtube.com/watch?v=Bt8HyMZFalQ
  * http://www.youtube.com/watch?v=fRgYua3R98Y
  * http://www.youtube.com/watch?v=PzOkwnsF4Po

Definitely, we would like to clone many details of this great game,
including its atmosphere, strategy game type, nice graphics, but we
would like to add some enhancements: network game for two players, even
better graphics and sound, and maybe more. It is important that we want
a non-violent friendly game without any blood and frightening parts.

At the moment graphics is borrowed from several third party artists.
Most artwork has a confirmed copyright (making the graphics available
for free), but if you feel any artworks here illegal to use, please
report it and we will substitute it with another file. Currently the
images are static, but we may change them to animated ones.

Battle for the Ring is written in Python 2.7 and PyGame. It can be
played with two players on two different computers. Another computer
("the server") is responsible for the fair play. Why Python? Well, this
is easy to learn for newcomers, and it is cross-platform enough.
(Another option would be HTML5 canvas.)

The server will store the gameplay data in an SQL database. Maybe there
will be performance issues on a slow server, but we hope there will be
no big issues. If yes, we can build up a memory based data storing for
the hot data, and only on save/load will the data be saved into the
database.

Clients will communicate with the server on a pre-defined protocol via
HTTP(S).

Installation
------------

On Ubuntu Linux 11.04, the python2.7 and python-pygame packages are
required. For editing the source code, any editor can be good enough.

On Windows, download the following pieces of software first:

  * http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi
  * http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi

The version number for Python is important: don't use any newer versions
(it will not work properly with PyGame, and it is also important not to
install the 64 bit version of Python since PyGame requires the 32 bit
version.)

For editing the source code, Notepad++ is suggested:
  
  * http://download.tuxfamily.org/notepadplus/6.1.5/npp.6.1.5.Installer.exe

During installing Python and PyGame, please choose the "Install for all
users" option, and also enter that PyGame should be installed for
"Python from another location: C:\Python27".

Current state
-------------

At the moment one can try the scrolling of the Middle Earth map by using
the arrow keys or the mouse (by pointing and clicking on the small black
arrow-like triangles), and view the initial amount of soldiers .

Authors and contribution
------------------------

Please feel free to join and contribute.

Authors (at the moment): Zoltan Kovacs <kovzol@matek.hu> and Benedek
Kovacs.
