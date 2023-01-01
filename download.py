from pytube import YouTube
from pytube.exceptions import VideoUnavailable

class YTDownload:
    def __init__(self, url):
        self.yt = YouTube(url)
        try:
            self.yt.check_availability()
            print("found")
            
            #yt.streams.first().download()
        except VideoUnavailable:
            print("video anable to find")

    def Video_download(self):
        stream = self.yt.streams.get_by_itag(22)
        return stream.download()
        