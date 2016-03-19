import urllib


def get_name(page):
    all_name = []
    x = 1
    start_quote = 0
    while x <= 343:
        start_link = page.find('E' + str(x) + '</span', start_quote)
        x += 1
        start_quote = page.find('>', start_link + 3)
        end_quote = page.find('</h4>', start_quote + 1)
        if x < 10:
            name = page[start_quote + 1:end_quote - 17]
        elif 9 < x < 100:
            name = page[start_quote + 1:end_quote - 17]
        elif 100 <= x < 355:
            name = page[start_quote + 1:end_quote - 17]

        all_name.append(name)
    return all_name


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()

    except:
        return "error"


all_names = get_name(get_page('http://www.letscodejavascript.com/v3/episodes/live'))
length = len(get_name(get_page('http://www.letscodejavascript.com/v3/episodes/live')))


# print all_names
# print length

def download(all_names):
    number = 58
    while number <= 68:
        number += 1
        print str(number) + "." + str(all_names[number - 1]) + ".mp4"
        test = urllib.FancyURLopener()
        test.retrieve("http://2.media.letscodejavascript.com/video/live/tdjs" + str(number) + ".mp4",
                      str(number) + "." + str(all_names[number - 1]) + ".mp4")


download(all_names)

# "http://2.media.letscodejavascript.com/video/live/tdjs" + number + ".mp4"
# "http://2.media.letscodejavascript.com/video/how_to/ht2.mp4"
# "http://2.media.letscodejavascript.com/video/lessons_learned/ll0.mp4"
# "http://2.media.letscodejavascript.com/video/lab/lab1.mp4"
