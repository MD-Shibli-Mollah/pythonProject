
import base64

if __name__ == '__main__':
    my_str = "aHR0cHM6Ly9mb3Jtcy5nbGUvWU5ZXQ0d2NRWHVLNnNwdjU="
    # add the padding "="  //base64.b64decode(code+"=") ***s = s.replace('.', '=')
    my_str += "=" * ((4 - len(my_str) % 4) % 4)
    # use ceil
    enc_st = my_str.encode("ascii")
    print("enc", enc_st)
    print(my_str)
    my_enc64 = base64.b16encode(enc_st)

    print("encode", my_enc64)
    base64_bytes = my_str.encode("ascii")

    print(base64_bytes)
    mystr_bytes = base64.b64decode(base64_bytes)

    print(mystr_bytes)
    # Base64 decode
    # print(f"Encoded string: {base64_string}")
