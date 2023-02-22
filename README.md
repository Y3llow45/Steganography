# Hide message in image
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation
```bash
pip install Pillow
```
#
## Description | Steganography

You can hide message in image and read it using this program. First you type the original image name, then you choose between hide and read options. If you choose hide (H) just enter the message
you want to hide and the output image with it's format (for example "output.png"). If you choose read (R) just enter the second image name that you want to read
from (this program will find the difference between the two images and will show you the hidden message).
#
## Examples
```console

Enter original image name: original.png

Type H for Hide/R for Read: R

Enter second image name and format: output.png

Reading...

Binary Message is: 00110001 00110010 00110011 00110100

1234
```
