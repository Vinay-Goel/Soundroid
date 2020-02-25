"""
Implement Tune Build operations here
"""
from src.utils import AudioSegmentWrapper


def build_tune(note, seconds):
    print("Building Tune of Seconds: [{}] from Note of Seconds = [{}].".format(seconds, note.duration_seconds))
    count = int(seconds / note.duration_seconds)
    raw_data_array = [note.raw_data for i in range(count)]
    raw_data = b''.join(raw_data_array)
    return AudioSegmentWrapper.build_note(raw_data, note.channels, note.sample_width, note.frame_rate)
