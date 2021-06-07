import base64
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)

    return base64.b64decode(data, altchars)
if __name__ == '__main__':
    my_str = "aHR0cHM6Ly9mb3Jtcy5nbGUvWU5ZXQ0d2NRWHVLNnNwdjU="
    enc_st = my_str.encode("ascii")
    result = decode_base64(enc_st)
    print(result)
