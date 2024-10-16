#!/bin/bash

# make new directory to store mp3 version and playlists
mkdir -p mp3

# copy all files except this script to the new folder
find . -type f -not -name "$(basename "$0")" -exec cp {} mp3/ \;

cd mp3

for file in *.flac; do
    output="${file%.flac}.mp3"
    lame -b 320 --add-id3v2 "$file" "$output" && rm "$file"
    done

echo "FLAC to MP3 conversion script complete! Make sure the conversion worked by inspecting the new mp3 folder."
