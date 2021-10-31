# murmurhash-cli-python

sample output

```
./murmurhash-cli.py license.txt /bin/sh does-not-exist.txt /etc/shadow 

license.txt
  mmh3 128 de1bcec6a19424dbb198e9dc74de6444
  mmh3  64 de1bcec6a19424db
  mmh3  32 de1bcec6
  mmh2  32 e42e704b
  mmh2  16 e42e
/bin/sh
  mmh3 128 81b1ea96f1af443a135fc3864bb2f62e
  mmh3  64 81b1ea96f1af443a
  mmh3  32 81b1ea96
  mmh2  32 ba7873f4
  mmh2  16 ba78
does-not-exist.txt
  error: no such file
/etc/shadow
  error: permission denied
```
