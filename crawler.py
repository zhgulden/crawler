import httplib2
import bs4 as bs
from time import sleep
from collections import deque
from urllib.request import urlopen
import collections
from collections import defaultdict

def download_page(url):
    page = urlopen(url)
    html_content = page.read()
    html_content = str(html_content)
    url = url.split('https://en.wikipedia.org/',1)[1].replace("/","-")
    file = open('pages/' + url + '.txt', 'w')
    file.write(html_content)
    file.close()

urls_bfs = []    
                    
def get_links_bfs(url):
    urls = []
    http = httplib2.Http()
    sleep(0.1)
    status, response = http.request(url)
    soup = bs.BeautifulSoup(response, "html.parser")
    for div in soup.find_all("div", {"class":"mw-body-content"}):
        for link in div.select("a"):
            if link.has_attr('href'):
                if link['href'].startswith("/wiki/") and ":" not in link['href'] and "Main_Page" not in link['href'] and "#" not in link['href']: 
                    urls.append(link['href'])
    urls = ['https://en.wikipedia.org' + s for s in urls]
    return urls
                  
def bfs(url):
    queue = deque([(url,0)])
    depth = 1
    while queue and len(set(urls_bfs)) < 10:
        url,depth = queue.popleft()
        if depth < 3:
                download_page(url)
                if url not in urls_bfs:
                    urls_bfs.append(url)
                links = get_links_bfs(url) 
                for link in links:
                    if link not in queue and link not in urls_bfs:
                        queue.append((link, depth + 1))
                        
def print_bfs_urls():
    with open('unique-urls-bfs.txt', 'w') as f:
        for item in urls_bfs:
            f.write("%s\n" %  item)
    
def bfs_crawl(url):
    bfs(url)
    print_bfs_urls()

bfs_crawl('https://en.wikipedia.org/wiki/Main_Page')
