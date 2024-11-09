import yt_dlp


def download_video(url, download_type):
    ydl_opts = {
        "format": "bestaudio/best"
        if download_type == "audio"
        else "bestvideo+bestaudio/best",
        "outtmpl": "output/%(title)s.%(ext)s",  # Save files to the output directory
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    url = input("Enter the YouTube video/playlist URL: ")
    download_type = input(
        'Enter "audio" to download audio only or "video" to download video: '
    ).lower()
    if download_type not in ["audio", "video"]:
        print('Invalid selection. Please enter "audio" or "video".')
        return
    download_video(url, download_type)


if __name__ == "__main__":
    main()
