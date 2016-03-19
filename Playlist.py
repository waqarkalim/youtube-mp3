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
    start_link = page.find('data-title=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def add_all_names_to_list(page):
    while True:
          name, endpos = get_name(page)
          if name:
                list_of_songs.append(name)
                page = page[endpos:]
          else:
                break
    print list_of_songs

page = get_page(url)
url_link = get_link(page)

new_link = "https://www.youtube.com" + str(url_link)

new_page = get_page(new_link)

add_all_names_to_list(new_page)
