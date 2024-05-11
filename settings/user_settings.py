import json

def my_hook(d):
    if d['status'] == 'finished':
        pass
        # with open('test_fin.json', 'w', encoding= 'utf-8') as f:
        #     json.dump(d, f, indent=4, ensure_ascii=False)
    elif d['status'] == 'downloading':
        # with open('test_down.json', 'w', encoding= 'utf-8') as f:
        #     json.dump(d, f, indent=4, ensure_ascii=False)
        print(f'Загружено {d["downloaded_bytes"]} из {d["total_bytes"]}')



YDL_OPTS = {
    'quiet': True,
    'writethumbnail': False,
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': 'downloads{/%(title)s.%(ext)s}',
    'socket_timeout': 5,  # чтобы снизить уровень вывода
    'allow_multiple_video_streams': True,
    'retries': 20,
    'fragment_retries': 10,
    'ffmpeg_location': 'ffmpeg',
    'progress_hooks': [my_hook]
}
