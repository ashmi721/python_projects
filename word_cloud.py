# Import the necessary libraries
from wordcloud import WordCloud  # Library to create word clouds
import matplotlib.pyplot as plt  # Library for plotting


# Prompt for the user input
text = input("Ente your text :")

# Create a WordCloud object with  properties of the word cloud.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))

# Display the word cloud image using the 'imshow' function
# Use 'interpolation' to enhance the quality of the image display
plt.imshow(wordcloud, interpolation='bilinear')

plt.axis('off')  #  Turn off the axes for a clean image display
plt.show() # Show the generated word cloud
