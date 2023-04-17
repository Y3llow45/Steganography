from PIL import Image
import os.path
import math
import argparse
import sys


def solve(mode, fileName, messageImage, message, outputName, bm):
    #fileName = input("Enter original image name: ")
    if os.path.isfile(fileName):
        try:
            image = Image.open(fileName)
        except Exception as e:
            print("Failed to open the file")
            sys.exit(1)
    else:
        print('No such file or directory')
        sys.exit(1)
    #mode = input("Type H for Hide/R for Read: ")
    if mode == "H":
        #message = input("Enter message to hide: ")
        res = ''.join(format(ord(i), '08b') for i in message)
        counter = 0
        for c in res:
            counter += 1
        if image.size[0]*image.size[1] > counter:
            #print("Message can fit in the image!")
            #outputName = input("Enter output name and format: ")
            if os.path.isfile(outputName):
                print('File already exist')
                sys.exit(1)
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
                # image.show()
                image = image.save(outputName, quality=100)
        else:
            #print('Message is too long \n Use bigger image or shorten the message')
            raise ValueError("Message is too long! Use bigger image!")
    else:
        #messageImage = input("Enter second image name and format: ")
        if os.path.isfile(messageImage):
            # print("Reading...")
            try:
                secondImage = Image.open(messageImage)
            except:
                print("Failed to open the file")
                sys.exit(1)
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
                    if counterEnd == 9:
                        break
                    else:
                        if row == image.size[0]-1:
                            row = 0
                            column = column+1
                        else:
                            row = row+1
            if bm == 'y' or bm == 'Yes' or bm == 'yes' or bm == 'Y':
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
                output = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
                print(output)
                return output
            except:
                print(ascii_string)
                return(ascii_string)
        else:
            print('No such file or directory')


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
    parser.add_argument('-bm', '--binarymsg', type=str,
                        help='show binary message after reading. y or n')

    args = parser.parse_args()

    if args.mode != "H" and args.mode != "R":
        print("Mode doesn't exist. Use -m R or -m H")
    elif args.mode == "H" and (args.original is None or args.message is None or args.output is None):
        print(
            "Specify (-oimg) original image, (-msg) message to hide and (-out) output image")
    elif args.mode == "R" and (args.original is None or args.second is None):
        print("Specify (-oimg) original image and (-simg) second image")
    else:
        solve(args.mode, args.original, args.second,
              args.message, args.output, args.binarymsg)

__all__ = ['solve']
