# Hide message in image
## Dependencies
```bash
pip install Pillow
Python 3
```

## Description

The program can hide a message in an image by altering the RGB values of pixels in a specific way, or read a hidden message from an image. The message is converted to binary and split into 8-bit chunks, and then each bit is embedded in the least significant bit of the RGB values of the pixels. 

## Example
```console

python hideRead.py -m R -oimg original.png -simg secrete.png -bm y
Reading...
Binary Message is: 00110001 00110010 00110011 00110100
1234
```
