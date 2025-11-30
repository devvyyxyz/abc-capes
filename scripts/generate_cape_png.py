#!/usr/bin/env python3
"""
Generate a transparent 64x32 PNG at
`assets/minecraft/textures/entity/cape.png`.

This uses only the Python standard library (no external deps).
"""
import os
import zlib
import struct
import binascii

WIDTH = 64
HEIGHT = 32
OUT_PATH = os.path.join("assets", "minecraft", "textures", "entity", "cape.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _chunk(tag: bytes, data: bytes) -> bytes:
    length = struct.pack("!I", len(data))
    crc = struct.pack("!I", binascii.crc32(tag + data) & 0xFFFFFFFF)
    return length + tag + data + crc


def make_transparent_png(path: str, width: int = WIDTH, height: int = HEIGHT) -> None:
    ihdr = struct.pack("!IIBBBBB", width, height, 8, 6, 0, 0, 0)

    # Each scanline: 1 filter byte (0) followed by width * 4 bytes (RGBA)
    row = b"\x00" + (b"\x00\x00\x00\x00" * width)
    raw = row * height
    compressed = zlib.compress(raw)

    png = PNG_SIGNATURE + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", compressed) + _chunk(b"IEND", b"")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(png)


if __name__ == "__main__":
    make_transparent_png(OUT_PATH)
    print(f"Wrote transparent PNG: {OUT_PATH}")
