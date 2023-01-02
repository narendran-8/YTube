from passlib.context import CryptContext
import youtube_dl
import json



# to check password and conform password
def password_check(password, c_password):
    if password == c_password:
        return True
    else:
        return False

#------------------------------------------------
# Hash the password
def hash_password(password):
    pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pass_context.hash(password)


#------------------------------------------------
# youtube link generate
def yt_link_gen(video_url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            video_url,
            download=False 
        )

    formats =[]
    single_data = {}
    for items in range(len(result["formats"])):

        single_data["filesize"] = result["formats"][items]["filesize"]
        single_data["resolution"] = result["formats"][items]["format_note"]
        single_data["url"] = result["formats"][items]["url"]
        single_data["extention"] = result["formats"][items]["ext"]
        single_data["is_audio_available"] = result["formats"][items]["acodec"]
        single_data["format"] = result["formats"][items]["format"]

        formats.append(single_data)
     
    payload = {}

    video_attribute = ["id","title","formats","description","upload_date","uploader","uploader_id",
    "uploader_url","channel_id","channel_url","duration","view_count","average_rating","age_limit","webpage_url",
    "categories","is_live", "subtitles", "channel", "playlist","playlist_index","thumbnail","display_id"]

    for items in video_attribute:
        if items =="formats":
            payload["formats"] = formats
            continue  
        payload[items] = result[items]

    result = json.dumps(payload, ensure_ascii=False).encode('utf8')
    return json.loads(result)


