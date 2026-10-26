from RedDownloader import RedDownloader 

def download_reddit_video(reddit_url,index):
    try:
        print(f"Attempting to download: {reddit_url}")
        
        # Download the video (Quality options can be 360, 720, or 1080)
        RedDownloader.Download(
            url=reddit_url, 
            output=f"reddit_download_{index}",  # Name of the output file (no extension needed)
            quality=720                # Target video quality
        )
        
        print("Download completed successfully!")
        
    except Exception as e:
        print("your file link is not applicable")
        print(f"An error occurred: {e}")

def mainLoop():
   with open("testOne.txt", "r") as file:
    lines = file.readlines()
    count = 0
    
    for line in lines:
        download_reddit_video(line,count)
        count+=1


if __name__ == "__main__":
    mainLoop()