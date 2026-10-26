from RedDownloader import RedDownloader 

def download_reddit_video(reddit_url):
    try:
        print(f"Attempting to download: {reddit_url}")
        
        # Download the video (Quality options can be 360, 720, or 1080)
        RedDownloader.Download(
            url=reddit_url, 
            output="reddit_download",  # Name of the output file (no extension needed)
            quality=720                # Target video quality
        )
        
        print("Download completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the full Reddit post URL: ").strip()
    
    if url:
        download_reddit_video(url)
    else:
        print("Please provide a valid URL.")