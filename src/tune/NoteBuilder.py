"""
Implement Note Build operations here
"""
import math

from src.utils import AudioSegmentWrapper
from src.utils import SampleToRawDataConverter

from src.constants import Constants
from src.constants.AudioConfigurations import DoubleChannelDoubleSample44100 as DD44100


def build_note_from_sample_array(sample_array, channels=DD44100.channels, sample_width=DD44100.sample_width,
                                 frame_rate=DD44100.frame_rate):
    raw_data = build_raw_data_from_sample_array(sample_array, channels, sample_width)
    return AudioSegmentWrapper.build_note(raw_data, channels, sample_width, frame_rate)


def build_natural_sample_array(radius, angular_velocity, phase=0.0, channels=DD44100.channels):
    print(
        "Building Sample Array using Natural Wave generation process with Amplitude: [{}], Angular Velocity: [{}] (NOTE:: not per second), Phase: [{}].".format(
            radius, angular_velocity, phase))
    sample_array = []
    angle = phase
    while True:
        for i in range(0, channels):
            sample_array.append(int(radius * math.sin(angle)))
        angle += angular_velocity

        n = (angle-phase) / (2*math.pi)
        if n - int(n) <= Constants.ANGULAR_VELOCITY_EPS:
            break
    return sample_array


def build_raw_data_from_sample_array(sample_array, channels, sample_width):
    print("Building Raw Data from Sample Array with Channels: [{}], Sample Width: [{}].".format(channels, sample_width))
    raw_data = b''
    for x in sample_array:
        sample_raw_data = SampleToRawDataConverter.sample_to_hexadecimal(x, sample_width)
        raw_data += sample_raw_data
    return raw_data
