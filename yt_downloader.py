import yt_dlp


def download_video(url, download_type):
    ydl_opts = {
        "format": "bestaudio/best"
        if download_type == "audio"
        else "bestvideo+bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "vorbis",  # Use 'vorbis' for OGG format
            }
        ]
        if download_type == "audio"
        else [],
        "outtmpl": "output/%(title)s.%(ext)s",  # Save files to the output directory
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    url = input("Enter the YouTube video/playlist URL: ")
    download_type = input(
        'Enter "audio" to download audio only or "video" to download video (default is audio): '
    ).lower()
    if download_type not in ["audio", "video"]:
        print("Invalid selection or no selection made. Defaulting to audio.")
        download_type = "audio"
    download_video(url, download_type)


if __name__ == "__main__":
    main()
