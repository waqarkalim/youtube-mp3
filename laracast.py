import urllib

all_id = []
all_names = []
def get_id(page):
    start_link = page.find("<a href='/downloads")
    start_quote = page.find('/', start_link + 1)
    end_quote = page.find('?type=episode', start_quote + 1)
    id = page[start_quote + 1:end_quote]
    return id


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()

    except:
        return "error"


def for_all():
    x = 1
    while x < 11:
        all_ids = get_id(get_page('https://laracasts.com/series/do-you-react/episodes/' + str(x)))
        name = get_name(get_page('https://laracasts.com/series/do-you-react/episodes/' + str(x)))
        x += 1
        all_id.append(all_ids)
        all_names.append(name)

def get_name(page):
    start_link = page.find("<title")
    start_quote = page.find('>', start_link + 1)
    end_quote = page.find('</title>', start_quote + 1)
    name = page[start_quote + 27:end_quote - 8]
    all_names.append(name)

for_all()
print all_id
print all_names

def download(all_names):
    # number = 0
    # x = 1
    # while number < 9:
    #     number += 1
    #     name_of_download = "https://laracasts.com/" + str(all_id[number]) + "?type=episode"
    #     print name_of_download
    #     print str(number) + "." + str(all_names[x-1]) + ".mp4"
    #     test=urllib.FancyURLopener()
    #     test.retrieve(name_of_download, str(number+1) + "." + str(all_names[x]) + ".mp4")
    #     x += 2
    test=urllib.FancyURLopener()
    test.retrieve("https://laracasts.com/downloads/266?type=episode", "Hello World with React.mp4")

download(all_names)


# "http://2.media.letscodejavascript.com/video/live/tdjs" + number + ".mp4"
