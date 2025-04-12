# NOISE

TODO:

* Denoise
* Check the impact
* Measure the impact of denoise.  
* PSNR - NOT WORKING YET
* Perceptual Evaluation of Audio Quality (PEAQ)
  * https://github.com/gonshell/peaq
  * https://github.com/NikolajAndersson/PEAQ
* Short-Time Objective Intelligibility (STOI)
* Log-Spectral Distance (LSD)

## Sources

```sh
# generate some brownian noise with an amplitude of 1 using audacity plugin.  
audacity

just sources
```

## Measure

```sh
mkdir -p ./out

# get baseline stats
just measure-levels ../sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3/english_coventrycarol_unknown_rg_64kb.mp3 > ./out/baseline.txt
```

## Mix Noise

Mix in noise types.  

```sh
just mix-pink-noise 0.1
just mix-brown-noise 0.1
```

## Measure New Noise Floor

Measure stats with noise mixed in.  

```sh
just measure-levels ../output/noise/english_coventrycarol_unknown_rg_64kb_pinknoise.mp3 > ./out/pink.txt
just measure-levels ../output/noise/english_coventrycarol_unknown_rg_64kb_brownnoise.mp3 > ./out/brown.txt

# NOT WORKING YET
just measure-psnr ../output/noise/english_coventrycarol_unknown_rg_64kb_pinknoise.mp3 
```

## Denoise

TRY OUT THE DENOISE MODELS!!

```sh
git clone https://github.com/GregorR/rnnoise-models.git


```




## Resources

* https://samplefocus.com/samples/music-record-noise
* https://www.amirsharif.com/using-ffmpeg-to-reduce-background-noise
* https://onelinerhub.com/ffmpeg/how-to-reduce-background-audio-noise-using-arnndn