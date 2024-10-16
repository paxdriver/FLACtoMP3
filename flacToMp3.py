import os
import shutil
import subprocess
import sys

README = '''This script will copy the contents of the source folder into a new folder called "mp3" so that album art and playlists are copied and in the same folder as the new mp3's

- First argument is for the source directory where the FLAC are located, default is currect directory.
- Second argument is for the target directory, where the MP3's and copied supporting files are supposed to go.

Running this script with no arguments will use local directory for the music and create an mp3 folder in the same location for the converted outputs.

============== EXAMPLES ========================
    1) script is next to a folder called demo which contains various flac files and folder art:
        "python flacToMp3.py ./demo . 256" -> this would copy the files from ./demo and create a folder ./mp3 to perform the conversions and encode the output at 256 bit
    2) script is in the same folder as the music and supporting files:
        "python flacToMp3.py" -> this will convert it all at CD quality 320kbps and store the output in a new mp3 folder in the same directory
'''

print(README)
 
def convert_flac_to_mp3(source_folder, target_folder, bitrate="320"):

    # Check that bitrate is a valid integer
    try:
        print(f"BITRATE for output: {int(bitrate)}kbps")
    except ValueError: 
        raise ValueError("Bitrate must be an integer value!!!")
    
    try:
        # Make a new output directory
        os.makedirs(target_folder, exist_ok=True)
        src_file = ''
        # Copy everything in the directory except this script into the output directory "mp3"
        # files = [file for file in os.listdir(source_folder) if file != os.path.basename(__file__)]  # (same as sys.argv[0] for getting this script's filename, but it's explicit to the full file path of this script)
        files = [file for file in os.listdir(source_folder) if file != sys.argv[0]]  # Ensures this script is never copied with the rest of the files if it is present in the listdir() output
        for file in files: 
            src_file = os.path.join(source_folder, file)
            if os.path.isfile(src_file):  # Only copy files, not directories
                print("Copying:", src_file)
                # copy files to ensure the originals are never touched
                shutil.copy2(src_file, os.path.join(target_folder, file))
            # shutil.copy2(os.path.join(source_folder, file), os.path.join(target_folder, file))  

        flac_files = [file for file in files if file.lower().endswith('.flac')]     # makes sure that "FLAC" and "flac" extensions are both compatible
        for flac_file in flac_files:
            mp3_file = f"{os.path.splitext(flac_file)[0]}.mp3"
            
            print("-"*25)
            print("Output MP3 file will be:", mp3_file)
            print("Converting:", os.path.join(target_folder, flac_file))
            print("Output MP3:", os.path.join(target_folder, mp3_file))
            print("-"*25)
            
            # LAME encoder used: captures metadata from flac files for new mp3 files
            command = ["lame", "-b", bitrate, "--add-id3v2", os.path.join(target_folder, flac_file), os.path.join(target_folder, mp3_file)]
            subprocess.run(command, check=True)
            os.remove(os.path.join(target_folder, flac_file))
        
        print("Conversion completed! Inspect the newly created mp3 folder for the converted tracks!")
    
    except FileNotFoundError as err:
        print(f"FileNotFound Error has occurred: {err}")
        sys.exit(1)
    except PermissionError as err:
        print(f"Permission Error has occurred: {err}")
        sys.exit(1)
    except subprocess.CalledProcessError as err:
        print(f"Subprocess Error has occurred: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"Exception Error has occurred: {err}")
        print(f"Problematic file: {src_file}")
        sys.exit(1)


if __name__ == "__main__":
    # Initialize values for when no arguments are provided to the script
    bitrate = "320"

    # Parse command line arguments (if present)
    number_of_arguments = len(sys.argv)         # sys.argv[0] is the name of the script being run

    source_folder = '.'
    target_folder = os.path.join(source_folder, 'mp3') if number_of_arguments < 3 else sys.argv[2]

    if number_of_arguments > 4:
        print("USAGE: python flacToMp3.py <source_directory> <target_directory> <integer bitrate>")
        sys.exit(1)

    if number_of_arguments >= 2:
        source_folder = sys.argv[1]
        target_folder = os.path.join(source_folder, 'mp3')  # Default target if only the <source> parameter is available
    if number_of_arguments >= 3:
        target_folder = sys.argv[2]
    if number_of_arguments == 4:
        bitrate = str(sys.argv[3])

    convert_flac_to_mp3(source_folder, target_folder, bitrate)
