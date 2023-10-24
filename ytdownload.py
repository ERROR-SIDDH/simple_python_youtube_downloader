
#BFEORE RUNNING THE CODE MAKE SURE YOU HAVE INSTALLED pytube3 module
#pip install pytube
#make sure path is correct
print('''Before running the code make sure you have installed pytube module and make sure path is correct''')



from pytube import YouTube,Playlist  #importing the module and its functions

def download_video(url, save_path): #function to download video
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(save_path)
        print("Downloading...")
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")
        



def download_audio(url, file_path): #function to download audio
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        print("Downloading...")
        audio.download(file_path)
        download_audio(url, file_path)
    except Exception as e:  
        print(f"Error: {e}")



def download_playlist(url, file_path): #function to download playlist
    playlist = Playlist(url) 
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"
    try:
        print("Downloading playlist...")
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            video = yt.streams.filter(file_extension='mp4', progressive=True).first()
            print(f"Downloading: {video_url}")
            video.download(file_path)
        print("Downloaded playlist")
    except Exception as e:  
        print(f"Error: {e}")




url=input("ENTER URL TO DOWNLOAD") #input url from user

save_path = "./OneDrive/Desktop/ytdownload"  # Replace with your desired save path
format=int(input('''ENTER 1 DOWNLOAD mp3 and 2 for mp4 and
             3 for playlist'''))#input format from user




#if statement to check if the user wants to download audio or video
if format==1: 
    download_audio(url, save_path) 
elif format==2:
    download_video(url, save_path)
elif format==3:
    download_playlist(url, save_path)
