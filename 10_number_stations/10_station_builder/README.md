# NUMBER STATION BUILDER

Create a number station.  

TODO:

* Add shortwave
* Add noise
* Add morse code blips

## Contents

- [NUMBER STATION BUILDER](#number-station-builder)
  - [Contents](#contents)
  - [Install](#install)
  - [Start](#start)
  - [Examples](#examples)
  - [Resources](#resources)

## Install

```sh
just nix
```

## Start

```sh
just lint

just format

just test

just start --test
```

## Examples

```sh
just test-measure 

just test-normalise
just test-measure "../../output/numbers"

just test-concatenate
```

## Resources

* An extremely fast Python package and project manager, written in Rust. [here](https://docs.astral.sh/uv/)
* https://amiaopensource.github.io/av-python-carpentry/09-aboutfiles/index.html