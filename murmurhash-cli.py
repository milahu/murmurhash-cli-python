#!/usr/bin/env python3

import sys
import mmh3
import murmurhash

def hexstr(bytes):
  return "".join('{:02x}'.format(x) for x in bytes)

def murmurhash3(str, num_bytes=16):
  hash_bytes = mmh3.hash_bytes(str)
  return hexstr(hash_bytes[0:num_bytes])

def murmurhash3_128(str):
  return murmurhash3(str, 16)

def murmurhash3_64(str):
  return murmurhash3(str, 8)

def murmurhash3_32(str):
  return murmurhash3(str, 4)

def murmurhash2(str, num_bytes=4, encoding='utf8'):
  hash_bytes = murmurhash.hash_bytes(str.encode(encoding)).to_bytes(4, byteorder='big', signed=True)
  return hexstr(hash_bytes[0:num_bytes])

def murmurhash2_32(str):
  return murmurhash2(str, 4)

def murmurhash2_16(str):
  return murmurhash2(str, 2)

if len(sys.argv) == 1:
  print(f"usage: {sys.argv[0]} inputfile...", file=sys.stderr)
  sys.exit(1)

for path in sys.argv[1:]:
  print(path)

  try:
    text = open(path, 'r').read()

    print(f"  mmh3 128 {murmurhash3_128(text)}")
    print(f"  mmh3  64 {murmurhash3_64(text)}")
    print(f"  mmh3  32 {murmurhash3_32(text)}")
    print(f"  mmh2  32 {murmurhash2_32(text)}")

  except UnicodeDecodeError as e:
    print(f"  error: binary file. not (yet?) supported")

  except FileNotFoundError as e:
    print(f"  error: no such file")

  except PermissionError as e:
    print(f"  error: permission denied")

  except Exception as e:
    print(f"  error: {type(e).__name__}: {e}")
