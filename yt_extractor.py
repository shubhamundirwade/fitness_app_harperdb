# Importing packages
# pip install youtube-dl

import youtube_dl
from youtube_dl import  DownloadError

# generating instance
ydl = youtube_dl.YoutubeDL()

# creating a function to get url's information
def get_info(url):
    with ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
                )
        except DownloadError:
            return None
        
    if "entries" in result:
        video = result["entries"][0]
    else:
        video = result
    
    # infos variable will use to fetch data from the youtube url by given list  
    infos = ["id", "title", "channel", "view_count", "like_count", 
            "channel_id", "duration", "categories", "tags"]
    
    # creating a function to change all the keys id to video_id
    def key_name(key):
        if key == "id":
            return "video_id"
        return key

    # It will keep all the keys and change the ids to video_id
    return {key_name(key): video[key] for key in infos}