import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    # Prompt the user for a URL
    url = input("Enter the image URL: ").strip()

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Fetch the image from the web
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Extract filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If URL doesn't end with a filename, generate one
            filename = "downloaded_image.jpg"

        # Path to save the image
        filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image successfully downloaded and saved as {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()