# Importing the necessary libraries
import sounddevice           # Library for audio recording and playback
from scipy.io.wavfile import write  # Library for working with WAV files

# Setting the sampling rate for audio recording
fs = 47100  # Sampling rate: 44,100 samples per second

# Prompting the user to input the recording time in seconds
second = int(input("Enter the Recording Time in second: "))

# Indicating that recording is starting
print("Recording.....\n")

# Recording audio using the sounddevice library
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)  # Recording stereo audio (2 channels)
sounddevice.wait()  # Waiting for the recording to complete

# Writing the recorded audio to a WAV file
write("MyRecording.wav", fs, record_voice)  # Writing to "MyRecording.wav" with specified sampling rate and audio data

# Displaying a message indicating the recording is done
print("Recording is done. Please check your folder to listen to the recording")
