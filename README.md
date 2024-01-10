# Kick API for Python
The `KickApi` Python package is your gateway to seamless integration with the Kick API, providing a robust and user-friendly interface for retrieving comprehensive channel and video data. Empowering developers to harness the full potential of Kick's capabilities, this package simplifies data retrieval, enabling a wide range of applications from content analysis to user interaction.

## Installation
Getting started is a breeze. Install the KickApi package with a single command:
```bash
pip install KickApi
```
## Usage
Integrate the KickApi into your Python project with ease:
### Fetch Channel Data
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
print("Created At:", video.createdAt)
print("Updated At:", video.updatedAt)
print("UUID:", video.uuid)
print("Views:", video.views)
print("Language:", video.language)
print("Stream Video URL:", video.strem_video)

# Access channel data associated with the video
print("Channel ID:", video.channel.id)
print("Channel Username:", video.channel.username)
```

## Features
- **Channel Insights** Obtain a detailed snapshot of Kick channels effortlessly. Retrieve essential information such as channel ID, bio, avatar URL, followers count, and playback URL.</br>
- **Video Analytics** Dive deep into Kick videos with a wealth of data at your fingertips. Retrieve details including video title, thumbnail URL, duration, live stream ID, creation and update timestamps, UUID, views count, language, stream video URL, and associated channel details.

## Contributing
We welcome contributions from the community! If you'd like to contribute to the development of KickApi, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure the code passes all tests.
- Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Make sure to include a `LICENSE` file in your project's root directory and specify the licensing details in that file. The provided link in the "License" section should point to the actual `LICENSE` file in your project.