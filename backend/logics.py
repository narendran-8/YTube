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
    itemCollection = len(result["formats"])
    for items in range(itemCollection):

        single_data["filesize"] = result["formats"][items]["filesize"]
        single_data["resolution"] = result["formats"][items]["format_note"]
        single_data["url"] = result["formats"][items]["url"]
        single_data["extention"] = result["formats"][items]["ext"]
        single_data["is_audio_available"] = result["formats"][items]["acodec"]
        single_data["format"] = result["formats"][items]["format"]

        formats.append(single_data)
     


    payload = {}

    payload["id"] = result["id"]
    payload["title"] = result["title"]
    payload["formats"] = formats
    payload["description"] = result["description"]
    payload["upload_date"] = result["upload_date"]
    payload["uploader"] = result["uploader"]
    payload["uploader_id"] = result["uploader_id"]
    payload["uploader_url"] = result["uploader_url"]
    payload["channel_id"] = result["channel_id"]
    payload["channel_url"] = result["channel_url"]
    payload["duration"] = result["duration"]
    payload["view_count"] = result["view_count"]
    payload["average_rating"] = result["average_rating"]
    payload["age_limit"] = result["age_limit"]
    payload["webpage_url"] = result["webpage_url"]
    payload["categories"] = result["categories"]
    payload["is_live"] = result["is_live"]
    payload["subtitles"] = result["subtitles"]
    payload["channel"] = result["channel"]
    payload["playlist"] = result["playlist"]
    payload["playlist_index"] = result["playlist_index"]
    payload["thumbnail"] = result["thumbnail"]
    payload["display_id"] = result["display_id"]


    result = json.dumps(payload, ensure_ascii=False).encode('utf8')
    return json.loads(result)


