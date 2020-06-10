# Crawler for Wikipedia

A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically 
browses the World Wide Web, typically for the purpose of Web indexing (web spidering). 

This list will hold downloaded links

```
urls_bfs = []  
```

Download the page and save it using the name '/wiki/...' this will help us construct URLS if required in future

```
def download_page(url)
```

Function to extract the links from content block of a page and return it in a list

```
def get_links_bfs(url)
```


Function for BFS crawling:

```
def bfs(url)
```
