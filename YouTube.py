#yt_dlp
import yt_dlp

def youtube_audio(murl):
    ydl_opts = {'format':'m4a/bestaudio/best',}
    with(yt_dlp.YoutubeDL(ydl_opts))as ydl:
        ydl.download(murl)

def fullyoutube(murl):
    def longer_than(info, *, incomplete):
        duration = info.get('duration')
        if(duration)and(duration<=30):
            return 'Too short'
    ydl_opts = {'match_filter':longer_than,}
    with(yt_dlp.YoutubeDL(ydl_opts))as ydl:
        error_code = ydl.download(murl)

fullyoutube('https://youtu.be/LIteRy3hhrE')
#youtube_audio('https://youtu.be/osS00YxeWWA')
