from __future__ import unicode_literals
import youtube_dl


def single_song(name):
    name = name.replace(" ", "+")

    url = "https://www.youtube.com/results?search_query=" + name

    def get_page(url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""

    def get_link(page):
        start_link = page.find('href="/watch?v=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url1 = page[start_quote + 1:end_quote]
        url = "https://www.youtube.com" + str(url1)
        return url

    page = get_page(url)

    download_link = get_link(page.decode("utf8"))
    return download_link


def playlist():
    name = raw_input("Enter Playlist name:- ")

    name = name.replace(" ", "+")

    url = "https://www.youtube.com/results?search_query=" + name + "+Playlist"

    endpos = 0
    list_of_songs = []

    def get_page(url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""

    def get_link(page):
        start_link = page.find('<a href="/playlist?list=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url

    def get_name(page):
        start_link = page.find('data-video-id=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

    def add_all_id_to_list(page):
        while True:
            name, endpos = get_name(page)
            if name:
                list_of_songs.append(name)
                page = page[endpos:]
            else:
                break
        return list_of_songs

    page = get_page(url)
    url_link = get_link(page.decode("utf8"))

    new_link = "https://www.youtube.com" + str(url_link)
    print new_link
    new_page = get_page(new_link)

    list_of_songs = add_all_id_to_list(new_page.decode("utf8"))
    return list_of_songs


def download_single(download_link):
    ydl = youtube_dl.YoutubeDL()
    r = None
    url = download_link
    with ydl:
        r = ydl.extract_info(url, download=False)

    options = {
        'format': 'bestaudio/best',  # choice of quality
        'extractaudio': True,  # only keep the audio
        'audioformat': "mp3",  # convert to mp3
        'outtmpl': '%(title)s.mp3',  # name the file the ID of the video
        'noplaylist': True,  # only download single song, not playlist
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


# def download_playlist(list):
#     for name in list:
#         download_link = single_song(name)
#         ydl = youtube_dl.YoutubeDL()
#         r = None
#         url = download_link
#         with ydl:
#             r = ydl.extract_info(url, download=False)
#
#         options = {
#             'format': 'bestaudio/best', # choice of quality
#             'extractaudio' : True,      # only keep the audio
#             'audioformat' : "mp3",      # convert to mp3
#             'outtmpl': '%(title)s',        # name the file the ID of the video
#             'noplaylist' : True,        # only download single song, not playlist
#         }
#         with youtube_dl.YoutubeDL(options) as ydl:
#             ydl.download([url])

def decision_making():
    decision = raw_input("Do you want to download a single song or a playlist of songs? ")

    if decision == "single" or decision == "single song" or decision == "song":
        name = raw_input("Enter Song name:- ")
        download_links = single_song(name)
        download_single(download_links)
    elif decision == "playlist" or decision == "playlist of songs":
        download_links = playlist()
        for id in download_links:
            url = "https://www.youtube.com/watch?v=" + str(id)
            print url
            download_link = single_song(url)
            download_single(download_link)

    ask_again()
def ask_again():
    answer = raw_input("To exit press 'Q' and to continue press 'C':- ")
    if answer == "Q" or answer == "q":
        quit()
    elif answer == "C" or answer == "c":
        decision_making()
decision_making()