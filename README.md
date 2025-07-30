# YouTube Video Downloader

A simple Python script that downloads YouTube videos in the highest resolution using the pytube library.

## Requirements

Before running this script, you need to meet the following requirements:

### Python Version
- Python 3.6 or higher

### Libraries
```bash
pip install pytube
```

## Installation

1. Clone this repository or download the script file to your computer
2. Open terminal or command prompt
3. Navigate to the folder containing the script file
4. Install the required library:
   ```bash
   pip install pytube
   ```

## Usage

1. Run the script in terminal or command prompt:
   ```bash
   python youtube_downloader.py
   ```

2. The program will ask for a YouTube video URL. Enter the complete URL of the video you want to download:
   ```
   Please enter the URL of the YouTube video you want to download: https://www.youtube.com/watch?v=example
   ```

3. The script will automatically download the video in the highest available resolution.

## Features

- **Highest Resolution**: Videos are automatically downloaded in the highest available resolution
- **Simple Usage**: Just enter the URL and you're done
- **Fast Download**: Utilizes pytube library's optimized download functionality

## Download Location

By default, videos are downloaded to the same folder as the script file. You can change the download location by editing the `path` variable:

```python
path = "C:/Downloads/"  # For Windows
path = "/home/user/Videos/"  # For Linux
path = "/Users/user/Downloads/"  # For macOS
```

## Supported Formats

The script supports all video formats available on YouTube and automatically selects the highest quality version.

## Troubleshooting

### Common Errors

**ModuleNotFoundError: No module named 'pytube'**
- Solution: Run `pip install pytube`

**Video could not be downloaded**
- Make sure the URL is correct
- Check your internet connection
- Ensure the video is publicly available

**Pytube version issues**
- Install the latest version: `pip install --upgrade pytube`

## Important Notes

- This script is for educational purposes only
- Follow local laws when downloading copyrighted content
- Respect YouTube's terms of service
- Do not use downloaded videos for commercial purposes

## License

This project is prepared for educational purposes. Use at your own responsibility.

## Contributing

To improve this simple script:
- Report bugs
- Suggest new features
- Propose code improvements

## Version History

- **v1.0**: Basic YouTube video download functionality
