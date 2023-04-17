# Steganography
![Python_badge](https://img.shields.io/badge/Python-3.9.2-success)
![Pillow_badge](https://img.shields.io/badge/Pillow-9.4.0-blue)
![PySide6_badge](https://img.shields.io/badge/PySide6-6.5.0%20-yellow)
## Description

This Steganography tool can help anyone in hiding sensitive information within images using a simple user interface.  The data is concealed and read using **LSB (least significant bit) steganography**, rendering it undetectable to the naked eye. Since no keys or passwords are required, this tool speeds the process of hiding information within an image **without compromising security**.

## Features
1. Hide and extract sensitive information from images
2. Modern and intuitive GUI for an enhanced user experience
3. CLI for advanced users and automation
4. Supports popular image format .PNG

## Applications
1. **Digital watermarking**: Steganography can be used to embed a digital watermark within an image or video, allowing copyright owners to **protect their intellectual property from unauthorized use or distribution**.
2. **Information hiding**: Steganography can securely hide sensitive information within an innocent-looking file. This can be useful in **military or intelligence applications**, or for **protecting private information** such as passwords or financial data.
3. **Covert communication**: Steganography can be used to hide communication within **social media posts, images, or videos**.This can be useful for covert communication in situations where traditional methods of communication may be **monitored or censored**.
4. **Digital forensics**: Steganography can be used in digital forensics investigations to **detect hidden messages or files** that may be relevant to a case.

## Installation

```bash
$ pip install -r requirements.txt --no-index
```
## Example - command line interface (CLI)
```console
python hideRead.py -m R -oimg original.png -simg secrete.png -bm y
Binary Message is: 00110001001100100011001100110100
1234
```
## Example - graphical user interface (GUI)


## Contribute
[Contributor Covenant](https://www.contributor-covenant.org/)

## License
MIT License