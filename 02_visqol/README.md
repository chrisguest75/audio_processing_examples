# VISQOL

Demonstrate how to use VisQOL.  

WARNING: Dockerfile is currently pointing to a fork.  

NOTE:

* Bazel build is a massive memory hog - check docker stats whilst building if you have issues.
* master has a bug where the WORKSPACE file needs to be patched https://github.com/google/visqol/issues/117

## Build

```sh
# build
just docker-build

just docker-shell

# rebuild if required
bazel-5.3.2 build :visqol -c opt
```

## Test

No noise

```sh
just mix-noise brown 0
just copy-inputs  

# inside container
./bazel-bin/visqol --reference_file /in/english_coventrycarol_unknown_rg_64kb.wav --degraded_file /in/english_coventrycarol_unknown_rg_64kb_brownnoise.wav --verbose --use_speech_mode --output_debug /out/debug.txt
```

Low noise

```sh
# low noise
just mix-noise brown 0.05
just copy-inputs  

# inside container
./bazel-bin/visqol --reference_file /in/english_coventrycarol_unknown_rg_64kb.wav --degraded_file /in/english_coventrycarol_unknown_rg_64kb_brownnoise.wav --verbose --use_speech_mode --output_debug /out/debug.txt
```

High noise

```sh
# high noise
just mix-noise brown 0.5
just copy-inputs  

# inside container
./bazel-bin/visqol --reference_file /in/english_coventrycarol_unknown_rg_64kb.wav --degraded_file /in/english_coventrycarol_unknown_rg_64kb_brownnoise.wav --verbose --use_speech_mode --output_debug /out/debug.txt
```

## Resources

* Perceptual Quality Estimator for speech and audio [here](https://github.com/google/visqol)
* Installing Bazel on Ubuntu [here](https://bazel.build/install/ubuntu)
* A user-friendly launcher for Bazel [here](https://github.com/bazelbuild/bazelisk)
* Put a built version in release [here](https://github.com/google/visqol/issues/117)
