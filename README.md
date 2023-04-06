# Hide message in image
## Dependencies
```bash
pip install Pillow
Python 3
```

## Description

The program can hide a message in an image by altering the RGB values of pixels in a specific way, or read a hidden message from an image. The message is converted to binary and split into 8-bit chunks, and then each bit is embedded in the least significant bit of the RGB values of the pixels. 

## Usage
To use the program, run the code and choose whether to hide or read a message. If hiding a message, enter the name of the original image and the message to be hidden. The program will output a new image with the message embedded in it. If reading a message, enter the name of the image containing the hidden message. The program will output the hidden message.

## Example
```console

Enter original image name: original.png

Type H for Hide/R for Read: R

Enter second image name and format: output.png

Reading...

Binary Message is: 00110001 00110010 00110011 00110100

1234
```
