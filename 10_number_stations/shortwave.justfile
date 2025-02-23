set dotenv-load := true

# default lists actions
default:
  @just -f justfile --list

sonic-visualiser file="${SOURCE_AUDIO_FILE}":
  #!/usr/bin/env bash
  set -eufo pipefail
  nix-shell -p sonic-visualiser --command "sonic-visualiser {{ file }}"

play filepath="${SOURCE_AUDIO_FILE}":
  vlc {{ filepath }}

samplerate-2400 filepath="${SOURCE_AUDIO_FILE}":
  #!/usr/bin/env bash
  set -eufo pipefail
  export OUTPUT_FOLDER="../output"
  export OUTPUT_FILE_2400="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_2400hz.wav"
  echo "OUTPUT_FILE_2400: ${OUTPUT_FILE_2400}"
  export OUTPUT_FILE_44100="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_44100hz.wav"
  echo "OUTPUT_FILE_44100: ${OUTPUT_FILE_44100}"

  ffmpeg -hide_banner -y -i {{ filepath }} -ar 2400 "${OUTPUT_FILE_2400}"
  ffmpeg -hide_banner -y -i "${OUTPUT_FILE_2400}" -ar 44100 "${OUTPUT_FILE_44100}"
  vlc "${OUTPUT_FILE_44100}"

lowpass filepath:
  #!/usr/bin/env bash
  set -eufo pipefail
  export OUTPUT_FOLDER="../output"
  export OUTPUT_FILE="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_lowpass.wav"
  echo "OUTPUT_FILE: ${OUTPUT_FILE}"
  ffmpeg -hide_banner -y -i "{{ filepath }}" -af "lowpass=f=2700" "${OUTPUT_FILE}"
  vlc "${OUTPUT_FILE}"

highpass filepath:
  #!/usr/bin/env bash
  set -eufo pipefail
  export OUTPUT_FOLDER="../output"
  export OUTPUT_FILE="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_highpass.wav"
  echo "OUTPUT_FILE: ${OUTPUT_FILE}"
  ffmpeg -hide_banner -y -i "{{ filepath }}" -af "highpass=f=300" "${OUTPUT_FILE}"
  vlc "${OUTPUT_FILE}"

shortwave filepath:
  #!/usr/bin/env bash
  set -eufo pipefail
  export OUTPUT_FOLDER="../output"
  export OUTPUT_FILE_2400="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_2400hz.wav"
  echo "OUTPUT_FILE_2400: ${OUTPUT_FILE_2400}"
  export OUTPUT_FILE_SHORTWAVE="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_shortwave.wav"
  echo "OUTPUT_FILE_SHORTWAVE: ${OUTPUT_FILE_SHORTWAVE}"

  ffmpeg -hide_banner -y -i {{ filepath }} -af "lowpass=f=2700,highpass=f=300" -ar 2400 "${OUTPUT_FILE_2400}"
  ffmpeg -hide_banner -y -i "${OUTPUT_FILE_2400}" -ar 44100 "${OUTPUT_FILE_SHORTWAVE}"
  vlc "${OUTPUT_FILE_SHORTWAVE}"


noise filepath noisetype="brown" amplitude="0.05":
  #!/usr/bin/env bash
  set -eufo pipefail
  export NOISE_TYPE={{ noisetype }}
  export OUTPUT_FOLDER="../output"
  export OUTPUT_FILE_NOISE="${OUTPUT_FOLDER}/{{ without_extension(file_name(filepath)) }}_noise.wav"
  echo "OUTPUT_FILE_NOISE: ${OUTPUT_FILE_NOISE}"
  ffmpeg -hide_banner -y -i "{{ filepath }}" -filter_complex "anoisesrc=color=${NOISE_TYPE}:amplitude={{ amplitude }}[noise];[0:a][noise]amix=inputs=2:duration=first:dropout_transition=3" -ar 44100 ${OUTPUT_FILE_NOISE}
  vlc ${OUTPUT_FILE_NOISE}
