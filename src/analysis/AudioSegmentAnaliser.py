import math

from src.tune import NoteBuilder

from src.constants.AudioConfigurations import DoubleChannelDoubleSample44100 as DD44100


def analise_produced_frequencies():

    for i in range(3, 2200):
        print(produce_data_for_array_length(i))


def produce_data_for_array_length(array_length):
    sample_array = NoteBuilder.build_natural_sample_array(23279, 2 * math.pi / array_length, math.pi/2)
    frequency = NoteBuilder.build_note_from_sample_array(sample_array, DD44100.channels, DD44100.sample_width,
                                                         DD44100.frame_rate)
    return 1/frequency.duration_seconds


if __name__ == "__main__":
    analise_produced_frequencies()
