import os

from RedDownloader import RedDownloader
from urllib.parse import urlparse
from pathlib import Path


def download_reddit_video(reddit_url, index, custom_folder_name):

    custom_path = Path.home() / "Desktop/reddit-video-DL-py" / custom_folder_name

    custom_path.mkdir(parents=True, exist_ok=True)
    try:
        print(f"Attempting to download: {reddit_url}")

        # Download the video (Quality options can be 360, 720, or 1080)
        RedDownloader.Download(
            url=reddit_url,
            output="reddit",  # Name of the output file (no extension needed)
            destination=str(custom_path),
            quality=720,  # Target video quality
        )
        print(custom_path)
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


def mainLoop():

    with open("testOne.txt", "r") as file:
        lines = file.readlines()
        count = 0  ##counter for the name of the video
        target_folder = ""
        for line in lines:
            if checkLink(line) == True:
                print(f"{target_folder}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                download_reddit_video(line, count, target_folder)
                count += 1
            else:
                print(f"The link is not reddit link:{line}")
                if line[0] == "f":
                    folder_name = line.replace("\n", "").replace("f", "")
                    target_folder = folder_name.strip()
                    print(
                        f"{target_folder}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    )
                else:
                    print("just a rumbled words")


def checkLink(url):
    try:
        parse_url = urlparse(url)
        domain = parse_url.netloc.lower()
        return "reddit.com" in domain or domain == "redd.it"

    except Exception as e:  # noqa:BLE001
        print(f"The link is not a reddit link: Details: {e}")
        return False


def create_folder():
    print("Write this folder")


if __name__ == "__main__":
    mainLoop()
