import pychromecast

def Play_Mp3(google_home, url):
    mc = google_home.media_controller
    mc.play_media(url, "audio/mp3")
    mc.block_until_active()
