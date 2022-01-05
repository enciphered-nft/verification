# Generated Hash Signatures

Cryptographic hash function (`SHA-256`) that applied to the `MESSAGE` by signing with `SECRET_KEY` which is the collected data from public internet resources (wikipedia) that mixed together to produce unique hashed signature.

The generated **hash signature** can be verified only using `SECRET_KEY`.

## Secret Keys

- `metadata.txt` - contains `base64` encoded bytes which is the collected data about item. [Online tools](https://www.base64decode.org/) can be used for decoding to see the original.
- `signature.txt` - contains bytes of related image (e.g. Personal Signature Image, Profile pic).
- `secret_key.txt` - merged version of two `txt` files above to mix bytes and used as actual secret key for verification.

## Steps to verify

- Download **Python 3**
- Navigate to the project folder (from terminal/cmd)
- Run following command and follow instruction for verification

```
python3 verify.py
```
