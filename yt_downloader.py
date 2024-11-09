from pytube import Playlist, YouTube
from tqdm import tqdm
import os

# Define a callback function to update the progress bar


def on_progress(stream, chunk, bytes_remaining):
    # Calculate the percentage complete
    percent_complete = (stream.filesize - bytes_remaining) / stream.filesize
    # Update the progress bar
    progress_bar.update(percent_complete - progress_bar.n)


# Prompt the user for the URL
url = input("Enter the YouTube playlist or video URL: ")

# Prompt the user for the download type
download_type = input("Enter the download type (audio or video): ")

# Set the download folder to an "output" folder in the current directory
download_folder = os.path.join(os.getcwd(), "output")

# Create the download folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Initialize a list to store the downloaded files
downloaded_files = []

# Check if the URL is a playlist or a single video
if "list=" in url:
    # Create a Playlist object
    playlist = Playlist(url)

    # Loop over each video in the playlist
    for i, video in enumerate(playlist.videos):
        try:
            # Register the on_progress callback function
            video.register_on_progress_callback(on_progress)

            # Check if the user wants to download audio or video
            if download_type == "audio":
                # Get the audio stream
                stream = video.streams.filter(only_audio=True).first()
            else:
                # Get the highest quality video stream
                stream = video.streams.get_highest_resolution()

            # Create a progress bar for this download with a counter
            progress_bar = tqdm(
                total=1.0, desc=f"Downloading {i+1}/{len(playlist.video_urls)}: {stream.default_filename}", unit="file")

            # Download the stream to the specified folder
            file_path = stream.download(output_path=download_folder)
            # Add the file path to the list of downloaded files
            downloaded_files.append(file_path)

            # Close the progress bar for this download
            progress_bar.close()
        except Exception as e:
            print(f"Skipping video due to error: {e}")
else:
    # Create a YouTube object
    video = YouTube(url)

    try:
        # Register the on_progress callback function
        video.register_on_progress_callback(on_progress)

        # Check if the user wants to download audio or video
        if download_type == "audio":
            # Get the audio stream
            stream = video.streams.filter(only_audio=True).first()
        else:
            # Get the highest quality video stream
            stream = video.streams.get_highest_resolution()

        # Create a progress bar for this download without a counter
        progress_bar = tqdm(
            total=1.0, desc=f"Downloading {stream.default_filename}", unit="file")

        # Download the stream to the specified folder
        file_path = stream.download(output_path=download_folder)
        # Add the file path to the list of downloaded files
        downloaded_files.append(file_path)

        # Close the progress bar for this download
        progress_bar.close()
    except Exception as e:
        print(f"Skipping video due to error: {e}")

# Print a summary of the download
print(
    f"\nDownload complete! {len(downloaded_files)} file(s) downloaded to {download_folder}:")
for file_path in downloaded_files:
    print(f"- {os.path.basename(file_path)}")
