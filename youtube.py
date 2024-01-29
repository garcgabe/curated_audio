import yt_dlp
import json

URLS = ["https://www.youtube.com/watch?v=WLwF_0Z2KHY"]

if __name__=="__main__":
    #help(yt_dlp.postprocessor)
    #help(yt_dlp.YoutubeDL)
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #info = ydl.extract_info(URL, download=False)
        error_code = ydl.download(URLS)

    print('Some videos failed to download' if error_code
        else 'All videos successfully downloaded')
        # ℹ️ ydl.sanitize_info makes the info json-serializable
        #print(json.dumps(ydl.sanitize_info(info)))
