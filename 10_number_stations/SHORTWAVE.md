# SHORTWAVE

## Contents

- [SHORTWAVE](#shortwave)
  - [Contents](#contents)
  - [Shortwave](#shortwave-1)
    - [Source](#source)
    - [Lower Audio Rate](#lower-audio-rate)
    - [Lowpass \& Highpass filters](#lowpass--highpass-filters)
    - [Shortwave Final](#shortwave-final)
  - [Resources](#resources)

## Shortwave

Standard SSB (Medium), 2.4 kHz, 300 Hz ~ 2.7 kHz, 2K40J3E from [here](https://www.nu9n.com/essb.html)  

### Source

```sh
export SOURCE_AUDIO_FILE=../sources/audiobooks/christmas_short_works_2008_0812_64kb_mp3/english_three_christmas_masses_daudet_ajm_64kb.mp3
just play ${SOURCE_AUDIO_FILE}
```

### Lower Audio Rate

```sh
just samplerate-2400 ${SOURCE_AUDIO_FILE}
```

### Lowpass & Highpass filters

```sh
# Check spectrum 
just lowpass ${SOURCE_AUDIO_FILE}
just sonic-visualiser '../output/english_three_christmas_masses_daudet_ajm_64kb_lowpass.wav'

just highpass ${SOURCE_AUDIO_FILE}
just sonic-visualiser '../output/english_three_christmas_masses_daudet_ajm_64kb_highpass.wav'
```

### Shortwave Final

With final filters and condensed sample rate.  

```sh
just shortwave ${SOURCE_AUDIO_FILE}

just sonic-visualiser '../output/english_three_christmas_masses_daudet_ajm_64kb_shortwave.wav'
```

## Resources

* https://www.nu9n.com/essb.html

