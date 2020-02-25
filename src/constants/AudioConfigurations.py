"""
    Define Audio Configurations here
    Syntax: Channel Count + Sample Count + Frame Rate
"""


class SingleChannelSingleSample24000:
    channels = 1
    sample_width = 1
    frame_rate = 24000


class DoubleChannelDoubleSample44100:
    channels = 2
    sample_width = 2
    frame_rate = 44100
