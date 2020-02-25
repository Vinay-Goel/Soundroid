from src.constants import Constants


def sample_to_hexadecimal(x, sample_width):
    raw_data = sample256_to_hexadecimal(x % 256)
    if sample_width == 2:
        raw_data += sample256_to_hexadecimal(x / 256)
    return raw_data


def sample256_to_hexadecimal(x):
    if x < 0:
        x += 256
    return bytes([int(x)])
