# SPLEETER

Spleeter is Deezer source separation library with pretrained models.  

## Install

```sh
export POETRY_VIRTUALENVS_IN_PROJECT=1
export POETRY_VIRTUALENVS_CREATE=1

git clone https://github.com/Deezer/spleeter && cd spleeter

pyenv install
poetry install
```

## Run

Split the sounds.  

```sh
poetry run spleeter

poetry run spleeter separate -p spleeter:2stems -o output audio_example.mp3

# play seperation
vlc ./output/audio_example/accompaniment.wav 

vlc ./output/audio_example/vocals.wav 
```

## Four stems

Outputs vocals, drums, bass and other.  

```sh
poetry run spleeter separate -p spleeter:4stems -o output audio_example.mp3
```

## Remix

Remix the stems back together.  

```sh
ffmpeg -i ./bass.wav -i ./drums.wav -i ./other.wav -i ./vocals.wav  -filter_complex amix=inputs=4:duration=shortest ./remixed.mp3

vlc ./remixed
```

## Resources

* https://github.com/deezer/spleeter?tab=readme-ov-file