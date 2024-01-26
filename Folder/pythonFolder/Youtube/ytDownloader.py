from pytube import YouTube

try:
    # Prompt the user to enter a YouTube video link
    link = input("Enter the YouTube video link: ")

    # Create a YouTube object
    yt = YouTube(link)

    # Print video information
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Specify the download directory using double backslashes or a raw string
    download_directory = r"eduSite\Folder\pythonFolder\Youtube\download"
    
    # Download the video
    yd.download(download_directory)

    print("Download successful!")

except Exception as e:
    print("An error occurred:", e)
