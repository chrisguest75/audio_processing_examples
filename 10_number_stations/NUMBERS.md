# NUMBERS

## Download

Download some numbers from internet archive  

```sh
just -f numbers.justfile getsource 
```

## Process

```sh
cd 10_station_handler

just test-measure
just test-normalise  
just test-concatenate

just -f ../shortwave.justfile shortwave ../output/numbers.wav

just -f ../shortwave.justfile noise '../output/numbers_shortwave.wav'

vlc '../../output/numbers_shortwave_noise.wav'
```

## Resources

* https://archive.org/details/numbers0-100englishpronouciation