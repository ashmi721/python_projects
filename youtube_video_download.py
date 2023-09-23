import pytube

video_url = input('Enter url: ')

video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.get_highest_resolution()

stream.download()