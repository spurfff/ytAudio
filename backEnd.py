#!/usr/bin/python3


import re # import the Regular Expressions module to validate a url 
from pytube import YouTube

# This functions validates a proper URL and ALSO checks that it's from youtube.com's servers
# The function accomplishes this, in a 
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

#def sift_through_streams(url):
#    yt = YouTube(url)
#    title = yt.title
#    audio_streams = yt.streams.filter(only_audio=True, file_extension='webm')
#    sorted_streams = sorted(audio_streams, key=lambda stream: int(stream.abr[-4]), reverse=True)