import moviepy.editor as mp


def video_to_audio(from_path, to_path):
    clip = mp.VideoFileClip(from_path)
    clip.audio.write_audiofile(to_path)


if __name__ == "__main__":
    video_to_audio(r"C:\Users\pc\PycharmProjects\Soundroid\audios\2nd explore\123.mp4",
                   r"C:\Users\pc\PycharmProjects\Soundroid\audios\2nd explore\audio.mp3")
