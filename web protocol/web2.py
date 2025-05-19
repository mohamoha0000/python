import requests
import re
import json
import urllib.parse

def get_video_info(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("فشل في تحميل الصفحة")
        return None

    html = response.text

    # استخراج ytInitialPlayerResponse
    pattern = r'ytInitialPlayerResponse\s*=\s*({.+?});'
    match = re.search(pattern, html)

    if not match:
        print("لم يتم العثور على ytInitialPlayerResponse")
        return None

    player_response = json.loads(match.group(1))
    print(player_response)
    exit()
    return player_response


def extract_streams(player_response):
    streams = []

    try:
        streaming_data = player_response["streamingData"]
        formats = streaming_data.get("formats", []) + streaming_data.get("adaptiveFormats", [])
        
        for fmt in formats:
            url = fmt.get("url")
            if not url and "signatureCipher" in fmt:
                cipher = fmt["signatureCipher"]
                cipher_dict = dict(urllib.parse.parse_qsl(cipher))
                url = cipher_dict["url"]
                s = cipher_dict["s"]
                # نحاول فك الشيفرة s — هذا المثال بسيط فقط!
                signature = s[::-1]  # في الحقيقة YouTube يستخدم خوارزمية أعقد
                url += f"&sig={signature}"
            
            mime = fmt.get("mimeType", "unknown")
            quality = fmt.get("qualityLabel", fmt.get("bitrate", ""))
            streams.append({"url": url, "mime": mime, "quality": quality})
    
    except Exception as e:
        print("خطأ أثناء استخراج الروابط:", e)

    return streams


def main():
    video_id = input("📹 أدخل معرف الفيديو (مثال: dQw4w9WgXcQ): ").strip()
    player_response = get_video_info(video_id)
    if not player_response:
        return

    streams = extract_streams(player_response)
    if not streams:
        print("لم يتم العثور على روابط")
        return

    print("\n✅ الروابط المتوفرة:")
    for i, stream in enumerate(streams):
        print(f"{i + 1}. الجودة: {stream['quality']} | النوع: {stream['mime']}")
        print(f"   📎 الرابط: {stream['url']}\n")


if __name__ == "__main__":
    main()
