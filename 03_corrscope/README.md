# CORRSCOPE

Corrscope is named because it cross-correlates the input wave and a history buffer, to maximize wave alignment between frames.  

TODO:

* Render from yaml - `pipenv run corr ./radio6.yaml`
* 

## Start

```sh
# required in terminal if using pipenv
# for vscode
export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VENV_IN_PROJECT=1

# install
just install
pipenv install "corrscope[qt5]"
```

## Run

```sh
# run app
pipenv run corr
```

## Content

```sh
mkdir -p ./out
ffmpeg -hide_banner -i http://lstn.lv/bbc.m3u8?station=bbc_6music&bitrate=96000 -ss 00:00:00 -t 00:02:00 ./out/radio6.mp3

ffmpeg -i ./out/radio6.mp3 ./out/radio6.wav
vlc ./out/radio6.wav
```

## Render

You need a master audio as the mixed version.  
Each channel is passed seperately for oscilloscope.  

```sh
pipenv run corr --audio ./out/radio6.wav --write --render ./out/radio6_2.mp4 ./out/radio6.wav
vlc ./out/radio6_2.mp4
```

## Resources

- https://github.com/corrscope/corrscope
- https://corrscope.github.io/corrscope/