alphabet = b'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz0123456789+/'
print(alphabet)
src = 'abcd'
def base64encode(src:str):
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return
    length = len(_src)
    for offset in range(0, length, 3):
        triple = _src[offset:offset+3]
