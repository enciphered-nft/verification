import os
import hashlib
import hmac


def get_signature(dir_name: str, msg: str) -> str:
    with open(f"assets/{dir_name}/secret_key.txt", "rb") as secret_key_txt_file:
        signature = hmac.new(secret_key_txt_file.read(), msg, hashlib.sha256)
        return signature


def verify_hash_signature() -> str:
    """
    Welcome to verification!

    Verification process needs 3 main inputs for comparing digest bewteen outputs:

    1. Location of Secret Key - The name of folder that holds secret key you want to sign with
    2. Message - The value which hashed by using secret_key (e.g. Apple)
    3. Hashed Value - The hashed value that provided in NFT
    """
    dir_name = input("Enter directory name from assets to fetch secret_key: ").lower()
    if os.path.exists(f"assets/{dir_name}/secret_key.txt"):
        msg = input("Enter message that needs to be verified: ").encode()
        digest = input("Enter hashed value: ")
        signature = get_signature(dir_name, msg)
        is_verified = hmac.compare_digest(signature.hexdigest(), digest)
        if is_verified:
            print("VERIFIED!")
        else:
            print("NOT VERIFIED!")
    else:
        print("No such folder in assets. Please try again")

print(verify_hash_signature.__doc__)
verify_hash_signature()