from urllib.parse import urlparse


def is_reddit_url(url):
    try:
        # Parse the URL into components
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()

        # Check if the domain belongs to Reddit
        return "reddit.com" in domain or domain == "redd.it"
    except Exception:
        return False


# --- Example Usage ---
if __name__ == "__main__":
    test_links = [
        "https://www.reddit.com/r/Python/comments/example/",
        "https://redd.it/abc1234",
        "https://www.google.com",
    ]

    for link in test_links:
        if is_reddit_url(link):
            print(f"VALID: {link}")
        else:
            print(f"INVALID: {link}")
