import os
import yt_dlp


def dl_audio(url,output):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': output +"/fichier_telecharge.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def main_dowload (video_url):
    output = os.getcwd()+"\\Data\\"
    dl_audio(video_url,output)
    print(output)
      
main_dowload ("https://www.youtube.com/watch?v=TXGbhniTBrU")