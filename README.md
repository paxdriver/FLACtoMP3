# FLACtoMP3 @paxdriver's repository

============== PYTHON VERSION ==================
FLAC to MP3 converter for batch of audio files using LAME encoder and preserving album art, playlists, metadata, etc if present in the source folder (and simpler bash version)

The python script will copy the contents of the source folder into a new folder called "mp3" so that album art and playlists are copied and in the same folder as the new mp3's

- First argument is for the source directory where the FLAC are located, default is currect directory.
- Second argument is for the target directory, where the MP3's and copied supporting files are supposed to go.

Running this script with no arguments will use local directory for the music and create an mp3 folder in the same location for the converted outputs.

============== EXAMPLES ========================
    1) script is next to a folder called demo which contains various flac files and folder art:
        "python flacToMp3.py ./demo . 256" -> this would copy the files from ./demo and create a folder ./mp3 to perform the conversions and encode the output at 256 bit
    2) script is in the same folder as the music and supporting files:
        "python flacToMp3.py" -> this will convert it all at CD quality 320kbps and store the output in a new mp3 folder in the same directory


============== BASH VERSION ====================

The bash version of the script is much simpler: put the script in the folder adjacent to the flac files you want converted, then run the script. An "mp3" folder is created with the CD quality audio tracks with the metadata and a copy of any album art or playlists also located adjacent to the flac files and the script. It copies the originals before performing any encoding then removes them when it's done so that file corruption of the originals isn't possible.
