import math

from src.constants import FadeConstants
from src.constants.AudioConfigurations import DoubleChannelDoubleSample44100 as DD44100

from src.tune import TuneBuilder, NoteBuilder, TuneFader

from src.utils import AudioExporter


if __name__ == "__main__":

    sample_array = NoteBuilder.build_natural_sample_array(23279, 2*math.pi/8.75, math.pi/2)
    frequency = NoteBuilder.build_note_from_sample_array(sample_array, DD44100.channels, DD44100.sample_width,
                                                         DD44100.frame_rate)
    note = TuneBuilder.build_tune(frequency, 1)
    beat_fade_in = TuneFader.fade_tune(note, 0, 0.001, FadeConstants.LINEAR_FADE_IN)
    beat = TuneFader.fade_tune(beat_fade_in, start_time=0.002)

    tune = TuneBuilder.build_tune(beat, 10)
    AudioExporter.export_audio("audio1", tune)
