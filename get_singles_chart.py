# import requests library for making HTTP requests to webpages
# import bs4 (BeautifulSoup) to use for web scraping
# import csv module
import requests
import bs4
import csv

def get_singles(url):
    all_singles = []
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
    singles = soup.find_all('div', class_ ='title')
    artists = soup.find_all('div', class_ ='artist')
    all_a_tags = soup.find_all('a', class_ = 'chart-runs-icon icon-circle-plus')

    # # Loop through each a tag and extract the third substring from the data-productid attribute
    isrc = [a['data-productid'].split('-')[2] for a in all_a_tags]

    # create a list of each track, tidying the format
    for i in range(0, len(positions)):
        single = []
        single.append(date.strip('\r').strip('\n').strip(' '))
        single.append(positions[i].text)
        single.append(artists[i].text.strip('\n').strip('\r'))
        single.append(singles[i].text.strip('\n').strip('\r'))
        single.append(isrc[i])
    # append each single list to the weeks list
        all_singles.append(single)

    # find next week's information and create link, exit loop if link can't be found
    nextlink = soup.find('a', string ='next')
    if nextlink == None:
        return None
    # get the 'href' for next week's chart
    link = (nextlink['href'])
    # get the url for next week's chart
    link = 'http://www.officialcharts.com/' + link

    # write weekly singles to CSV, appending to existing file
    with open('uk_single_charts.csv', 'a', newline='') as output:
        wr = csv.writer(output)
        wr.writerows(all_singles)

    # clear out the weekly list and proceed to next weeks file
    all_singles = []
    get_singles(link)


if __name__ == '__main__':
    # Enter start page to start the loop from 5th Jan 2018
    get_singles('https://www.officialcharts.com/charts/uk-top-40-singles-chart/20180105/750140')
