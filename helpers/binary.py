from math import fabs


def to_gray(binary: str, out_len: int):

    # Converting binary to integer
    #
    int_repr = int(binary, 2)

    # Applying XOR and translating to Gray code
    int_repr ^= (int_repr >> 1)

    # Translate integer back to bin representation
    #
    bin_repr = bin(int_repr)[2:]

    # If actual length is less than desired
    # then we compensate this by adding zero's
    # at the beginning
    #
    difference = int(fabs(len(bin_repr) - out_len))

    return bin_repr \
        if not difference \
        else (difference * '0') + bin_repr


def from_gray(gray_code: str):
    # Integer representation of gray code
    #
    int_repr = int(gray_code, 2)

    mask = int_repr
    while mask != 0:
        mask >>= 1
        int_repr ^= mask

    return bin(int_repr)[2:]
