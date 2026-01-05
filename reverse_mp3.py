#########################################################################################
# file: reverse_mp3.py
# type: Python
# date: 05_JANUARY_2026
# author: karbytes
# license: PUBLIC_DOMAIN 
#########################################################################################

"""
This Python program reverses the playback order of a specific MP3 file.

The input file path and output file path are explicitly defined
inside this source code file to ensure reproducibility and clarity.

The program performs the following steps:

1. Loads the input MP3 file from disk
2. Decodes the MP3 into raw audio samples
3. Reverses the order of those samples
4. Re-encodes the reversed samples as a new MP3 file
"""

import os
from pydub import AudioSegment

# -------------------------------------------------
# user-defined file paths (edit these as needed)
# -------------------------------------------------
input_mp3_path = "input_audio.mp3"
output_mp3_path = "input_audio_[reversed].mp3"

# -------------------------------------------------
# verify input file exists
# -------------------------------------------------
print("Input MP3 file path:")
print(input_mp3_path)

if not os.path.isfile(input_mp3_path):
    print("Error: input MP3 file does not exist.")
    raise SystemExit(1)

# -------------------------------------------------
# load MP3 file into memory
# -------------------------------------------------
print("Loading MP3 file into memory...")

audio_data = AudioSegment.from_file(
    input_mp3_path,
    format="mp3"
)

# -------------------------------------------------
# reverse audio samples
# -------------------------------------------------
print("Reversing audio samples...")

reversed_audio_data = audio_data.reverse()

# -------------------------------------------------
# write reversed audio to output file
# -------------------------------------------------
print("Writing reversed MP3 file:")
print(output_mp3_path)

reversed_audio_data.export(
    output_mp3_path,
    format="mp3",
    bitrate="192k"
)

# -------------------------------------------------
# completion message
# -------------------------------------------------
print("Done.")
print("Reversed MP3 file successfully created.")
