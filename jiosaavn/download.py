import tempfile as tf
import eyed3
import os
import json
import requests
# file = tf.NamedTemporaryFile(suffix='.mp3', delete=False)
# file_path = file.name
url = 'https://apg-saavn-api.herokuapp.com/song/?q='
song_url = 'https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw'
req = json.loads(requests.get(url+song_url).text)
print(type(req))