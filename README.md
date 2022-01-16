# Generated Hash Signatures

Cryptographic hash function (`SHA-256`) that applied to the `MESSAGE` by signing with `SECRET_KEY` which is the collected data from public internet resources (wikipedia) that mixed together to produce unique hashed signature.

The generated **hash signature** can be verified only using `SECRET_KEY`.

## Secret Keys

- `metadata.txt` - contains `base64` encoded bytes which is the collected data about item. [Online tools](https://www.base64decode.org/) can be used for decoding to see the original.
- `signature.txt` - contains bytes of related image (e.g. Personal Signature Image, Profile pic).
- `secret_key.txt` - merged version of two `txt` files above to mix bytes and used as actual secret key for verification.

## Steps to verify

You can check verification by using online tools like below:

https://www.devglan.com/online-tools/hmac-sha256-online

or

https://www.javainuse.com/hmac

- Enter the message such as "Elon Musk"
- Copy the secret key content of particular asset and paste the required field
- Select proper cryptographic Hash Function (take a look footer of NFT e.g. sha-256)
- Click the compute hash and the output should be same as NFT.

Also if you want to see the plain text format of encoded secret key:

- Copy the content of `signature.txt` file and decode it by using online tool below:

https://codebeautify.org/base64-to-image-converter

- Copy the content of `metadata.txt` file and decode it by using online tool below:

https://www.base64decode.org


Remember the `secret_key.txt` file is a mixed version of these two file above.

## Steps to verify (as a Developer)

- Download **Python 3**
- Navigate to the project folder (from terminal/cmd)
- Run following command and follow instruction for verification

```
python3 verify.py
```
