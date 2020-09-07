## JioSaavn API [Unofficial]

#### JioSaavn API written in Python using Django  

 ---
###### **NOTE:** You don't need to have JioSaavn link of the song in order to fetch the song details, you can directly search songs by their name. Fetching Songs/Albums/Playlists from URL is also supported in this API.  

 ---

### **Features**:
##### Currently the API can get the following details for a specific song in JSON format:
- **Song Name**
- **Singer Name**
- **Album Name**
- **Album URL**
- **Duration of Song**
- **Song Thumbnail URL (Max Resolution)**
- **Song Language**
- **Download Link**
- **Release Year**
- **Album Art Link (Max Resolution)**
- **Lyrics**
- .... and much more!

```json
{
    "album": "BIBA",
    "album_url": "https://www.jiosaavn.com/album/biba/98G3uzIs2qQ_",
    "autoplay": "false",
    "duration": "175",
    "e_songid": "ICERW0MFfQs",
    "has_rbt": "false",
    "image_url": "https://c.saavncdn.com/987/BIBA-English-2019-20190201201359-500x500.jpg",
    "label": "Joytime Collective",
    "label_url": "/label/joytime-collective-albums/",
    "language": "hindi",
    "liked": "false",
    "map": "Marshmello^~^/artist/marshmello-songs/Eevs5FiVgus_^~^Pritam Chakraborty^~^/artist/pritam-chakraborty-songs/OaFg9HPZgq8_^~^Shirley Setia^~^/artist/shirley-setia-songs/9qGdjoPJ1vM_^~^Pardeep Singh Sran^~^/artist/pardeep-singh-sran-songs/NIfiZRCrYQA_^~^Dev Negi^~^/artist/dev-negi-songs/NpCqdI4dD5U_",
    "music": "",
    "origin": "search",
    "origin_val": "biba",
    "page": 1,
    "pass_album_ctx": "true",
    "perma_url": "https://www.jiosaavn.com/song/biba/ICERW0MFfQs",
    "publish_to_fb": true,
    "singers": "Marshmello, Pritam Chakraborty, Shirley Setia, Pardeep Singh Sran, Dev Negi",
    "songid": "PIzj75J8",
    "starred": "false",
    "starring": "",
    "streaming_source": null,
    "tiny_url": "https://www.jiosaavn.com/song/biba/ICERW0MFfQs",
    "title": "BIBA",
    "twitter_url": "http://twitter.com/share?url=https%3A%2F%2Fwww.jiosaavn.com%2Fsong%2Fbiba%2FICERW0MFfQs&text=%23NowPlaying+%22BIBA%22+%40jiosaavn+%23OurSoundtrack&related=jiosaavn",
    "url": "http://h.saavncdn.com/987/cd902d048c13e5ce6ca84cc409746a5d.mp3",
    "year": "2019"
  }
```

### **Usage**:
Fetching lyrics is optional and is triggered only when it is passed as an argument in the GET Request. (**&lyrics=true**)
**If you enable lyrics search, it will take more time to fetch results**

---
##### **Universal Endpoint**: (Supports Song Name, Song Link, Album Link, Playlist Link)
```sh
https://apg-saavn-api.herokuapp.com/result/?q=<insert-jiosaavn-link-or-query-here>&lyrics=true
```
**Example:** Navigate to https://apg-saavn-api.herokuapp.com/result/?q=alone to get a JSON response of songs data in return.

----


##### **Song URL Endpoint**:
```sh
https://apg-saavn-api.herokuapp.com/song/?q=<insert-jiosaavn-song-link>&lyrics=true
```
**Example:** Navigate to https://apg-saavn-api.herokuapp.com/song/?q=https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw to get a JSON response of song data in return.

---

##### **Playlist URL Endpoint**:
```sh
https://apg-saavn-api.herokuapp.com/playlist/?q=<insert-jiosaavn-playlist-link>&lyrics=true
```
**Example:** Navigate to https://apg-saavn-api.herokuapp.com/playlist/?q=https://www.jiosaavn.com/featured/romantic-hits-2020---hindi/ABiMGqjovSFuOxiEGmm6lQ__ to get a JSON response of playlist data in return.

---

##### **Album URL Endpoint**:
```sh
https://apg-saavn-api.herokuapp.com/album/?q=<insert-jiosaavn-album-link>&lyrics=true
```
**Example:** Navigate to https://apg-saavn-api.herokuapp.com/album/?q=https://www.jiosaavn.com/album/chhichhore/V4F3M5,cNb4_ to get a JSON response of album data in return.

---

##### **Lyrics Endpoint**:
```sh
https://apg-saavn-api.herokuapp.com/lyrics/?q=<insert-jiosaavn-song-link-or-song-id>&lyrics=true
```
**Example:** Navigate to https://apg-saavn-api.herokuapp.com/lyrics/?q=https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw to get a JSON response of album data in return.

---

### © [Aditya](https://aditya-web-py.github.io)
