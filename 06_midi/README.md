# MIDI

Midi playback using a soundfont.  

NOTE:

* You can look at midi files in imhex
* fluidsynth allows you to set the gain

TODO:

* Is it possible to remap the instrument?

## Install (Nix)

```sh
# find the sound font and change in just file
find /nix/store -iname "*.sf2"

just nix
```

## Play (FluidSynth)

```sh
# play default
just play

# pass a file
just play ./files/Chords\ Bbm-Bbm-Fm-Ab\ 100bpm.mid
```

## Rsources

* A SoundFont Synthesizer [here](https://www.fluidsynth.org/)
* https://sourceforge.net/projects/qsynth/
* https://github.com/FluidSynth/fluidsynth
* https://github.com/FluidSynth/fluidsynth/wiki/SoundFont
* https://www.polyphone.io/en/soundfonts/organs/733-pipe-organ-samples
* http://www.hammersound.net/
* https://github.com/FluidSynth/fluidsynth/wiki/FluidFeatures
* https://discourse.nixos.org/t/how-to-configure-fluidsynth-to-use-soundfont-fluid/42830
* https://wiki.archlinux.org/title/FluidSynth
* http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html
