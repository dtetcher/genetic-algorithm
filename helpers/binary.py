def to_gray(binary: str):
    int_repr = int(binary, 2)

    int_repr ^= (int_repr >> 1)
    return bin(int_repr)[2:]