import hashlib

filename = "Ashley-Madison.txt"

password = "Tsoguwa"

encode_password = password.encode("utf-8")
passwordHash = hashlib.md5(encode_password.strip()).hexdigest()

pass_file = open(filename, "r")

for word in pass_file:
    encode_word = word.encode("utf-8")
    enc_hash = hashlib.md5(encode_word.strip()).hexdigest()

    if passwordHash == enc_hash:
        print("This agency has been hacked. The password was "+ word)
        quit()

print("This agency has a strong password.")
