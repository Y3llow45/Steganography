"""Hide and recover UTF-8 text by comparing two PNG images.

A four-byte big-endian payload length precedes the message. Each bit uses one
pixel: 0 leaves it unchanged and 1 changes the red channel by exactly one.
The original image is required to decode the modified image.
"""
import argparse
from pathlib import Path

from PIL import Image

HEADER_BYTES = 4


def _bits(data):
    for byte in data:
        for shift in range(7, -1, -1):
            yield (byte >> shift) & 1


def _images(original, modified=None):
    with Image.open(original) as source:
        base = source.convert("RGBA" if source.mode == "RGBA" else "RGB")
    if modified is None:
        return base
    with Image.open(modified) as other:
        encoded = other.convert(base.mode)
    if base.size != encoded.size:
        raise ValueError("Images must have identical dimensions")
    return base, encoded


def _output_path(filename):
    target = Path(filename)
    if target.suffix.lower() != ".png":
        raise ValueError("Output image must be a PNG (lossless)")
    # Preserve the GUI's historical default output folder.
    if target.parent == Path("."):
        target = Path("img") / target
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError("Output image already exists: " + str(target))
    return target


def solve(mode, fileName, messageImage, message, outputName, bm):
    """Keep the existing CLI/GUI interface: mode H=hide, R=read."""
    if mode == "H":
        if not message:
            raise ValueError("Message cannot be empty")
        image = _images(fileName)
        payload = message.encode("utf-8")
        if len(payload) >= 2 ** 32:
            raise ValueError("Message is too large")
        data = len(payload).to_bytes(HEADER_BYTES, "big") + payload
        if len(data) * 8 > image.width * image.height:
            raise ValueError("Message is too long! Use a bigger image.")
        output = _output_path(outputName)
        pixels = image.load()
        for offset, bit in enumerate(_bits(data)):
            if not bit:
                continue
            x, y = offset % image.width, offset // image.width
            pixel = pixels[x, y]
            red = pixel[0] + 1 if pixel[0] < 255 else pixel[0] - 1
            pixels[x, y] = (red,) + pixel[1:]
        image.save(output, format="PNG")
        return str(output)

    if mode == "R":
        if not messageImage:
            raise ValueError("Provide the encoded image")
        original, encoded = _images(fileName, messageImage)
        before, after = original.load(), encoded.load()
        capacity = original.width * original.height
        if capacity < HEADER_BYTES * 8:
            raise ValueError("Image is too small to contain a message")

        def changed(offset):
            x, y = offset % original.width, offset // original.width
            return int(before[x, y][0] != after[x, y][0])

        def read_bytes(start, length):
            result = bytearray()
            for byte_index in range(length):
                value = 0
                for bit_index in range(8):
                    value = (value << 1) | changed(start + byte_index * 8 + bit_index)
                result.append(value)
            return bytes(result)

        size = int.from_bytes(read_bytes(0, HEADER_BYTES), "big")
        if size == 0 or (HEADER_BYTES + size) * 8 > capacity:
            raise ValueError("Invalid or missing message header (image may use the old format)")
        data = read_bytes(HEADER_BYTES * 8, size)
        try:
            result = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("Message is damaged or images do not match") from exc
        if str(bm).strip().lower() in ("yes", "y"):
            print("Binary Message is:", "".join(str(x) for x in _bits(data)))
        print(result)
        return result

    raise ValueError("Mode must be H (hide) or R (read)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PNG image steganography")
    parser.add_argument("-m", "--mode", choices=["H", "R"], required=True)
    parser.add_argument("-oimg", "--original", required=True)
    parser.add_argument("-simg", "--second")
    parser.add_argument("-msg", "--message")
    parser.add_argument("-out", "--output")
    parser.add_argument("-bm", "--binarymsg", default="n")
    args = parser.parse_args()
    if args.mode == "H" and (not args.message or not args.output):
        parser.error("H requires -msg and -out")
    if args.mode == "R" and not args.second:
        parser.error("R requires -simg")
    try:
        solve(args.mode, args.original, args.second, args.message, args.output, args.binarymsg)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


__all__ = ["solve"]
