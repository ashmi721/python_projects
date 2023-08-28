'''the "gtts" and "pydub.playback" library allows to easily convert text to speech
and play the generated autio within python script, making it a useful approach for 
tasks that involve working with spoken content.'''

from gtts import gTTS
from pydub.playback import play

# Prompt the user for text
text = input("Enter your text: ")

# Convert text to speech
tts = gTTS(text)

# Save the generated audio to a file
tts.save("output.mp3")

# Play the generated audio file
play(tts)
