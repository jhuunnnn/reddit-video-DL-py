from RedDownloader import RedDownloader
from urllib.parse import urlparse
from pathlib import Path


def download_reddit_video(reddit_url, index, custom_folder_name):

    if not custom_folder_name:
        custom_folder_name = "general downloads"

    custom_path = Path.home() / "Desktop" / "reddit-video-DL-py" / custom_folder_name

    custom_path.mkdir(parents=True, exist_ok=True)
    try:
        print(f"Attempting to download: {reddit_url}")
        fixed_destination = str(custom_path) + "/"
        # Download the video (Quality options can be 360, 720, or 1080)
        RedDownloader.Download(
            url=reddit_url,
            output=f"reddit{index}",  # Name of the output file (no extension needed)
            destination=fixed_destination,
            quality=720,  # Target video quality
        )
        print(custom_path)
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


def mainLoop():
    try:
        with open("testOne.txt", "r") as file:
            lines = file.readlines()
            count = 0
            target_folder = "default_fodler"

            for line in lines:
                clean_line = line.strip()
                if not clean_line:
                    continue

                if clean_line.startswith("f"):
                    target_folder = clean_line.replace("f", "", 1).strip()
                    print(f"\n Target folder updated to :[{target_folder}]")
                    continue

                if checkLink(clean_line):
                    print(f"Found Valid Reddt Link! Using folder:[{target_folder}]")
                    download_reddit_video(clean_line, count, target_folder)
                    count += 1
                    continue

                else:
                    print(f"Skipped invalid link or test:{clean_line}")
    except FileNotFoundError:
        print("Error: `testOne.txt` file was not found.")


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
