# PEAQ

Build and use PEAQ tool.  

TODO:

* The code segfaults
* Create a patch for the code.

## Modify

NOTE: For the files that fail to link add `#include <errno.h>` to the .c files

## Build

```sh
just docker-build
just docker-shell

# inside container shell
make
make install
/usr/local/bin/peaqb 
```

## Noise

```sh
just mix-noise pink 0.1
just mix-noise brown 0.05
```

## Quick Test

```sh
# copy
just copy-inputs    

# compare (in container) SEGFAuLTS
/usr/local/bin/peaqb -r /in/english_coventrycarol_unknown_rg_64kb.wav -t /in/english_coventrycarol_unknown_rg_64kb_brownnoise.wav  
```

## Resources

* Perceptual Evaluation of Audio Quality [here](https://sourceforge.net/projects/peaqb/)
* https://github.com/gonshell/peaq
