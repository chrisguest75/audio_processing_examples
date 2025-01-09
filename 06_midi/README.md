# MIDI

Midi playback using a soundfont.  

NOTE:

* You can look at midi files in imhex
* fluidsynth allows you to set the gain

TODO:

* Is it possible to remap the instrument?
* Get jack working

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

## ALSA

```sh
# if running qsynth you should see fluidsynth listed.
cat /proc/asound/seq/clients

# also 
aconnect --list

# show that midi-thru is connected
just nix
just patchage

# using alsa-utils playing to a port - playing on midithru
aplaymidi --port 14:0 ./files/Chords\ Bbm-Bbm-Fm-Ab\ 100bpm.mid

# then spy on it
aseqdump -p 14:0
```

## Rsources

* A SoundFont Synthesizer [here](https://www.fluidsynth.org/)
* Qsynth is a fluidsynth GUI front-end [here](https://sourceforge.net/projects/qsynth/)
* FluidSynth/fluidsynth [repo](https://github.com/FluidSynth/fluidsynth)
* https://github.com/FluidSynth/fluidsynth/wiki/SoundFont
* https://www.polyphone.io/en/soundfonts/organs/733-pipe-organ-samples
* https://github.com/FluidSynth/fluidsynth/wiki/FluidFeatures
* https://discourse.nixos.org/t/how-to-configure-fluidsynth-to-use-soundfont-fluid/42830
* https://wiki.archlinux.org/title/FluidSynth
* Standard MIDI-File Format Spec. 1.1, updated [here](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html)
* https://freeshell.de/~murks/posts/ALSA_and_JACK_MIDI_explained_(by_a_dummy_for_dummies)/
* https://jackaudio.org/
* https://github.com/gbevin/ShowMIDI
* https://github.com/alsa-project/alsa-utils