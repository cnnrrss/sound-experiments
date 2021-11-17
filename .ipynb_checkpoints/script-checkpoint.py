import librosa

# %matplotlib inline
import matplotlib.pyplot as plt
import librosa.display


# filename = librosa.example('example.mp3')

y, sr = librosa.load('./example.mp3', sr=44100)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(y, sr=sr)

# BPMs
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
