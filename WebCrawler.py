import requests
response = requests.get('https://en.wikipedia.org/wiki/Djaoeh_Dimata')

#check status code
print(response.status_code)

print(type(response.txt))

whtml = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(whtml,'html.parser')
print(soup.p.a)


'''
Breaking the problem into steps
1.Open an article
2. Find the first link in the article
3. Follow the link
4. Repeat till the final link is visited or the program repeats the links
'''


'''
Recording our Progress
Breaking the problem into steps
1.Open an article
2. Find the first link in the article
3. Follow the link
4.Record the link in the wiki_chain data structure
5. Repeat till the final link is visited or the program repeats the links
'''
'''
The program should end the while loop:
* It has reacched philosophy page
* we have reached a page that we have already visited. (eg  chair)
* the program goes for more than 25 iterations
* We reach a page that has no links
'''

'''
PSEUDO CODE

page = a random starting page
while title of page isn't philosophy and we havent discovered a cycle
* append the page to article_chain
* download the page content
* find the first link in the content
* page = that link
* pause for a sec or two

1. Main loop - the wiki chain, limit the rate of request, print(output)
2. request code - make request and find links
'''

def perform_crawl(search_history,target_url):
    if search_history[-1] == target_url:
        print('We have found the target article')
        return False
    elif len(search_history)>max_steps:
        print('The search has gone very long')
        return False
    elif(search_history[-1] in search_history[:-1]):
        print('We have reached a cycle')
        return False
    else:
        return True

while continue_crawl(article_chain, target_url):
    #download html of last article in article_chain using requests
    #find the first link in that html- using bs4
    # add the first link to article_chain
    #delay for about two seconds

#dont run
import time
while continue_crawl(article_chain, target_url):
    '''
    #download html of last article in article_chain using requests
    #find the first link in that html- using bs4
    # add the first link to article_chain
    #delay for about two seconds
    '''
    first_link = find_first_link(article_chain[-1])
    article_chain.append(first_link)
    time.sleep(2)

def find_first_link(url):
    '''
    1.get the html from 'url' using request module or library
    2.feed the html into bs4
    3.find the first link
    4. return the first linnk, or set to None if no link exist
    '''
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html,'html.parser')

    #TODO: find the first link in the article

    #this div tag contains the article's body
    content_div = soup.find(id = 'mw-content-text').find(class_='mw-parser-output')

    #stores the first link found in the article, if thearticle contains no links, it will set to none
    article_link = None

    #find all the direct children of content_div that are paragraphs
    for element in content_div.find_all('p',recursive = False):

        if element.find('a',recursive = False):
            first_relative_link = element.find('a'.recursive = False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.url.join('')

    return first_link

    

    soup.find(id = 'mw-content-text').find(class_='mw-parser-output').p.a.get('href')

    #Let's rewrite
    content_div = soup.find(id = 'mw-content-text').find(class_='mw-parser-output').p.a.get('href')
    for element in content_div.find_all('p',recursive = False):
        if element.a:
            first_relative_link = element.a.get('href')

     #Let's rewrite
    content_div = soup.find(id = 'mw-content-text').find(class_='mw-parser-output').p.a.get('href')
    for element in content_div.find_all('p',recursive = False):
        if element.find('a',recursive = False):
            first_relative_link = element.find('a'.recursive = False).get('href')
            break

    #dont run
    import time
    import urllib
    from bs4 import BeautifulSoup
    import requests
    start_url = 'https://en.wikipedia'
    target_url = ''
    article_chain = [start_url]
    while perform_crawl(article_chain, target_url, max_steps = 25):
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])
        article_chain.append(first_link)
        time.sleep(2)
