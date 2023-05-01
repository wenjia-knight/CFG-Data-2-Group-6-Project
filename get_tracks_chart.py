# import requests library for making HTTP requests to webpages
# import bs4 (BeautifulSoup) to use for web scraping
# import csv module
import requests
import bs4
import csv

def get_tracks(url):
    all_tracks = []
    print(f'Getting Page {url}')

    req = requests.get(url)
    req.raise_for_status()

    # Exit loop if status code is not 200
    if req.status_code != 200:
        return None

    # creates a BeautifulSoup object called soup. Use this object to navigate and search the HTML/XML document and extract the information we're interested in.
    soup = bs4.BeautifulSoup(req.text,'lxml')

    # Retrieve chart dates and use the first date as start date. e.g. 28 April 2023
    sdate = soup.find_all('p', class_ ='article-date')
    date = sdate[0].text.split('-')[0]

    # retrieve on position, artist, track name and ISRC number
    positions = soup.find_all('span', class_ ='position')
    titles = soup.find_all('div', class_ ='title')
    artists = soup.find_all('div', class_ ='artist')
    labels = soup.find_all('div', class_='label-cat')
    all_a_tags = soup.find_all('a', class_ = 'chart-runs-icon icon-circle-plus')

    # # Loop through each a tag and extract the third substring from the data-productid attribute
    isrc = [a['data-productid'].split('-')[2] for a in all_a_tags]

    # create a list of each track, tidying the format
    for i in range(0, len(positions)):
        track = []
        track.append(date.strip('\r').strip('\n').strip(' '))
        track.append(positions[i].text)
        track.append(titles[i].text.strip('\n').strip('\r'))
        track.append(artists[i].text.strip('\n').strip('\r'))
        track.append(labels[i].text.strip('\n').strip('\r'))
        track.append(isrc[i])
    # append each single list to the weeks list
        all_tracks.append(track)

    # find next week's information and create link, exit loop if link can't be found
    nextlink = soup.find('a', string ='next')
    if nextlink == None:
        return None
    # get the 'href' for next week's chart
    link = (nextlink['href'])
    # get the url for next week's chart
    link = 'http://www.officialcharts.com/' + link

    # write weekly singles to CSV, appending to existing file
    with open('uk_top_singles_chart.csv', 'a', newline='') as output:
        wr = csv.writer(output)
        wr.writerows(all_tracks)

    # clear out the weekly list and proceed to next weeks file
    all_tracks = []
    get_tracks(link)



if __name__ == '__main__':
    # Enter start page to start the loop from 27th April 2018
    get_tracks('https://www.officialcharts.com/charts/uk-top-40-singles-chart/20180427/750140')
