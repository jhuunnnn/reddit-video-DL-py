import os

from RedDownloader import RedDownloader
from urllib.parse import urlparse
from pathlib import Path


def download_reddit_video(reddit_url, index, target_folder):

    try:
        print(f"Attempting to download: {reddit_url}")

        # Download the video (Quality options can be 360, 720, or 1080)
        RedDownloader.Download(
            url=reddit_url,
            output=f"reddit{index}",  # Name of the output file (no extension needed)
            # destination=str(target_folder),
            quality=720,  # Target video quality
        )

        print("Download completed successfully!")

    except Exception as e:
        print("your file link is not applicable")
        print(f"An error occurred: {e}")


def mainLoop():
    target_folder = ""
    with open("testOne.txt", "r") as file:
        lines = file.readlines()
        count = 0  ##counter for the name of the video

        for line in lines:
            if checkLink(line) == True:
                download_reddit_video(line, count, target_folder)
                count += 1
            else:
                print(f"The link is not reddit link:{line}")
                if line[0] == "f":
                    ## clean the string in the line
                    folder_name = line.replace("\n", "").replace("f", "")
                    folder_path = Path(folder_name)
                    if folder_path.exists():
                        print(
                            f"Folder `{folder_path}` already exists! Canceling creation."
                        )
                    else:
                        print("Creating a folder")
                        folder_path.mkdir()
                        print("Done Creating")
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
