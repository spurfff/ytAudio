#!/usr/bin/python3


import re # import the Regular Expressions module to validate a url 
from pytube import YouTube
from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['ytAudio']
collection = db['Streams']

def is_valid_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    if re.search(r'youtube\.com', url, re.IGNORECASE):
        return re.match(url_pattern, url)

    return False

def store_stream_data(youtube_url):
    try:
        # Get YouTube Video stream details
        yt = YouTube(youtube_url)
        title = yt.title
        stream = yt.streams.get_audio_only()
        thumbnail_url = yt.thumbnail_url

        # Store the title in MongoDB
        db.Streams.insert_one({
            'title': title,
            'thumbnail_url': thumbnail_url,
            'video_url': youtube_url,
            'stream': {
                'itag': stream.itag,
                'mime_type': stream.mime_type,
                'resolution': stream.resolution,
                'size_MB': stream.filesize_mb,
                'abr': stream.abr,
                'audio_codec': stream.audio_codec,
                'type': stream.type
            }
        })


        return True, "Stream Data fetched and stored successfully"

    except Exception as e:
        return False, f"Error: {str(e)}"