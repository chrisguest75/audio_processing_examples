# VISQOL

Demonstrate how to use VisQOL.  

NOTE:

* Bazel build is a massive memory hog - check docker stats whilst building if you have issues.

## Build

```sh
# build
docker buildx build --load --memory 6GB -f Dockerfile.build -t visqol . 
docker run -it --rm -v $(pwd):/assets --memory 6GB --entrypoint /usr/bin/bash visqol

# rebuild if required
bazel-5.3.2 build :visqol -c opt
```

## Prepare

```sh
mkdir -p ./assets
ffmpeg -y -hide_banner -i "../output/LNL222_5sec_aac_wav_trim.wav" -ac 1 -ar 48000 "./assets/LNL222_5sec_aac_wav_trim_48khz.wav"

ffmpeg -y -hide_banner -i "../output/LNL222_5sec_ogg_wav_notrim.wav" -ac 1 -ar 48000 "./assets/LNL222_5sec_ogg_wav_notrim_48khz.wav"

ffmpeg -y -hide_banner -i "../output/LNL222.mp3.wav" -ac 1 -ar 48000 "./assets/LNL222_48khz.mp3.wav"
```


## Test

```sh
./bazel-bin/visqol --reference_file /assets/assets/LNL222_48khz.mp3.wav --degraded_file /assets/assets/LNL222_5sec_aac_wav_trim_48khz.wav --verbose --use_speech_mode --output_debug /assets/assets/debug.txt
```


## Resources

* https://github.com/google/visqol
* https://bazel.build/install/ubuntu
* https://github.com/bazelbuild/bazelisk
