# Kick API for Python
The `KickApi` Python package is your gateway to seamless integration with the Kick API, providing a robust and user-friendly interface for retrieving comprehensive channel and video data. Empowering developers to harness the full potential of Kick's capabilities, this package simplifies data retrieval, enabling a wide range of applications from content analysis to user interaction.

## Installation
Getting started is a breeze. Install the KickApi package with a single command
```bash
pip install KickApi
```

## Usage
Integrate the KickApi into your Python project with ease:
### Fetch Channel Data
The KickAPI package allows you to fetch detailed information about a Kick channel effortlessly. The example code below demonstrates how to use KickAPI to retrieve and display channel data.
```python
from kickapi import KickAPI

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch channel data by username
channel = kick_api.channel("username")

# Access channel attributes
print("Channel ID:", channel.id)
print("Username:", channel.username)
print("Bio:", channel.bio)
print("Avatar URL:", channel.avatar)
print("Followers:", channel.followers)
print("Playback URL:", channel.playback)
```

### Fetch Video Data
To obtain insights into Kick videos, including details such as title, thumbnail URL, duration, and more, you can use KickAPI to fetch video data. The example code below demonstrates how to retrieve and display video details.
```python
from kickapi import KickAPI

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch video data by video ID
video = kick_api.video("video_id")

# Access video attributes
print("Video ID:", video.id)
print("Title:", video.title)
print("Thumbnail URL:", video.thumbnail)
print("Duration:", video.duration)
print("Live Stream ID:", video.live_stream_id)
print("Created At:", video.created_at)
print("Updated At:", video.updated_at)
print("UUID:", video.uuid)
print("Views:", video.views)
print("Language:", video.language)
print("Stream Video URL:", video.strem_video)

# Access channel data associated with the video
print("Channel ID:", video.channel.id)
print("Channel Username:", video.channel.username)
```

### Fetch Chat Data
The KickAPI package allows you to fetch chat data for a specific video, providing insights into the conversation history. The example code below demonstrates how to use KickAPI to retrieve and display chat messages.
```python
from kickapi import KickAPI

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch video data
channel = kick_api.channel('username')

# Fetch chat data for the video's channel and a specific date
chat = kick_api.chat(channel.id, '<DATE_TIME>') # Example 2024-01-1T01:00:00.000Z

# Iterate over messages and print sender's username and text
for message in chat.messages:
    print("{}: {}".format(message.sender.username, message.text))
```

### Fetch Live Chat Data
To fetch live chat data and receive real-time updates on the ongoing conversation, you can continuously retrieve messages at intervals. The example code below demonstrates how to use KickAPI to fetch and display live chat messages.
```python
from kickapi import KickAPI
from datetime import datetime, timedelta
import time

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch video data
video = kick_api.video('b8cdb750-a957-4636-b0f8-9c8c41dd2f7c')

while True:
    # Convert to datetime object and format in the desired way
    original_date_obj = datetime.strptime(video.start_time, '%Y-%m-%d %H:%M:%S')
    formatted_date_str = original_date_obj.strftime('%Y-%m-%dT%H:%M:%S.000Z')

    # Fetch chat data for the video's channel and the specific date
    chat = kick_api.chat(video.channel.id, formatted_date_str)

    # Iterate over messages and print sender's username and text
    for message in chat.messages:
        print("{}: {}".format(message.sender.username, message.text))

    # Update start_time for the next iteration and pause for 5 seconds
    video.start_time = (original_date_obj + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(5)
```

### Fetch and Save Avatar Image
You can use the KickAPI to fetch a channel's avatar image and save it locally. Below is an example code snippet demonstrating how to achieve this:
```python
from kickapi import KickAPI
import requests

# Create an instance of KickAPI
kick_api = KickAPI()

# Fetch channel data by username
channel = kick_api.channel("username")

# Send a request to get the avatar URL from the channel data
response = requests.get(channel.avatar)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open a file handler to create a new file named 'avatar.webp'
    with open('avatar.webp', "wb") as file:
        # Write the content of the response to the file
        file.write(response.content)
        print("Avatar image saved successfully.")
else:
    print(f"Failed to fetch avatar. Status Code: {response.status_code}")
```

## Features
- **Channel Insights** Obtain a detailed snapshot of Kick channels effortlessly. Retrieve essential information such as channel ID, bio, avatar URL, followers count, and playback URL.</br>
- **Video Analytics** Dive deep into Kick videos with a wealth of data at your fingertips. Retrieve details including video title, thumbnail URL, duration, live stream ID, creation and update timestamps, UUID, views count, language, stream video URL, and associated channel details.</br>
- **Chat Integration** Stay connected with Kick chat functionality. Retrieve and interact with chat messages, including sender details, message content, and timestamps.

## Contributing
We welcome contributions from the community! If you'd like to contribute to the development of KickApi, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure the code passes all tests.
- Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Make sure to include a `LICENSE` file in your project's root directory and specify the licensing details in that file. The provided link in the "License" section should point to the actual `LICENSE` file in your project.