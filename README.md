# wallapy

## Overview
Basic CLI tool to bulk process images splitting them into separate files for dual monitor desktop setups. Written in python using [pillow](https://pillow.readthedocs.io/en/stable/) and [click](https://click.palletsprojects.com/en/8.1.x/).

## Motivation

KDE Plasma doesn't support wallpaper spanning (???) and no one has the time to process hundreds of images manually :smile:

## Features

### Bisect all images in a folder

**Before**
![Full-Size-Image-Example](docs/w77.png)

**After**
|Left|Right|
|-|-|
![Split-Left-Image-Example](docs/w77_L.png)|![Split-Right-Image-Example](docs/w77_R.png)

----

### CLI flags for better control

```zsh
Options:
  -v, --verbose / -q, --quiet  -v, --verbose: Prints additional information
                               during script execution
                               
                               -q, --queit: Displays progress bar only
                               
                               default = -q, --quiet
  -d, --delete / -k, --keep    -d, --delete: Deletes source files after
                               processing complete
                               
                               -k, --keep: Keeps source files
                               
                               default = -k, --keep
  -o, --output_dir TEXT        -o, --output_dir: Specifies output directory
                               for processed images. If the directory does not
                               exist the script will try to create it.
                               
                               default: None, same as input directory
  --help                       Show this message and exit.
```

----
## Roadmap

- [ ] Better documentation, getting-started and usage examples
- [ ] Unit and Integration Tests
- [ ] Performance (concurreny)
  - [ ] Possibly migrate to Go
- [ ] Web app
- [ ] UI for more advanced transformations
  - [ ] Canvas to drag and drop monitors over the image and crop out accordingly



