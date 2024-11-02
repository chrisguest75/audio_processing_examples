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

## Resources

* https://github.com/deezer/spleeter?tab=readme-ov-file