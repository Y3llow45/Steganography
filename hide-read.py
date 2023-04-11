from PIL import Image
import os.path
import math
import argparse
import sys


def main(mode, original, second, message, output):
    print(f"Running {mode} mode.")
    print(original, second, message, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Steganography')
    parser.add_argument('-m', '--mode', type=str,
                        help='(R)Read and (H)Hide', required=True)
    parser.add_argument('-oimg', '--original', type=str,
                        help='name and format of the original image', required=True)
    parser.add_argument('-simg', '--second', type=str,
                        help='name and format of the second image')
    parser.add_argument('-msg', '--message', type=str, help='message to hide')
    parser.add_argument('-out', '--output', type=str,
                        help='name and format of the output image')

    args = parser.parse_args()

    if args.mode != "H" and args.mode != "R":
        print("Mode doesn't exist. Use -m R or -m H")
    elif args.mode == "H" and (args.original is None or args.message is None or args.output is None):
        print(
            "Specify (-oimg) original image, (-msg) message to hide and (-out) output image")
    elif args.mode == "R" and (args.original is None or args.second is None):
        print("Specify (-oimg) original image and (-simg) second image")
    else:
        main(args.mode, args.original, args.second, args.message, args.output)


fileName = input("Enter original image name: ")
image = Image.open(fileName)
type = input("Type H for Hide/R for Read: ")
if type == "H":
    message = input("Enter message to hide: ")
    res = ''.join(format(ord(i), '08b') for i in message)
    counter = 0
    for c in res:
        counter += 1
    if image.size[0]*image.size[1] > counter:
        print("Message can fit in the image!")
        outputName = input("Enter output name and format: ")
        if os.path.isfile(outputName):
            print("File allready exist!!!")
        else:
            print("Hidding...")
            pixelMap = image.load()
            row = 0
            column = 0
            for i in range(counter):
                if i == 0 and res[i] == "1":
                    pixel = pixelMap[row, column]
                    if(pixel[0] == 0):
                        pixelMap[row, column] = (
                            pixel[0]+1, pixel[1], pixel[2])
                    elif(pixel[0] == 250):
                        pixelMap[row, column] = (
                            pixel[0]-1, pixel[1], pixel[2])
                else:
                    if(i != 0):
                        if row == image.size[0]-1:
                            row = 0
                            column = column+1
                        else:
                            row = row+1
                        if res[i] == "1":
                            pixel = pixelMap[row, column]
                            if(pixel[0] == 0):
                                pixelMap[row, column] = (
                                    pixel[0]+1, pixel[1], pixel[2])
                            elif(pixel[0] == 250):
                                pixelMap[row, column] = (
                                    pixel[0]-1, pixel[1], pixel[2])
            image.show()
            image = image.save(outputName)
    else:
        print("Message is too big!")
else:
    messageImage = input("Enter second image name and format: ")
    if os.path.isfile(messageImage):
        print("Reading...")
        secondImage = Image.open(messageImage)
        secondMap = secondImage.load()
        firstMap = image.load()
        row = 0
        column = 0
        binaryMessage = ""
        counterEnd = 0
        if image.size[0] == secondImage.size[0] and image.size[1] == secondImage.size[1]:
            for i in range(image.size[0]*image.size[1]):
                pixel = firstMap[row, column]
                pixel2 = secondMap[row, column]
                if(pixel[0] == pixel2[0] and pixel[1] == pixel2[1] and pixel[2] == pixel2[2]):
                    binaryMessage += "0"
                    counterEnd = counterEnd+1
                else:
                    binaryMessage += "1"
                    counterEnd = 0
                if counterEnd == 8:
                    break
                else:
                    if row == image.size[0]-1:
                        row = 0
                        column = column+1
                    else:
                        row = row+1
        print("Binary Message is: "+binaryMessage)
        n = int(binaryMessage, 2)
        num = len(binaryMessage)/8
        if num.is_integer():
            binaryMessage = binaryMessage.rstrip(binaryMessage[-8])
            loopNum = num-8
        else:
            loopNum = math.floor(num)
        MessageWithSpace = ""
        count = 0
        loopNum = int(loopNum)
        for o in range(loopNum*8):
            MessageWithSpace = MessageWithSpace+binaryMessage[o]
            count = count+1
            if count == 8:
                MessageWithSpace = MessageWithSpace+" "
                count = 0
        binary_values = MessageWithSpace.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
        # print(binaryMessage)
        try:
            print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
        except:
            print(ascii_string)
