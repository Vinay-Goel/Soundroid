"""
Implement Note Depression logic here
"""
from src.tune import NoteBuilder
from src.constants import FadeConstants


def fade_tune(tune, start_time=0, end_time=-1, fade_type=FadeConstants.LINEAR_FADE_OUT):
    print(
        "Fading Audio (channels: [{}], sample width: [{}], frame rate: [{}]) of duration: [{}] sec, from: [{}] sec, to: [{}] sec with Fade type: [{}].".format(
            tune.channels, tune.sample_width, tune.frame_rate, tune.duration_seconds, start_time, end_time, fade_type))

    sample_array = tune.get_array_of_samples()
    if end_time == -1:
        end_time = tune.duration_seconds
    start_index = max(0, int(start_time / tune.duration_seconds * len(tune.get_array_of_samples())))
    end_index = min(len(tune.get_array_of_samples()),
                    int(end_time / tune.duration_seconds * len(tune.get_array_of_samples())))
    print(
        "Fading sample array of size: [{}], from: [{}], to: [{}].".format(len(tune.get_array_of_samples()), start_index,
                                                                          end_index))

    for i in range(start_index, end_index, tune.channels):
        for j in range(0, tune.channels):
            if fade_type == FadeConstants.LINEAR_FADE_OUT:
                sample_array[i+j] = linear_fade_out_sample(sample_array[i+j], i, start_index, end_index)
            elif fade_type == FadeConstants.LINEAR_FADE_IN:
                sample_array[i+j] = linear_fade_in_sample(sample_array[i+j], i, start_index, end_index)

    return NoteBuilder.build_note_from_sample_array(sample_array, tune.channels, tune.sample_width, tune.frame_rate)


def linear_fade_in_sample(sample, index, start_index, end_index):
    return int((1.0*index - start_index) / (end_index - start_index) * sample)


def linear_fade_out_sample(sample, index, start_index, end_index):
    return int((1.0*end_index - index) / (end_index - start_index) * sample)
