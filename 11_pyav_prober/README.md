# PYAV PROBER

Demonstrate using pyav as an ffprobe tool.  

## Contents

- [PYAV PROBER](#pyav-prober)
  - [Contents](#contents)
  - [Install](#install)
  - [Start](#start)
  - [Created](#created)
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

just start --probe --file ./myaudio.m4a
```

## Created

When installing a fresh UV project.  

```sh
# create a basic skeleton
uv init .

# add packages
uv add pyyaml

# add dev 
uv add --dev flake8-2020 
```

## Resources

* https://pyav.basswood-io.com/docs/stable/development/changelog.html

* An extremely fast Python package and project manager, written in Rust. [here](https://docs.astral.sh/uv/)
* https://github.com/astral-sh/uv
* https://www.datacamp.com/tutorial/python-uv
