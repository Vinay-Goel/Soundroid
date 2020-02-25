import os
import time


def export_audio(name, audio, path=r''.join([os.getcwd(), '\\..\\audios\\', str(int(time.time())), '\\']),
                 audio_format='wav'):
    print("Exporting Audio: [{}] to Location: [{}] in format: [{}].".format(name, path, audio_format))
    if not os.path.exists(path):
        os.makedirs(path)
    audio.export(path + name + '.' + audio_format, audio_format)
