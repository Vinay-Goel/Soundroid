from pydub import AudioSegment
from src.constants.AudioConfigurations import DoubleChannelDoubleSample44100 as DD44100


def build_note(raw_data, channels=DD44100.channels, sample_width=DD44100.sample_width, frame_rate=DD44100.frame_rate):
    print("Creating Audio Segment with, Raw Data length: [{}], Channels: [{}], Sample Width: [{}], Frame Rate: [{}]."
          .format(len(raw_data), channels, sample_width, frame_rate))
    note = AudioSegment(raw_data, sample_width=sample_width, frame_rate=frame_rate, channels=channels)
    print(
        "Created Audio Segment of Sample Array length: [{}], Raw Data length: [{}], Channels: [{}], Sample Width: [{}], Frame Rate: [{}].".format(
            len(note.get_array_of_samples()), len(note.raw_data), note.channels, note.sample_width, note.frame_rate))
    return note
