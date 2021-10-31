#!/usr/bin/env python3

import sys
import mmh3
import murmurhash

if len(sys.argv) == 1:
  print(f"usage: {sys.argv[0]} inputfile...", file=sys.stderr)
  sys.exit(1)

for path in sys.argv[1:]:
  print(path)

  try:
    bytes = open(path, 'rb').read()
    hash3 = mmh3.hash_bytes(bytes).hex()
    hash2 = murmurhash.hash_bytes(bytes).to_bytes(4, byteorder='big', signed=True).hex()
    print(f"  mmh3 128 {hash3}")
    print(f"  mmh3  64 {hash3[0:16]}")
    print(f"  mmh3  32 {hash3[0:8]}")
    print(f"  mmh2  32 {hash2}")
    print(f"  mmh2  16 {hash2[0:4]}")

  except FileNotFoundError as e:
    print(f"  error: no such file")

  except PermissionError as e:
    print(f"  error: permission denied")

  except Exception as e:
    print(f"  error: {type(e).__name__}: {e}")
