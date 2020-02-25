from pydub import AudioSegment


def mono_frequency_tune(path, start, end):
    tune = AudioSegment.from_file(path, format="wav")[start:end]
    print(tune.get_array_of_samples())
    positions = get_repeating_raw_data(tune.get_array_of_samples(), tune.channels, 1)

    # Raw data uses 2 hexadecimal values to represent a sample e.g.: 23729 = \xefZ i.e. (Z ascii 90) * 256 +
    # (ef hexadecimal to decimal 239)
    print(tune.raw_data[2*positions["start"]:2*positions["end"]])


def get_repeating_raw_data(samples, channels, wave, pos=0):
    start = local_peak_position(samples, pos, channels)
    mid = local_peak_position(samples, start, channels)
    end = local_peak_position(samples, mid, channels)
    print(samples[start:end])
    print(start)
    print(end)
    if wave == 1:
        return {"start": start, "end": end}
    else:
        return get_repeating_raw_data(samples, channels, wave-1, end-5)


def local_peak_position(samples, curr, incr):
    pos = curr
    if samples[pos+incr] < samples[pos]:
        while samples[pos+incr] < samples[pos]:
            pos += incr
    else:
        while samples[pos+incr] > samples[pos]:
            pos += incr
    return pos


if __name__ == "__main__":
    mono_frequency_tune(r'C:\Users\pc\PycharmProjects\Soundroid\audios\2nd explore\audio.wav', 8000, 9000)
