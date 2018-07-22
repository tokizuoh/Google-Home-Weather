import pychromecast

def Play_Mp3(url):
    chromecasts = pychromecast.get_chromecasts()
    google_home = chromecasts[0]
    mc = google_home.media_controller
    mc.play_media(url, "audio/mp3")
    mc.block_until_active()
