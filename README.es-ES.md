

## API de JioSaavn [No oficial]

#### API de JioSaavn escrita en Python usando Django  

 ---
###### **NOTA:** No necesitas tener el enlace de JioSaavn de la canción para obtener los detalles, puedes buscar canciones directamente por su nombre. Esta API también admite obtener Canciones/Álbumes/Listas de reproducción desde una URL.  

 ---

### **Características**:
##### Actualmente, la API puede obtener los siguientes detalles para una canción específica en formato JSON:
- **Nombre de la canción**
- **Nombre del cantante**
- **Nombre del álbum**
- **URL del álbum**
- **Duración de la canción**
- **URL de la miniatura de la canción (Resolución máxima)**
- **Idioma de la canción**
- **Enlace de descarga**
- **Año de lanzamiento**
- **Enlace de la portada del álbum (Resolución máxima)**
- **Letra**
- .... ¡y mucho más!

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

### **Uso**:
La obtención de letras es opcional y solo se activa cuando se pasa como argumento en la solicitud GET. (**&lyrics=true**)
**Si habilitas la búsqueda de letras, tomará más tiempo obtener los resultados**

---
##### **Endpoint Universal**: (Admite Nombre de canción, Enlace de canción, Enlace de álbum, Enlace de lista de reproducción)
```sh
https://apg-saavn-api.herokuapp.com/result/?q=<insert-jiosaavn-link-or-query-here>&lyrics=true
```
**Ejemplo:** Navega a https://apg-saavn-api.herokuapp.com/result/?q=alone para obtener una respuesta JSON con los datos de las canciones.

----


##### **Endpoint de URL de canción**:
```sh
https://apg-saavn-api.herokuapp.com/song/?q=<insert-jiosaavn-song-link>&lyrics=true
```
**Ejemplo:** Navega a https://apg-saavn-api.herokuapp.com/song/?q=https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw para obtener una respuesta JSON con los datos de la canción.

---

##### **Endpoint de URL de lista de reproducción**:
```sh
https://apg-saavn-api.herokuapp.com/playlist/?q=<insert-jiosaavn-playlist-link>&lyrics=true
```
**Ejemplo:** Navega a https://apg-saavn-api.herokuapp.com/playlist/?q=https://www.jiosaavn.com/featured/romantic-hits-2020---hindi/ABiMGqjovSFuOxiEGmm6lQ__ para obtener una respuesta JSON con los datos de la lista de reproducción.

---

##### **Endpoint de URL de álbum**:
```sh
https://apg-saavn-api.herokuapp.com/album/?q=<insert-jiosaavn-album-link>&lyrics=true
```
**Ejemplo:** Navega a https://apg-saavn-api.herokuapp.com/album/?q=https://www.jiosaavn.com/album/chhichhore/V4F3M5,cNb4_ para obtener una respuesta JSON con los datos del álbum.

---

##### **Endpoint de letras**:
```sh
https://apg-saavn-api.herokuapp.com/lyrics/?q=<insert-jiosaavn-song-link-or-song-id>&lyrics=true
```
**Ejemplo:** Navega a https://apg-saavn-api.herokuapp.com/lyrics/?q=https://www.jiosaavn.com/song/khairiyat/PwAFSRNpAWw para obtener una respuesta JSON con los datos de la letra.

---

### © [Aditya](https://aditya-web-py.github.io)
