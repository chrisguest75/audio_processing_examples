set dotenv-load := true

# default lists actions
default:
  @just -f justfile --list

getsource filepath="${SOURCE_AUDIO_FILE}":
  #!/usr/bin/env bash
  set -eufo pipefail
  mkdir -p ../sources/numbers/  
  #curl -vvv -L -o ./sources/numbers/numbers0-100englishpronouciation.zip https://archive.org/compress/numbers0-100englishpronouciation/formats=VBR%20MP3&file=/numbers0-100englishpronouciation.zip
  #unzip ./sources/numbers/numbers0-100englishpronouciation.zip -d ./sources/numbers/numbers0-100englishpronouciation

durations:   
  #!/usr/bin/env bash
  set -eufo pipefail
  set +f 
  for file in ../sources/numbers/numbers0-100englishpronouciation/*.mp3; do
    echo "Processing: ${file}"
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${file}"
  done

