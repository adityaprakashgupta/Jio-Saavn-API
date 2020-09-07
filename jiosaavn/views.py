from django.shortcuts import render
from django.http import JsonResponse
import time
from . import jios
import os
from traceback import print_exc
# Create your views here.
def home(request):
    return render(request, 'jiosaavn/jiosaavn.html')

def search(request):
    lyrics = False
    query = request.GET.get('q')
    lyrics_ = request.GET.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        #return jsonify(jiosaavn.search_for_song(query,lyrics))
        song_id = jios.get_song_id(query)
        song = jios.get_song(song_id,lyrics)
        return JsonResponse(song)
    else:
        error = {
            "status": False,
            "error":'Query is required to search songs!'
        }
        return JsonResponse(error)

def playlist(request):
    lyrics = False
    query = request.GET.get('q')
    lyrics_ = request.GET.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        id = jios.get_playlist_id(query)
        songs = jios.get_playlist(id,lyrics)
        return JsonResponse(songs)
    else:
        error = {
            "status": False,
            "error":'Query is required to search playlists!'
        }
        return JsonResponse(error)

def album(request):
    lyrics = False
    query = request.GET.get('q')
    lyrics_ = request.GET.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True
    if query:
        id = jios.get_album_id(query)
        songs = jios.get_album(id,lyrics)
        return JsonResponse(songs)
    else:
        error = {
            "status": False,
            "error":'Query is required to search albums!'
        }
        return JsonResponse(error)

def lyrics(request):
    query = request.GET.get('q')

    if query:
        try:
            if 'http' in query and 'saavn' in query:
                id = jios.get_song_id(query)
                lyrics = jios.get_lyrics(id)
            else:
                lyrics = jios.get_lyrics(query)
            response = {}
            response['status'] = True
            response['lyrics'] = lyrics
            return JsonResponse(response)
        except Exception as e:
            error = {
            "status": False,
            "error": str(e)
            }
            return JsonResponse(error)
        
    else:
        error = {
            "status": False,
            "error":'Query containing song link or id is required to fetch lyrics!'
        }
        return JsonResponse(error)

def result(request):
    lyrics = False
    false = False
    true = True
    query = request.GET.get('q')
    lyrics_ = request.GET.get('lyrics')
    if lyrics_ and lyrics_.lower()!='false':
        lyrics = True

    if 'saavn.com' not in query:
        return JsonResponse(jios.search_for_song(query,lyrics), safe=False)
    try:
        if '/song/' in query:
            print("Song")
            song_id = jios.get_song_id(query)
            song = jios.get_song(song_id,lyrics)
            return JsonResponse(song)

        elif '/album/' in query:
            print("Album")
            id = jios.get_album_id(query)
            songs = jios.get_album(id,lyrics)
            return JsonResponse(songs)

        elif '/playlist/' or '/featured/' in query:
            print("Playlist")
            id = jios.get_playlist_id(query)
            songs = jios.get_playlist(id,lyrics)
            return JsonResponse(songs)

    except Exception as e:
        print_exc()
        error = {
            "status": True,
            "error":str(e)
        }
        return JsonResponse(error)
    return None